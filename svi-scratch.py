import xarray as xr
import rasterio
import rasterio.mask
import geopandas as gpd
import matplotlib.pyplot as plt
import pygris
import numpy as np

# Fetch Detroit boundary using pygris
detroit = pygris.places(state="MI", year=2022)
detroit = detroit[detroit['NAME'] == 'Detroit']

# Convert to GeoDataFrame (it already is, but let's ensure it)
detroit = gpd.GeoDataFrame(detroit, geometry='geometry', crs='EPSG:4269')

# Specify the TIF files
tif_files = [
    "data/svi/svi_2020_tract_overall_wgs84.tif" ,
    "data/svi/svi_2020_tract_minority_wgs84.tif",
    "data/svi/svi_2020_tract_socioeconomic_wgs84.tif",
    "data/svi/svi_2020_tract_housing_wgs84.tif",
    "data/svi/svi_2020_tract_household_wgs84.tif"]

# Create an empty list to store the individual DataArrays
data_arrays = []

# Read each TIF file, clip it to Detroit's extent, and append it to the list
for file in tif_files:
    with rasterio.open(file) as src:
        # Reproject Detroit boundary to match the raster CRS
        detroit_reprojected = detroit.to_crs(src.crs)
        
        # Clip the raster to Detroit's geometry
        out_image, out_transform = rasterio.mask.mask(src, detroit_reprojected.geometry, crop=True)
        out_meta = src.meta.copy()
        
        # Update the metadata
        out_meta.update({"driver": "GTiff",
                         "height": out_image.shape[1],
                         "width": out_image.shape[2],
                         "transform": out_transform})
        
        # Create coordinates
        height = out_meta['height']
        width = out_meta['width']
        cols, rows = np.meshgrid(np.arange(width), np.arange(height))
        xs, ys = rasterio.transform.xy(out_transform, rows, cols)
        
        # Create a DataArray from the clipped data
        da = xr.DataArray(out_image[0],  # Use the first band
                          coords={'y': ('y', ys[0]),
                                  'x': ('x', xs[:,0])},
                          dims=['y', 'x'])
        da.attrs['crs'] = src.crs
        da.attrs['transform'] = out_transform
        data_arrays.append(da)

# Combine all DataArrays into a single DataSet
ds = xr.concat(data_arrays, dim='layer')

# Rename the layers
layer_names = ['Overall', 'Socioeconomic', 'Minority', 'Housing', 'Household']
ds['layer'] = layer_names

# Create a multipanel plot
fig, axes = plt.subplots(3, 2, figsize=(15, 20))
axes = axes.flatten()

# Plot each layer
for i, layer in enumerate(layer_names):
    im = ds[i].plot(ax=axes[i], add_colorbar=False)
    axes[i].set_title(layer)
    
    # Plot Detroit boundary
    detroit_reprojected.boundary.plot(ax=axes[i], color='red', linewidth=1)

# Remove the extra subplot
fig.delaxes(axes[5])

# Add a single colorbar
cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])
fig.colorbar(im, cax=cbar_ax, label='Value')

plt.tight_layout()
plt.show()
# Get the rocker image we want
# FROM ubuntu:20.04
FROM rocker/binder

# Python Environment
## python and pip
USER root
RUN apt-get update

## python geospatial
RUN pip install geopandas pyproj shapely xarray rioxarray 
RUN pip install rasterio netcdf4 h5netcdf dask bottleneck nc-time-axis
RUN pip install numpy pandas matplotlib 
RUN pip install requests

# Juan
RUN pip install rasterstats pygadm plotly

CMD ["/init"]
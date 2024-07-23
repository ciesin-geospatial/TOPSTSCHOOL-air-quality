# Get the rocker image we want
FROM rocker/binder:latest

# Python Environment
## python and pip
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
## python geospatial
RUN pip install geopandas pyproj shapely xarray rioxarray 
RUN pip install rasterio netcdf4 h5netcdf dask bottleneck 
RUN pip install numpy pandas nc-time-axis requests
## exactextract
### dependencies
RUN pip install CMake pybind11 GEOS
### latest on git
RUN pip install git+https://github.com/isciences/exactextract.git

CMD ["/init"]
""" Utility functions for tests. """
import numpy as np
import pytest
from affine import Affine
import rasterio as rio


@pytest.fixture
def basic_image():
    """
    A 10x10 array with a square (3x3) feature
    Equivalent to results of rasterizing basic_geometry with all_touched=True.
    Borrowed from rasterio/tests/conftest.py

    Returns
    -------
    numpy ndarray
    """
    image = np.zeros((10, 10), dtype=np.uint8)
    image[2:5, 2:5] = 1
    return image


@pytest.fixture
def basic_image_2():
    """
    A 10x10 array with a square (3x3) feature
    Equivalent to results of rasterizing basic_geometry with all_touched=True.
    Borrowed from rasterio/tests/conftest.py

    Returns
    -------
    numpy ndarray
    """
    image = np.zeros((20, 20), dtype=np.uint8)
    image[2:5, 2:5] = 1
    return image


@pytest.fixture
def basic_image_tif(tmpdir, basic_image):
    """
    A GeoTIFF representation of the basic_image array.
    Borrowed from rasterio/tests/conftest.py

    Returns
    -------
    string path to raster file
    """
    outfilename = str(tmpdir.join("basic_image.tif"))
    kwargs = {
        "crs": rio.crs.CRS({"init": "epsg:4326"}),
        "transform": Affine.identity(),
        "count": 1,
        "dtype": rio.uint8,
        "driver": "GTiff",
        "width": basic_image.shape[1],
        "height": basic_image.shape[0],
        "nodata": None,
    }
    with rio.open(outfilename, "w", **kwargs) as out:
        out.write(basic_image, indexes=1)
    return outfilename


@pytest.fixture
def basic_image_tif_2(tmpdir, basic_image_2):
    """
    A GeoTIFF representation of the basic_image_2 array.
    Borrowed from rasterio/tests/conftest.py

    Returns
    -------
    string path to raster file
    """
    outfilename = str(tmpdir.join("basic_image_2.tif"))
    kwargs = {
        "crs": rio.crs.CRS({"init": "epsg:4326"}),
        "transform": Affine.identity(),
        "count": 1,
        "dtype": rio.uint8,
        "driver": "GTiff",
        "width": basic_image_2.shape[1],
        "height": basic_image_2.shape[0],
        "nodata": None,
    }
    with rio.open(outfilename, "w", **kwargs) as out:
        out.write(basic_image_2, indexes=1)
    return outfilename


@pytest.fixture
def basic_image_tif_CRS(tmpdir, basic_image):
    """
    A GeoTIFF representation of the basic_image array with a different CRS.
    Borrowed from rasterio/tests/conftest.py

    Returns
    -------
    string path to raster file
    """
    outfilename = str(tmpdir.join("basic_image_CRS.tif"))
    kwargs = {
        "crs": rio.crs.CRS({"init": "epsg:3857"}),
        "transform": Affine.identity(),
        "count": 1,
        "dtype": rio.uint8,
        "driver": "GTiff",
        "width": basic_image.shape[1],
        "height": basic_image.shape[0],
        "nodata": None,
    }
    with rio.open(outfilename, "w", **kwargs) as out:
        out.write(basic_image, indexes=1)
    return outfilename


@pytest.fixture
def basic_image_tif_Affine(tmpdir, basic_image):
    """
    A GeoTIFF representation of the basic_image array with a different affine transform.
    Borrowed from rasterio/tests/conftest.py

    Returns
    -------
    string path to raster file
    """
    outfilename = str(tmpdir.join("basic_image_Affine.tif"))
    kwargs = {
        "crs": rio.crs.CRS({"init": "epsg:4326"}),
        "transform": Affine(2.0, 0.0, 0.0, 0.0, 2.0, 0.0),
        "count": 1,
        "dtype": rio.uint8,
        "driver": "GTiff",
        "width": basic_image.shape[1],
        "height": basic_image.shape[0],
        "nodata": None,
    }
    with rio.open(outfilename, "w", **kwargs) as out:
        out.write(basic_image, indexes=1)
    return outfilename


@pytest.fixture
def image_array_2bands():
    return np.random.randint(10, size=(2, 4, 5))

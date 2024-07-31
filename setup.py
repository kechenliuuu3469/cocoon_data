from setuptools import setup, find_packages

setup(
    name="cocoon_data_custom",
    version="0.1.91",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    extras_require={
        "geo": ["geopandas==0.14.1", "rasterio", "pyproj", "shapely", "scipy"],
        "bedrock": ["boto3==1.34.90"],
    },
    author="Zachary Huang",
    author_email="zh2408@columbia.edu",
    description="Cocoon is an open-source project that aims to free analysts from tedious data transformations with LLM.",
    url="https://github.com/kechenliuuu3469/cocoon_data.git",
)

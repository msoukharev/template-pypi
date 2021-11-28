import setuptools

with open("README.md", "rt", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    # name="",
    # version="0.0.1",
    # author="",
    # author_email="",
    # description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="",
    # project_urls={
    #     "Bug Tracker": "https://github.com/msoukharev/pydatamocker",
    # },
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
    # package_dir={"": "."},
    # packages=setuptools.find_packages(where='.'),
    # python_requires=">=3.6",
    # package_data={
    #     "": [ "data/*.*" ]
    # }
)

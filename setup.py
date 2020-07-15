from setuptools import setup, find_packages

setup(
    name='pytextdistance',
    version='0.0.2',
    author='Kanae Ohta',
    author_email='kanae5321@gmail.com',
    url='https://github.com/taKana671/PyTextDistance.git',
    descriptions='Cython implementation to calculate text distance',
    long_description='README',
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
)

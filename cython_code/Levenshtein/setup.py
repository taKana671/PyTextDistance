from distutils.core import setup
from Cython.Build import cythonize

setup(name='cylevenshtein',
    ext_modules=cythonize('cylevenshtein.pyx'))
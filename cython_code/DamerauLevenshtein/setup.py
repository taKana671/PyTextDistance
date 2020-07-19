from distutils.core import setup
from Cython.Build import cythonize

setup(name='cydameraulevenshtein',
    ext_modules=cythonize('cydameraulevenshtein.pyx'),
)
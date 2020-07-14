from distutils.core import setup
from Cython.Build import cythonize


setup(name='cyjarowinkler',
    ext_modules=cythonize('cyjarowinkler.pyx'),
)
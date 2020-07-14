from distutils.core import setup
from Cython.Build import cythonize


setup(name='cyhamming',
    ext_modules=cythonize('cyhamming.pyx'),
)
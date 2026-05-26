
from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "app_tools.encryption.xor_tools", ["app_tools/encryption/xor_tools.pyx"], language="c"
    ),
]

setup(
    name="app_tools",
    packages=[],
    zip_safe=False,
    ext_modules=cythonize(
        extensions,
        compiler_directives={
            "language_level": "3",
            "boundscheck": False,
            "wraparound": False,
            "initializedcheck": False,
        },
    ),
)
import numpy as np
from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("app_tools.dirs", ["app_tools/dirs.pyx"], language="c++"),
    Extension("app_tools.queue", ["app_tools/queue.pyx"], language="c++"),
    Extension("app_tools.scanner", ["app_tools/scanner.pyx"], language="c++"),
    Extension(
        "app_tools.visualizer_compute",
        ["app_tools/visualizer_compute.pyx"],
        language="c++",
        include_dirs=[np.get_include()],
        ),

]

setup(
    name="app_tools",
    packages=[],   # ← ADD THIS
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
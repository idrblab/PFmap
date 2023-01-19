from pathlib import Path
from numpy.distutils.core import Extension
from numpy.distutils.core import setup
from setuptools import find_packages
from annopro import (
    __version__,
    __author__,
    __email__,
    __url__,
    __name__
)

PACKAGE_DIR = "."
install_requires = Path("requirements.txt").read_text().split("\n")

setup(
    name = __name__,
    version = __version__,
    author = __author__,
    author_email = __email__,
    url = __url__,
    package_dir = {"": PACKAGE_DIR},
    install_requires = install_requires,
    packages = find_packages(where=PACKAGE_DIR),
    include_package_data=True,
    package_data = {
        'annopro.data': ['*'],
        'annopro.data_procession._libprofeatconfig': ['*.sdf', '*.dat'],
        'annopro.model_param': ['*.h5']
    },
    ext_modules = [Extension(
        name="annopro.data_procession._libprofeat",
        sources=[f"{PACKAGE_DIR}/annopro/data_procession/_libprofeat.f"],
        extra_f77_compile_args=[
            ## Uncomment this arg if you using latest gfortran
            # "-fallow-argument-mismatch",
            "-w"]
    )],
    python_requires=">=3.8",
    entry_points=dict(console_scripts=["annopro = annopro:console_main"])
)
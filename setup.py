from pathlib import Path

from setuptools import find_packages, setup

REQUIRES = [
    "click==8.1.3",
    "nornir==3.3.0",
    "nornir-napalm==0.2.0",
    "nornir-utils==0.2.0",
    "rich==10.16.2",
    "pluggy>=1.0,<1.1",
]


README = (Path(__file__).parent / "README.md").read_text()


def get_version():
    """Get version"""
    global_vars = {}
    exec(Path("nornir_apps/version.py").read_text(), global_vars)
    return global_vars["__version__"]


setup(
    name="nornir-apps",
    keywords=["nornir", "nornir-cli"],
    license="MIT license",
    version=get_version(),
    author="Tafsir Thiam",
    author_email="ttafsir@gmail.com",
    url="https://github.com/ttafsir/nornir-apps",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description=("Lightweight pluggable CLI for nornir scripts"),
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=REQUIRES,
    extras_require={"test": ["pytest", "pytest-cov"]},
    packages=find_packages(exclude=("tests",)),
    entry_points={
        "console_scripts": [
            "nornir-app=nornir_apps.cli:cli",
            "nornir-apps=nornir_apps.cli:cli",
        ],
    },
    include_package_data=True,
)

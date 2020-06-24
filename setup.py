"""
jshdate
----------------

Get date ticks for statistic in JSH
"""
import os.path
from setuptools import setup

folder = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(folder, "jshdate/__init__.py")) as f:
    for line in f:
        if line.startswith("__version__ = "):
            version = line.split("=")[-1].strip().replace('"', "")
            break

setup(
    name="jshdate",
    version=version.replace("'", ""),
    url="https://github.com/lixxu/jshdate",
    license="BSD",
    author="Lix Xu",
    author_email="xuzenglin@gmail.com",
    description="Get date ticks for statistic in JSH",
    long_description=__doc__,
    packages=["jshdate"],
    zip_safe=False,
    platforms="any",
    install_requires=["python-dateutil"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

from distutils.core import setup
from PyNOAAGeoMagIndiceHandler import __version__
from PyNOAAGeoMagIndiceHandler import GeoMagReferences
from PyNOAAGeoMagIndiceHandler import decorator
from ez_setup import use_setuptools 

use_setuptools()

setup(
    name="PyNOAAGeoMagIndiceHandler",
    version=__version__,
    description="A python interface to Space NOAA Magnetometer, Solar Wind Electron Proton, Differential Flux and Anisotropy Index from ACE and Stereo A, B satellite.",
    license="BSD NEW LICENCE",
    url="http://github.com/priendeau/PyNOAAGeoMagIndiceHandler/blob/master/dist/PyNOAAGeoMagIndiceHandler-%s-apha-jedyais.tar.gz" % ( __version__ ),
    long_description=u"""A python interface to Space NOAA 
====================================
    A python interface to Space NOAA Magnetometer, Solar Wind Electron Proton, Differential Flux and 
    Anisotropy Index from ACE and Stereo A, B satellite. 
    
    In this package, I inclued pyaeso and bctc and Lomnick\xc3 \xc5t\xc3t Neutron detector as well 
    Space NOAA Magnetometer, Solar Wind Electron Proton, Differential Flux and Anisotropy Index, 
    to cross data. 
    
    This Module is a project aim to get folding indice of magnetic permeability while solar 
    flare higher than Class M. This Solara flare are mitigating the electricity current 
    flow during solar flare event and magnetic storm, and can be predicted by corrected 
    humain normal energy consumption prediction and the normal proton pression existing 
    around many region where energy can rate can be accessible with pythonic module. 
    Region being calculated with spherical harmonic matrix. 

    Can also lead to detection of future electric discontinuity during M and X Class Solar flare. 

Installing
=====================================
  It is using distutils(setup.py), so you can easily install this on most system with no trouble.
  From the base dir:
  python setup.py install (you would need root access depending on the system being used(`sudo'))
  
  You can download the latest versions released from <<No pypi for the moment, crude develpt and 
  in correct stuff will cause problem and rejection, but maxistedeams will release it >>
  or download the development version straight from the mercurial repository hosted by me at:
  git://github.com/priendeau/PyNOAAGeoMagIndiceHandler.git.

Documentation
========================================
  Is currently lacking, about every method is documented in the source. But future prototype will
  become move and more verbosis and Final realse will include test-case and a lot of documentation.
""",
    packages=["PyNOAAGeoMagIndiceHandler"],
    cmdclass={ 'GeoMagReferences': GeoMagReferences, 'decorator':decorator }
)
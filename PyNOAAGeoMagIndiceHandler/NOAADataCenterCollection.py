from __future__ import with_statement

import os, sys, re, pynav, time, datetime, pytz ,pyaeso, spharm, matplotlib, xml_marshaller, xmlbuilder
import numpy as np
from pynav import Pynav
from pyaeso import ets
from bctc import BC_TZ
from bctc.load import yield_load_points
from xml_marshaller import xml_marshaller as XmlMarshaller
from XmlMarshaller import *
from xmlbuilder import XMLBuilder
from PyNOAAGeoMagIndiceHandler import decorator
from decorator import DictAssign


"""
Sample Of Ozone NOAA Data received:
111 1975 01 23 12   22.4
111 1975 01 23 13   21.4
111 1975 01 23 14   20.9
111 1975 01 23 15   20.9
111 1975 01 23 16   20.9
111 1975 01 23 17   20.9
111 1975 01 23 18   21.4
111 1975 01 23 19   21.9
111 1975 01 23 20   22.4
111 1975 01 23 22   22.9
111 1975 01 23 23   22.9
111 1975 01 23 24   22.4


"""

class NOAADataReference( object ):

  class NOAADataReferenceImpl( object ):
    DictReference={
      'field':{
        'name':'dict',
        'value':[ 'NOAADictCollector' ],
        'dict':{
          'name':'position',
          'value':[ 'system' ],
            'position':{
              'name':'localtion',
              'value':[ 'earth','sonde','satellite' ], },
            'localtion':{
              'name':'site',
              'value':[ 'spo','sum','thd','smo','rpb','nwr','mlo','ice','brw','bmw','arh' ]  },
              'site':{
                'name':'detector',
                'value':['ozone'],
                'detector':{
                  'name':['stringfield','listfield','collectionfield'],
                  'value':[ 'title','field','laps','url','1m','5m','1h','12h','24h','1w','1m','1y','2y' ],
                  'stringfield':{
                    'name':'str',
                    'value':[ 'title', 'url'] },
                  'listfield':{
                    'name':'list',
                    'value':['field'] },
                  'collectionfield':{
                    'name':'dict',
                    'value':['laps','1m','5m','1h','12h','24h','1w','1m','1y','2y'] }
                  }
                }
              }
            }
          }

    NOAADictCollector={
      'system':{
        'earth':{
          'spo':{
            'ozone':{
              'laps':{
                '1h':{
                  'url':'ftp://ftp.cmdl.noaa.gov/ozwv/surfo3/south_pole/spclsoz' } } } },
          'sum':{
            'ozone':{
              'laps':{
                '1h':{
                  'url':'ftp://ftp.cmdl.noaa.gov/ozwv/surfo3/summit_greenland/sutclsoz' } } } },
          'thd':{
            'ozone':{
              'laps':{
                '1h':{
                  'url':'ftp://ftp.cmdl.noaa.gov/ozwv/surfo3/trinidad_head/thtclsoz' } } } },
          'smo':{
            'ozone':{
              'laps':{
                '1h':{
                  'url':'ftp://ftp.cmdl.noaa.gov/ozwv/surfo3/samoa/smclsoz' } } } },
          'rpb':{
            'ozone':{
              'laps':{
                '1h':{
                  'url':'ftp://ftp.cmdl.noaa.gov/ozwv/surfo3/barbados/baclsoz' } } } },
          'nwr':{
            'ozone':{
              'laps':{
                '1h':{
                  'url':'ftp://ftp.cmdl.noaa.gov/ozwv/surfo3/niwot_ridge/nwclsoz' } } } },
          'mlo':{
            'ozone':{
              'laps':{
                '1h':{
                  'url':'ftp://ftp.cmdl.noaa.gov/ozwv/surfo3/mauna_loa/mlclsoz' } } } },
          'ice':{
            'ozone':{
              'laps':{
                '1h':{
                  'url':'ftp://ftp.cmdl.noaa.gov/ozwv/surfo3/westman_iceland/vmclsoz' } } } },
          'brw':{
            'ozone':{
              'laps':{
                '1h':{
                  'url':'ftp://ftp.cmdl.noaa.gov/ozwv/surfo3/barrow/brclsoz' } } } },
          'bmw':{
            'ozone':{
              'laps':{
                '1h':{
                  'url':'ftp://ftp.cmdl.noaa.gov/ozwv/surfo3/bermuda/bmclsoz' } } } },
          'arh':{
            'ozone':{
              'laps':{
                '1h':{
                  'url':'ftp://ftp.cmdl.noaa.gov/ozwv/surfo3/arrival_heights/ahclsoz' } } } } } } }

  class NOAADataReferenceFactory( object ):
    Data=NOAADataReference.NOAADataReferenceImpl

  def __init__( self , **Kargs ):
    for ItemKey in Kargs.keys():
      setattr( self.Data, ItemKey, Kargs[ItemKey] )

if __name__.__eq__( '__main__' ):
  OnjNOAATest=NOAADataReference() 


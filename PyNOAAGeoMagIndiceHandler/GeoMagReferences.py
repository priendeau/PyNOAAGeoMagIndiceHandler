from __future__ import with_statement

import os, sys, re, pynav, time, datetime, pytz ,pyaeso, spharm, matplotlib,xml_marshaller, xmlbuilder, sqlitedict, UnderscoreX

from UnderscoreX import _XDecoratorWrapper

from sqlitedict import SqliteDict
from xml_marshaller import xml_marshaller 
from xml_marshaller.xml_marshaller import *
from xmlbuilder import XMLBuilder

import numpy as np
from pynav import Pynav
from pyaeso import ets
from bctc import BC_TZ
from bctc.load import yield_load_points

from PyNOAAGeoMagIndiceHandler import decorator
from decorator import DictAssign

import numericalunits as Nu
from numericalunits import *

reset_units()
set_derived_units_and_constants()


class GeoMagReferences( object ):
  NodeUpdate=None
  
  class GeoMagReferenceImpl( object ):
    FieldReference={  }
    SatelliteName=None
    LapsInterleave=None
    DictReference={
      'field':{
        'name':'dict',
        'value':[ 'RealTimeSolarIndiceReference' ],
        'dict':{
          'name':'position',
          'value':[ 'system' ],
            'position':{
              'name':'localtion',
              'value':[ 'earth','sonde','satellite' ], },
            'localtion':{
              'name':'site',
              'value':[ 'sk-ta3','ace','stereo-a','stereo-b' ]  },
              'site':{
                'name':'detector',
                'value':['neutronmonitor','swepam','magnetometer'],
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
    
    RealTimeSolarIndiceReference={
      'system':{
          'earth':{
            'sk-ta3':{
                'neutronmonitor':{
                  'laps':{
                    '1m':{ 'url':'http://neutronmonitor.ta3.sk/ascii.php?filename=/data/6h.dat' },
                    '5m':{ 'url':'http://neutronmonitor.ta3.sk/ascii.php?filename=/data/24h.dat'},
                    '1h':{ 'url':'http://neutronmonitor.ta3.sk/ascii.php?filename=/data/30d.dat' }
                    }
                  }
                }
            }, 
          'satellite':{
            'ace':{
              'swepam':{
                'title':'Solar Wind Electron Proton Alpha Monitor',
                'field':['UT Date YR', 'UT Date MO','UT Date DA','UT Date HHMM','Modified Julian Day','Seconds of the Day','S','Density','Speed','Temperature' ],
                'laps':{
                  '1m':{ 'url':"http://www.swpc.noaa.gov/ftpdir/lists/ace/ace_swepam_1m.txt" }
                  }
                 }
            },
            'stereo-a':{
              'name':{
                'a':{
                  'field':[ 'UT Date YR', 'UT Date MO', 'UT Date DA', 'UT Date HHMM', 'Modified Julian Day','Seconds of the Day','S','BR','BT','BN','Bt','Lat.','Long.' ], 
                  'magnetometer':{
                    'laps':{
                      '1m':{
                        'url':"http://www.swpc.noaa.gov/ftpdir/lists/stereo/sta_mag_1m.txt" }
                      }
                    }
                  }
                }
              },
            'stereo-b':{
              'name':{
                'a':{
                  'field':[ 'UT Date YR', 'UT Date MO', 'UT Date DA', 'UT Date HHMM', 'Modified Julian Day','Seconds of the Day','S','BR','BT','BN','Bt','Lat.','Long.' ], 
                  'magnetometer':{
                    'laps':{
                      '1m':{
                        'url':"http://www.swpc.noaa.gov/ftpdir/lists/stereo/stb_mag_1m.txt" }
                      }
                    }
                  }
                }
              }
            }
          }
      }

   
    RootName=None
    RootNameContent=None
    @DictAssign( 'RealTimeSolarIndiceReference' )
    def GetRoot( self ):
      return self.RootName, self.RootNameContent
    @DictAssign( 'RealTimeSolarIndiceReference' )
    def SetRoot( self, value ):
      DictRef=self.PropertyDictName
      self.RootName = value
      self.RootNameContent=self.RealTimeSolarIndiceReference[self.RootName]

    PropertyRoot=property( GetRoot, SetRoot )
    
    CollectionType=None
    CollectionTypeContent=None

    @DictAssign( 'RealTimeSolarIndiceReference' )
    def GetCollectionType( self ):
      return self.CollectionType, self.CollectionTypeContent

    @DictAssign( 'RealTimeSolarIndiceReference' )
    def SetCollectionType( self, value ):
      self.CollectionType = value
      self.CollectionTypeContent=self.RealTimeSolarIndiceReference[self.RootName][self.CollectionType]

    PropertyCollectionType=property( GetCollectionType, SetCollectionType )

    CollectionName=None
    CollectionNameContent=None

    @DictAssign( 'RealTimeSolarIndiceReference' )
    def GetCollectionName( self ):
      return self.CollectionName, CollectionNameContent

    @DictAssign( 'RealTimeSolarIndiceReference' )
    def SetCollectionName( self, value ):
      self.CollectionName = value
      self.CollectionNameContent=self.RealTimeSolarIndiceReference[self.RootName][self.CollectionType][self.CollectionName]

    PropertyCollectionName=property( GetCollectionName, SetCollectionName )

    CollectionSection=None
    CollectionSectionContent=None
    @DictAssign( 'RealTimeSolarIndiceReference' )
    def GetCollectionSection( self ):
      return self.CollectionSection, self.CollectionSectionContent

    @DictAssign( 'RealTimeSolarIndiceReference' )
    def SetCollectionSection( self, value ):
      self.CollectionSection = value
      self.CollectionSectionContent = self.RealTimeSolarIndiceReference[self.RootName][self.CollectionType][self.CollectionName][self.CollectionSection]

    PropertyCollectionSection=property( GetCollectionSection, SetCollectionSection )

    InstrumentName=None
    InstrumentNameContent=None

    @DictAssign( 'RealTimeSolarIndiceReference' )
    def GetInstrumentName( self ):
      return self.InstrumentName, self.InstrumentNameContent

    @DictAssign( 'RealTimeSolarIndiceReference' )
    def SetInstrumentName( self, value ):
      self.InstrumentName = value
      self.InstrumentNameContent = self.RealTimeSolarIndiceReference[self.RootName][self.CollectionType][self.CollectionName][self.CollectionSection]

    PropertyInstrumentName=property( GetInstrumentName, SetInstrumentName )

    RTSIR=None
    RTSIRContent=None
    @DictAssign( 'RealTimeSolarIndiceReference' )
    def GetRTSIR( self ):
      return self.RTSIR

    @DictAssign( 'RealTimeSolarIndiceReference' )
    def SetRTSIR( self, value ):
      self.PropertyRoot, self.PropertyCollectionType, self.PropertyCollectionName, self.PropertyCollectionSection = value
      self.RTSIR = MainDict[self.PropertyRoot][self.PropertyCollectionType][self.PropertyCollectionName][self.PropertyCollectionSection]

    PropertyRTSIR=property( GetRTSIR, SetRTSIR )
  ### Property By Instrument:

    FieldName=None
    def GetFieldName( self ):
      return self.RTSIR['field']

    def SetFieldName( self, value ):
      self.FieldName = value
      self.RTSIR['field']=self.FieldName

    PropertyFieldName=property( GetFieldName, SetFieldName )

    LapsValue=None

    def GetLapsValue( self ):
      return self.RTSIR['laps'][self.LapsValue]

    def SetLapsValue( self, value ):
      self.LapsValue = value
      
    PropertyLapsValue=property( GetLapsValue, SetLapsValue )

    UrlName=None
    UrlContent=None

    def GetUrlName( self ):
      return self.UrlContent

    def SetUrlName( self, value ):
      if len( value ) == 2 :
        self.LapsValue, self.UrlName  = value
      else:
        self.UrlName  = value
      if self.UrlName:
          self.UrlContent = self.RTSIR['laps'][self.LapsValue]['url']

    PropertyUrlName=property( GetUrlName, SetUrlName )

    Title=None
    def GetTitle( self ):
      return self.Title

    def SetTitle( self, value ):
      if value:
        self.RTSIR['laps'][self.LapsValue]['title']

    PropertyTitle=property( GetTitle, SetTitle )


    ###self.PropertyInstrumentName, self.PropertyFieldName, self.PropertyLapsValue
  def __init__( self , **Kargs ):
    Node=self.GeoMagReferenceImpl()
    for ItemKey in Kargs.keys( ):
      setattr( self.Node, ItemKey, Kargs[ItemKey] )
      
  def UpdateReference( self ):
    self.UrlNav=pynav.Pynav()
    
    
if __name__.__eq__( '__main__' ):
  AGeoLocE=GeoMagReferences()

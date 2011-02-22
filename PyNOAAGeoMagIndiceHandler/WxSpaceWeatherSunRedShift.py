#!/usr/bin/env python

import re, os, sys, tempfile

TTempHandler=tempfile.NamedTemporaryFile( 'w+', -1, suffix='', prefix='img-wxspace', dir=None, delete=True )

class DecoratorWxWeather:

  FuncName = None 

  @classmethod
  def SetFuncName( cls ):
    
    """
    This Decorator Will:
    - Create a variable funcName being assigned automatically to funcName the FunctionName

    The marshaller computes a key from function arguments
    """
    def decorator(func):
        def inner(*args, **kwargs):
          cls.FuncName = func.__name__
          func( *args, **kwargs )
        return inner
    return decorator


  
class WxWeatherPyLadModuleLoader( object ):

  BaseModuleLoad={
    '__Modpylab__'        :{
      'SystemExit':"Pylab is essential to this example." } ,
    '__Modurllib_pynav__' :{
      'SystemExit':"This example need Network support with following module( urllib, urllib2, Pynav ).",
      'ModuleVar':{
        'Pynav':'PyNavUrlLoader' } } ,
    '__ModImage__'        :{
      'SystemExit':"PIL must be installed to run this example." } ,
    '__Modmathplotlib__'  :{
      'SystemExit':"matplotlib.cbook must be installed to run this example." }
    }
  CurrVarName     = None
  
  CurrModule      = None
  CurModuleName   = None
  CurSectionName  = None
  CurItemSecName  = None 

  def GetItemSecName( self ):
    return self.CurItemSecName

  def SetItemSecName( self, value  ):
    self.CurItemSecName = value

  def GetSectionName( self ):
    return self.CurSectionName

  def SetSectionName( self, value  ):
    self.CurSectionName = value
  
  
  def GetModuleName( self ):
    return self.CurModuleName

  def SetModuleName( self, value  ):
    self.CurModuleName = value

  
  def GetVarName( self ):
    return self.CurrVarName

  def SetVarName( self, value ):
    self.CurrVarName = value 
    
  def GetVarValue( self ):
    return getattr( self, self.BaseModuleLoad[self.CurModuleName][self.CurSectionName][CurItemSecName] )

  def SetVarValue( self, value ):
    setattr( self, self.BaseModuleLoad[self.CurModuleName][self.CurSectionName][CurItemSecName] , value )

  def GetRootValue( self ):
    return GetVarValue( )

  def SetRootVar( self , value ):
    self.ModuleName, self.SectionName, self.CurItemSecName = value
    

  ### Core 
  VarName = property( GetVarName, SetVarName )

  VarValue = property( GetVarValue, SetVarValue )

  ModuleName = property( GetModuleName, SetModuleName )

  SectionName = property( GetSectionName , SetSectionName )

  ItemSecName = property( GetSectionName , SetSectionName )

  ### FrameWork
  RootValue = property( GetRootValue, SetRootVar  )

  @DecoratorWxWeather.SetFuncName( )
  def __Modpylab__( self ):
    try:
      __builtins__.__import__( 'pylab', {}, {} ,[], -1 ) 
      
      #from pylab import *
    except ImportError, exc:
        raise SystemExit( self.BaseModuleLoad[ DecoratorWxWeather.FuncName ]['SystemExit'] )

  @DecoratorWxWeather.SetFuncName( )
  def __Modurllib_pynav__( self ):
    try:
      import urllib, urllib2, pynav
      from pynav import Pynav
      setattr( self, self.BaseModuleLoad[ DecoratorWxWeather.FuncName ]['ModuleVar']['Pynav'], Pynav() )
      
    except ImportError, exc:
        raise SystemExit( self.BaseModuleLoad[ DecoratorWxWeather.FuncName ]['SystemExit'] )

  @DecoratorWxWeather.SetFuncName( )
  def __ModImage__( self ):
    try:
      #import Image
      __builtins__.__import__( 'Image', {}, {} , [], -1 ) 
    except ImportError, exc:
        raise SystemExit( self.BaseModuleLoad[ DecoratorWxWeather.FuncName ]['SystemExit'] )

  @DecoratorWxWeather.SetFuncName( )
  def __Modmathplotlib__( self ):
    try:
      #import matplotlib.cbook as cbook
      __builtins__.__import__( 'matplotlib.cbook', {}, {} , ['cbook'], -1 ) 
    except ImportError, exc:
      raise SystemExit( self.BaseModuleLoad[ DecoratorWxWeather.FuncName ]['SystemExit'] )
     

  def __init__( self ):
    for ItemModule in self.BaseModuleLoad:
      print "Calling %s from Load." % ( ItemModule )
      getattr( self, ItemModule )( )
 

AWxModluleLoad=WxWeatherPyLadModuleLoader() 


# http://www.spaceweather.com/
# http://www.spaceweather.com/images2011/18feb11/

UrlPath={ 'url':"http://www.spaceweather.com/",
          'file-filter':[ r'(?ui)images[0-9]{4}',
                          r'(?ui)/+[0-9]{2}[a-z]{3}[0-9]{2}/+' ,
                          r'(?ui)hmi4096' ]  }

if hasattr( AWxModluleLoad ,'PyNavUrlLoader' ):
  ImageUrl = AWxModluleLoad.PyNavUrlLoader.go( UrlPath['url'] )
  ImageRegList=AWxModluleLoad.PyNavUrlLoader.get_all_links( )
  ImageRegListFilter=list()

for ImageName in ImageRegList:
  CurrStreamOut='Testing Images : %s ' % ( ImageName )
  IntMatchCount=0
  for RegExpRule in UrlPath['file-filter'] :
    #print "\tBuilding RegExp : %s" % ( RegExpRule )
    CurrReg=re.compile( RegExpRule )
    if CurrReg.search( ImageName ) :
      IntMatchCount+=1
  CurrStreamOut+='\t %d matches' % IntMatchCount
  if IntMatchCount > 0 and IntMatchCount < len( UrlPath['file-filter'] )-1 :
      sys.stdout.write( "%s\n" % CurrStreamOut )
  if IntMatchCount >= len( UrlPath['file-filter'] )-1 and IntMatchCount < len( UrlPath['file-filter'] ) :
      sys.stdout.write( "Candidate( %s )\n" % CurrStreamOut )
  if IntMatchCount == len( UrlPath['file-filter'] ) :
    sys.stdout.write( "Success( %s )\n" % CurrStreamOut )

"""
###
### Twice closer to the point ; in fact there is several example in Pylab website 
###
### Reference-tables start here : http://matplotlib.sourceforge.net/gallery.html
###

  The Expectation was to query sun images and correlate each one as signal strength from simple transformations
  into frequency representation and attenuating level with csd_demo.py, go get something stable to transform
  into wavelet and vector representation of waht we catch from the sun to analyse variation of proton and
  color-discrete representation of sun-color variation....

  This is also one of theses first land-test to complete the understanding of PyNOAAGeoMagIndiceHandler for the
  mass... Involving magnetic fluctuation and electric fluctuation of human to draw a Geomagnetic Index to
  understand more the effect of Mass Proton deflection on human behavioring.


  This Work-land is also a demonstration of couple of tools and decorator, property , behavior used to approach fair
  and accepted developpment...

  Developped during spare time and during couples calls, @IBM, KellyServices for BNC Bank help center ( ... and what lying aroud to
  fairly analyse impact of 4th Generation of language and it's impact... )

  
  

"""   
  
  

#datafile = cbook.get_sample_data('lena.jpg')

#TypeImageSunDated = Image.open( ImageUrl )
#dpi = rcParams['figure.dpi']
#figsize = lena.size[0]/dpi, lena.size[1]/dpi

#figure(figsize=figsize)
#ax = axes([0,0,1,1], frameon=False)
#ax.set_axis_off()
#im = imshow(lena, origin='lower')

#show()


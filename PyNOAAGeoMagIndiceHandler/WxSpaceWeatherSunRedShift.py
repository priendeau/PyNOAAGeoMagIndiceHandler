#!/usr/bin/env python

import re, os, sys, tempfile

### Following is not needed 
### TTempHandler=tempfile.NamedTemporaryFile( 'w+', -1, suffix='', prefix='img-wxspace', dir=None, delete=True )

class DecoratorWxWeather( object ):

  FuncName                = None 
  StrClassName            = None
  StrFuncName             = None
  ModuleList              = list()
  IsProcessModuleList     = False
  RaiserInfo              = None
  DecoratorExceptError    = None
  DecoratorRaiseError     = None
  DecoratorRaiseMsg       = None
  DecorKargs              = None
  
  @classmethod
  def ScanArgs( cls ):
    print "Decorator %s, KeyList:[ %s ]" % ( 'ScanArgs', cls.DecorKargs.keys()  )
    for ItemKeyName in cls.DecorKargs.keys():
      print "\tAdd pairValue Setting Item %s, value: %s" % ( ItemKeyName, cls.DecorKargs[ItemKeyName] )
      setattr( cls, ItemKeyName, cls.DecorKargs[ItemKeyName] )

  @classmethod
  def PrintInstanceMsg( cls ):
    print "Decorator %s" % ( 'PrintInstanceMsg' )
    MsgDisplay="From Class %s, Instantiation of %s" % ( cls.StrClassName , cls.StrFuncName )
    if hasattr( cls, 'class-instance-display-msg' ):
      IsClassShow=getattr( cls, 'class-instance-display-msg' )
      if IsClassShow == True:
        print MsgDisplay
    else:
      print MsgDisplay

  @classmethod
  def ImportModule( cls ):
    print "Decorator %s ModuleList:[ %s ]" % ( 'ImportModule', cls.ModuleList  )
    try:
      for ItemName in cls.ModuleList :
        print "Processing Module %s" % ( ItemName )
        if type( ItemName ) == type( str() ):
          setattr( __builtins__, ItemName, __builtins__.__import__( ItemName, {}, {} , [], -1 ) )
        elif type( ItemName ) == type( dict() ):
          ### need Loop
          LastModule = None
          for ItemKeyName in ItemName.keys():
            if ItemKeyName != 'attr':
              setattr( __builtins__, ItemName, __builtins__.__import__( ItemName, {}, {} , [], -1 ) )
    except cls.DecoratorExceptError, exc:
        raise getattr( __builtins__, cls.DecoratorRaiseError )( DecoratorRaiseMsg )

          
  @classmethod
  def InitStructStart( cls , **Kargs ):
    cls.DecorKargs=Kargs 
    """
    This Decorator Will:
    - Create a variable funcName being assigned automatically to funcName the FunctionName

    The marshaller computes a key from function arguments
    """
    cls.ScanArgs( )
    def decorator( func ):
      def inner(*args, **kwargs):
        cls.StrClassName = cls.__name__
        cls.StrFuncName = func.__name__
        cls.PrintInstanceMsg( )
        if hasattr( cls, 'IsProcessModuleList' ):
          if cls.IsProcessModuleList == True:
            cls.ImportModule() 
        func( *args, **kwargs )
      return inner
    return decorator

  @classmethod
  def SetFuncName( cls , **Kargs ):
    
    """
    This Decorator Will:
    - Create a variable funcName being assigned automatically to funcName the FunctionName

    The marshaller computes a key from function arguments
    """
    def decorator(func):
        def inner(*args, **kwargs):
          cls.StrClassName = cls.__name__
          cls.StrFuncName = func.__name__
          cls.FuncName = func.__name__
          print "\tRegistered FuncName : %s in class %s" % ( cls.StrFuncName , cls.StrClassName )
          if cls.IsProcessModuleList == True:
            cls.ImportModule()
          cls.ModuleList=list()
          func( *args, **kwargs )
        return inner
    return decorator


  
class WxWeatherPyLabModuleLoaderFactory( object ):

  UrlPath={
    'url':"http://www.spaceweather.com/",
    'file-filter':[
      r'(?ui)images[0-9]{4}',
      r'(?ui)/+[0-9]{2}[a-z]{3}[0-9]{2}/+' ,
      r'(?ui)hmi4096' ]  }

  BaseModuleLoad={
    'list':[ '__pylab__','__urllib_pynav__','__Image__','__mathplotlib__','__UrlPayload__',
             '__Filter_Image_Url__', '__Download_Image_Url__' , '__Display_Image__' ] ,
    '__pylab__'        :{
      'modulelist':[ 'pylab' ] ,
      'SystemExit':"Pylab is essential to this example." } ,
    '__urllib_pynav__' :{
      'modulelist':[ 'urllib', 'urllib2',
                     'pynav' ,
                     { 'pynav':'Pynav', 'attr':'PyNavUrlLoader' } ] ,
      'SystemExit':"This example need Network support with following module( urllib, urllib2, Pynav ).",
      'ModuleVar':{
        'Pynav':'PyNavUrlLoader' } } ,
    '__Image__'        :{
      'modulelist':[ 'Image' ] ,
      'SystemExit':"PIL must be installed to run this example." } ,
    '__mathplotlib__'  :{
      'modulelist':[ { 'matplotlib':'cbook' } ] ,
      'SystemExit':"matplotlib.cbook must be installed to run this example." } ,
    '__UrlPayload__':{
      'modulelist':[] ,
      'SystemExit':"No PyNav Module-Attr available." },
    '__Filter_Image_Url__':{
      'SystemExit':{ 'noattr':'No Attr ImageRegList Provided within actual work-stream' ,
                     'main':"No Images provided with actual work-stream." } } ,
    '__Download_Image_Url__':{
      'modulelist':[] ,
      'temp':"c:\\docume~1\\admini~1\\locals~1\\temp\\",
      'Section':{
        'name':'ImagePattern',
        'field':'level',
        'grade':3,
        'type':type(dict()) } ,
      'SystemExit':{
        'noattr':'No Attr ImagePattern Provided within actual work-stream' ,
        'main'  :'No Downloading Images was provided with actual work-stream.' } },
    '__Display_Image__':{
      'modulelist':[] ,
      'Section':{
        'name':'ImageList',
        'type':type(list()) } ,
      'SystemExit':{
        'noattr':'No Attr ImageList Provided within actual work-stream' ,
        'main'  :'No Images was provided to display on view-screen.' } }
    }


  ImagePattern={ 'level':{ 1:[ ], 2:[ ], 3:[ ] } }
  ImageList=[ ]
  DecorTransfertKeyStep=[ { 'modulelist':{ 'method-transfert':'append' } } ]
  IntDecorKeyId = 0
  CurrentFuncParsed = None 
  
  # Dedication Content Handler 
  CurrVarName     = None

  # Dedicated to Content association 
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
  VarName     = property( GetVarName, SetVarName )

  VarValue    = property( GetVarValue, SetVarValue )

  ModuleName  = property( GetModuleName, SetModuleName )

  SectionName = property( GetSectionName , SetSectionName )

  ItemSecName = property( GetSectionName , SetSectionName )

  ### FrameWork
  RootValue   = property( GetRootValue, SetRootVar  )


  ### Stream Member 
  @DecoratorWxWeather.SetFuncName( )
  def __pylab__( self ):
    print "end of function"


  @DecoratorWxWeather.SetFuncName( )
  def __urllib_pynav__( self ):
    print "end of function"

        

  @DecoratorWxWeather.SetFuncName( )
  def __Image__( self ):
    print "end of function"


  @DecoratorWxWeather.SetFuncName( )
  def __mathplotlib__( self ):
    print "end of function"
 
  @DecoratorWxWeather.SetFuncName( )
  def __UrlPayload__( self ):
    if hasattr( self ,'PyNavUrlLoader' ):
      self.ImageUrl = getattr( getattr( self, 'PyNavUrlLoader' ), 'go' )( self.UrlPath['url'] )
      self.ImageRegList=getattr( getattr( self, 'PyNavUrlLoader' ), 'get_all_links' )( )
      self.ImageRegListFilter=list()
    else:
      raise SystemExit( self.BaseModuleLoad[ DecoratorWxWeather.FuncName ]['SystemExit'] )

  @DecoratorWxWeather.SetFuncName( )
  def __Filter_Image_Url__( self ):
    if hasattr( self, 'ImageRegList' ):
      for ImageName in getattr( self, 'ImageRegList' ):
        IntMatchCount=0
        for RegExpRule in self.UrlPath['file-filter'] :
          CurrReg=re.compile( RegExpRule )
          if CurrReg.search( ImageName ) :
            IntMatchCount+=1

        if IntMatchCount not in self.ImagePattern['level'].keys():
          self.ImagePattern['level'][IntMatchCount]=list()
          
        self.ImagePattern['level'][IntMatchCount].append( ImageName )
    else:
      raise SystemExit( self.BaseModuleLoad[ DecoratorWxWeather.FuncName ]['SystemExit']['noattr'] )

  @DecoratorWxWeather.SetFuncName( )
  def __Download_Image_Url__( self ):
    StrTempPath=self.BaseModuleLoad[ DecoratorWxWeather.FuncName ][ 'temp' ]
    DefaultDicImage = self.BaseModuleLoad[ DecoratorWxWeather.FuncName ][ 'Section' ][ 'name' ]
    FieldImage = self.BaseModuleLoad[ DecoratorWxWeather.FuncName ][ 'Section' ][ 'field' ]
    IntDefaultGradeList=self.BaseModuleLoad[ DecoratorWxWeather.FuncName ][ 'Section' ][ 'grade' ]
    if hasattr( self, DefaultDicImage ): 
      for ImageSample in getattr( self, DefaultDicImage )[ FieldImage ][ IntDefaultGradeList ]:
        ### Cleaning PHP SessionID and all suffixed informations from link :
        ListCleanFileName=ImageSample.split( '?' )
        print "Processing File : %s , downloading to path : %s" % ( ListCleanFileName[0] , StrTempPath )
        self.ImageRegList=getattr( getattr( self, 'PyNavUrlLoader' ), 'download' )( ListCleanFileName[0] , StrTempPath )
        self.ImageList.append( ListCleanFileName[0] )
        
    else:
      raise SystemExit( self.BaseModuleLoad[ DecoratorWxWeather.FuncName ]['SystemExit']['noattr'] )

  @DecoratorWxWeather.SetFuncName( )
  def __Display_Image__( self ):
    DefaultDicImage = self.BaseModuleLoad[ DecoratorWxWeather.FuncName ][ 'Section' ][ 'name' ]
    
    if hasattr( self, DefaultDicImage ):
      for ItemImageFile in getattr( self, DefaultDicImage ):
        datafile = cbook.get_sample_data( ItemImageFile )
        dataHandler = Image.open( datafile )
        dpi = rcParams['figure.dpi']
        figsize = lena.size[0]/dpi, lena.size[1]/dpi
        figure(figsize=figsize)
        ax = axes([0,0,1,1], frameon=False)
        ax.set_axis_off()
        im = imshow(dataHandler, origin='lower')
        show()

    else:
      raise SystemExit( self.BaseModuleLoad[ DecoratorWxWeather.FuncName ]['SystemExit']['noattr'] )

  def __StrutcTransfert__( self , ItemName, BasedModule , itemlist):
    return { ItemName:getattr( self, BasedModule )[ self.CurrentFuncParsed ][ itemlist ] }

  def __DecorTransfertDict__( self, ClassTransfert ):
    StrPageDictTransfert=self.DecorTransfertKeyStep[self.IntDecorKeyId]
    #print "StrPageDictTransfert: %s " % ( StrPageDictTransfert )
    #print "StrSectionTransferAttr: %s " % ( self.DecorTransfertKeyStep[self.IntDecorKeyId]['modulelist']['method-transfert'] )
    #['method-transfert'] )
    StrSectionTransferAttr=self.DecorTransfertKeyStep[self.IntDecorKeyId]['modulelist']['method-transfert']
    #for ItemName in self.BaseModuleLoad.keys():
    ItemNameDict = self.BaseModuleLoad[self.CurrentFuncParsed]
    if StrPageDictTransfert in self.BaseModuleLoad[self.CurrentFuncParsed].keys():
      NewStrucTransfert=self.__StrutcTransfert__( ItemName , self.BaseModuleLoad, modulelist )
      print "\t\tContent of StrucTransfert: %s " % ( NewStrucTransfert ) 
      getattr( getattr( ClassTransfert, ModuleList ), StrSectionTransferAttr )(  )
    
  
  @DecoratorWxWeather.InitStructStart( IsProcessModuleList=True )
  def __init__( self ):
    for ItemModule in self.BaseModuleLoad['list']:
      self.CurrentFuncParsed = ItemModule
      self.__DecorTransfertDict__( DecoratorWxWeather )
      print "Calling %s from Load." % ( ItemModule )
      DecoratorWxWeather.DecoratorExceptError=ImportError
      DecoratorWxWeather.DecoratorRaiseError='SystemExit'
      DecoratorWxWeather.DecoratorRaiseMsg = self.BaseModuleLoad[ ItemModule ]['SystemExit']
      getattr( self, ItemModule )(  )
 

AWxModluleLoad=WxWeatherPyLabModuleLoaderFactory( ) 


# http://www.spaceweather.com/
# http://www.spaceweather.com/images2011/18feb11/




##for ImageName in ImageRegList:
##  CurrStreamOut='Testing Images : %s ' % ( ImageName )
##  IntMatchCount=0
##  for RegExpRule in UrlPath['file-filter'] :
##    #print "\tBuilding RegExp : %s" % ( RegExpRule )
##    CurrReg=re.compile( RegExpRule )
##    if CurrReg.search( ImageName ) :
##      IntMatchCount+=1
##  CurrStreamOut+='\t %d matches' % IntMatchCount
##  if IntMatchCount > 0 and IntMatchCount < len( UrlPath['file-filter'] )-1 :
##      sys.stdout.write( "%s\n" % CurrStreamOut )
##  if IntMatchCount >= len( UrlPath['file-filter'] )-1 and IntMatchCount < len( UrlPath['file-filter'] ) :
##      sys.stdout.write( "Candidate( %s )\n" % CurrStreamOut )
##  if IntMatchCount == len( UrlPath['file-filter'] ) :
##    sys.stdout.write( "Success( %s )\n" % CurrStreamOut )

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


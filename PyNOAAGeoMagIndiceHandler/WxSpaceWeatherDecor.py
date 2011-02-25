
import re, os, sys, importlib 

"""
  DecoratorWxWeather,
    embedded Import-Module Mechanism with Error-catching. 
  Copyright(C) 2010, Maxiste Deams, Rheault Etccy, Patrick Riendeau ( priendea@ca.ibm.com )
  Also 'distributible' under New-Bsd License for developpement purposes


  This following model is a structure to load Element from Decorator while informations living and are stored
  from Based Classes, loading the __init__ with pre-decorated @DecoratorWxWeather.InitStructStart( IsProcessModuleList=True )
  will look for a module-list of element <WHERE> Structure will be presented in a draft-topology mechanisme for concept-proof
  brginging some tree from fore-scene to background-scene can be a good explanation from scene-1 to scene-2 memory
  model observation in finite-instruction.

  --- Under Syntaxic Correction , applied for paragrah only --- 


"""

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
  
    """
    This Part Will:
    -  --- Explained soon ----
    """
  @classmethod
  def ScanArgs( cls ):
    print "Decorator %s, KeyList:[ %s ]" % ( 'ScanArgs', cls.DecorKargs.keys()  )
    for ItemKeyName in cls.DecorKargs.keys():
      print "\tAdd pairValue Setting Item %s, value: %s" % ( ItemKeyName, cls.DecorKargs[ItemKeyName] )
      setattr( cls, ItemKeyName, cls.DecorKargs[ItemKeyName] )

    """
    This part Will:
    -  --- Explained soon ----
    """
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

    """
    This Decorator Will:
    -  --- Explained soon ----
    """
  @classmethod
  def ImportModule( cls ):
    print "Decorator %s ; Listed Module: %i ModuleList:[ %s ]" % ( 'ImportModule', len(cls.ModuleList) ,cls.ModuleList  )
    try:
      for ItemName in cls.ModuleList :
        if type( ItemName ) == type( str() ):
          print "(ItemName:%s) -> import %s" % ( ItemName , ItemName )
          getattr( importlib, 'import_module')( ItemName, package=None )
        if type( ItemName ) == type( dict() ):
          ### need Loop
          LastModule = None
          for ItemKeyName in ItemName.keys():
            if ItemKeyName != 'attr':
              print "from %s import %s" % ( ItemKeyName, ItemName[ItemKeyName] )
              getattr( importlib, 'import_module')( "%s.%s" %(  ItemName, ItemName[ItemKeyName] ) )
    except cls.DecoratorExceptError, exc:
        raise cls.DecoratorRaiseError( cls.DecoratorRaiseMsg )

    """
    This Decorator Will:
    -  --- Explained soon ----
    """
 @classmethod
  def InitStructStart( cls , **Kargs ):
    cls.DecorKargs=Kargs 
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

    """
    This Decorator Will:
    -  --- Explained soon ----
    """
  @classmethod
  def SetFuncName( cls , **Kargs ):
    
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


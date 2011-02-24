
import re, os, sys

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
    print "Decorator %s ; Listed Module: %i ModuleList:[ %s ]" % ( 'ImportModule', len(cls.ModuleList) ,cls.ModuleList  )
    try:
      for ItemName in cls.ModuleList :
        if type( ItemName ) == type( str() ):
          print "(ItemName:%s) -> import %s" % ( ItemName , ItemName )
          #setattr( __builtins__, ItemName, None )
          __builtins__.setattr( __builtins__, ItemName, None )
          __builtins__.setattr( __builtins__, ItemName, getattr(__builtins__,'__import__')( ItemName, {}, {} , [], -1 ) )
          
          #setattr( __builtins__, ItemName , getattr(__builtins__,'__import__')( ItemName, {}, {} , [], -1 ) )
        if type( ItemName ) == type( dict() ):
          ### need Loop
          LastModule = None
          for ItemKeyName in ItemName.keys():
            if ItemKeyName != 'attr':
              print "from %s import %s" % ( ItemKeyName, ItemName[ItemKeyName] )
              setattr( __builtins__, ItemName, getattr( __builtins__ , '__import__' )( ItemName[ItemKeyName], {}, {} , [], -1 ) )
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


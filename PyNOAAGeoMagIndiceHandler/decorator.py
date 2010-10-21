
###
### FileName : decorator.py
###

def DictAssign( DictName , KeyNode=None ):
    """
    This Decorator will create a Byteplay Statck known to Add Exception List in head of
    decorated function... Instead of adding raiser ( NotImplementedYet, Is ready ) This byteplay decorator
    will add it naturally, By playing with StackModule Level implemented close to here...

    See instruction on http://pypi.python.org/pypi/byteplay/N.N = ( 0.2 )

    The marshaller computes a key from function arguments
    """
    def decorator(func):
        def inner(*args, **kwargs):
            if KeyNode == None:
              kwargs.update( MainDict=getattr( self , DictName ) )
            func( *args, **kwargs )
        return inner
    return decorator

class singleton(type):
  _ins = {}
  def __call__(cls,*arg,**kwargs):
    if cls not in cls._ins:
      cls._ins[cls] = super().__call__(*arg,**kwargs)
    return cls._ins[cls]


class Test(metaclass=singleton):
  pass
  
a=Test()
b=Test()
    
# decorator

def singleton(className):
  _ins = {}
  def getIns(*args,**kwars):
    if className not in _ins:
      _ins[className] = className(*args,**kwargs)
    return _ins[className]
  return getIns

@singleton
class Test:
  pass
  
a=Test()
b=Test()

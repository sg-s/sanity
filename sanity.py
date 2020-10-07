

# use "from sanity import *" to get all these function callable in the main ws

def methods(object, spacing=20): 
    """list methods of object"""

    methodList = [] 
    for method_name in dir(object): 
        try: 
            if callable(getattr(object, method_name)): 
                methodList.append(str(method_name)) 
        except: 
            methodList.append(str(method_name)) 

    processFunc = (lambda s: ' '.join(s.split())) or (lambda s: s) 
 

    for method in methodList: 
        try: 
            print(str(method.ljust(spacing)) + ' ' + 
              processFunc(str(getattr(object, method).__doc__)[0:90])) 
        except: 
            print(method.ljust(spacing) + ' ' + ' getattr() failed') 



class BetterObjects:


    def __init__(self):
        pass

    def __repr__(self):
        obj_type = type(self).__name__
        print(obj_type + " with properties:\n")

        d = dir(self)
        for i in range(0,len(d)-1):
            if d[i].startswith("__"):
                continue
            if callable(getattr(self,d[i])):
                continue
            print("  " + d[i])

        return ""

    def methods(self):
        """return a list of methods of this object"""
        m = []
        d = dir(self)
        for i in range(0,len(d)-1):
            if d[i].startswith("__"):
                continue
            if callable(getattr(self,d[i])):
                m.append(d[i])
        return m

    def props(self):
        """return a list of properties of this object"""
        m = []
        d = dir(self)
        for i in range(0,len(d)-1):
            if d[i].startswith("__"):
                continue
            if callable(getattr(self,d[i])):
                continue
            m.append(d[i])
        return m
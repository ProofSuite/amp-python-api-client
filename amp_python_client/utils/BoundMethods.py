class BoundStaticMethods(object):
    """
    binds the static methods of instanced objects to the object as __getattr__ methods.
    """
    def __init__(self, *ARGS):
        self.bindings = {}
        try:
            [self.bindings.update(d.__class__.__dict__) for d in ARGS]
        except:
            raise Exception("Arguments must be instanced objects.")

    def update(self, *ARGS):
        try:
            [self.bindings.update(d.__class__.__dict__) for d in ARGS]
        except:
            raise Exception("Arguments must be instanced objects.")

    def __getattr__(_attr):
        return self.bindings.get(_attr) #For Safe Access


class BoundInstanceMethods(object):
    def __init__(self,*ARGS):
        self.bindings = {}
        for _obj in ARGS:
            self.bindings.update({ meth: getattr(_obj, meth) for meth in _obj.__dir__() if not meth.startswith("__")})

    def update(self, *ARGS):
        for _obj in ARGS:
            self.bindings.update({ meth: getattr(_obj, meth) for meth in _obj.__dir__() if not meth.startswith("__")})

    def __getattr__(self,_attr):
        return self.bindings.get(_attr)

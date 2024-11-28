class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
    def __str__(self):
        return "AnyClass: " + ', '.join([f"{key}={repr(self.__dict__[key])}" for key in self.__dict__])

    def __repr__(self):
        return "AnyClass(" + ', '.join([f"{key}={repr(self.__dict__[key])}" for key in self.__dict__]) + ')'


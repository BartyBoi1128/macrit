from abc import ABCMeta, abstractstaticmethod

class IWarning(metaclass=ABCMeta):

    @abstractstaticmethod
    def __init__(self) -> None:
        pass

    @abstractstaticmethod
    def warningMessage():
        return("This is the default warning message")

class vegetarianWarning(IWarning):
    
    def __init__(self) -> None:
        self.type = "vegetarian"
        self.message = "Warning: This recipe contains meat."
    
    def warningMessage(self):
        return(self.message)

class glutenWarning(IWarning):
    
    def __init__(self) -> None:
        self.type = "gluten"
        self.message = "Warning: This recipe contains gluten."

    def warningMessage(self):
        return(self.message)

class IMacrosWarning(metaclass=ABCMeta):

    @abstractstaticmethod
    def __init__(self) -> None:
        pass

    @abstractstaticmethod
    def warningMessage():
        pass

class macrosWarning(IMacrosWarning):

    def __init__(self):
        self.type = ""

    def setType(self, inType):
        self.type = inType

    def warningMessage(self):
        return("Warning: This recipe will send you over your daily recommended %s intake." % self.type)

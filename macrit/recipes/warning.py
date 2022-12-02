from abc import ABCMeta, abstractstaticmethod

#Default Warning
class IWarning(metaclass=ABCMeta):

    @abstractstaticmethod
    def __init__(self) -> None:
        pass

    @abstractstaticmethod
    def warningMessage():
        return("This is the default warning message")

#Warning for if the user is a vegetarian
class vegetarianWarning(IWarning):
    
    def __init__(self) -> None:
        self.type = "vegetarian"
        self.message = "Warning: This recipe contains meat."
    
    def warningMessage(self):
        return(self.message)

#Warning for if the user has gluten allergies
class glutenWarning(IWarning):
    
    def __init__(self) -> None:
        self.type = "gluten"
        self.message = "Warning: This recipe contains gluten."

    def warningMessage(self):
        return(self.message)

#Warning for the macros
class IMacrosWarning(metaclass=ABCMeta):

    @abstractstaticmethod
    def __init__(self) -> None:
        pass

    @abstractstaticmethod
    def warningMessage():
        pass


#Warning for if the user is going to go over the daily reccomended intake
class macrosWarning(IMacrosWarning):

    def __init__(self):
        self.type = ""

    def setType(self, inType):
        self.type = inType

    def warningMessage(self):
        return("Warning: This recipe will send you over your daily recommended %s intake." % self.type)

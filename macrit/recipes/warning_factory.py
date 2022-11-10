from warning import glutenWarning, vegetarianWarning, macrosWarning

class warning_factory:

    @staticmethod
    def buildWarning(warningType):
        macroTypes = ["calorie", "protein", "carbohydrate", "fat", "sugar", "fibre", "salt"]
        if warningType == "gluten":
            return glutenWarning()
        elif warningType == "vegetarian":
            return vegetarianWarning()
        elif warningType in macroTypes:
            warning = macrosWarning()
            warning.setType(warningType)
            return warning
        else:
            return -1

print(warning_factory.buildWarning("gluten").warningMessage())
from uagents import Model

# define a data model class named 'TemperatureData' that inherits from 'Model'
class TemperatureData(Model):

    # to represent temperature-related data with attributes for 'city' (a string) and 'temperature' (a float).
    city: str
    temperature: float

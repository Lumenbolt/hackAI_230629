#Importing Required Modules and Classes
from uagents import Bureau, Agent
from agents.temperature_alert import TemperatureAlert
from agents.terminal_interface import TerminalInterface
from messages.temperature_data import TemperatureData

def main():
    #ask the user for inputs : API Key, location, minimum temperature, and maximum temperature thresholds
    apikey = input("Enter your OpenWeather API key (mandatory): ")
    location = input("Enter the city to fetch weather data (blank for Delhi): ") or 'Delhi'
    minimum_temp = float(input("Enter the minimum temperature threshold (in Celsius): "))
    maximum_temp = float(input("Enter the maximum temperature threshold (in Celsius): "))

    # set up the TemperatureAlert agent and create a TerminalInterface for easy interaction
    temperature_alert = TemperatureAlert(apikey)
    terminal_interface = TerminalInterface()

    #create different agents for different tasks: TemperatureAlert, notifications for min and max thresholds, and a CLI agent
    temperature_alert_agent = Agent(name="temp", seed="temp")
    minimum_threshold_notify_agent = Agent(name="minthres", seed="minthres")
    maximum_threshold_notify_agent = Agent(name="maxthres", seed="maxthres")
    temperature_correct_notify_agent = Agent(name="cli", seed="cli")

    #define a function to periodically fetch weather data and send notifications
    @temperature_alert_agent.on_interval(period=1.0)
    async def fetch_weather(ctx):
        # getting the latest temperature data for the chosen location
        data = temperature_alert.fetch_temperature_data(location)

        #check if the temperature falls below or exceeds your set thresholds, and send notifications accordingly
        if data.temperature < minimum_temp:
            await ctx.send(minimum_threshold_notify_agent.address, data)
        elif data.temperature > maximum_temp:
            await ctx.send(maximum_threshold_notify_agent.address, data)
        else:
            await ctx.send(temperature_correct_notify_agent.address, data)

    #handle messages received by the notification agents and print temperature information
    @minimum_threshold_notify_agent.on_message(TemperatureData)
    async def print_weather(ctx, sender, msg):
        terminal_interface.print_temperature_under(msg, minimum_temp)

    @maximum_threshold_notify_agent.on_message(TemperatureData)
    async def print_weather(ctx, sender, msg):
        terminal_interface.print_temperature_over(msg, maximum_temp)

    @temperature_correct_notify_agent.on_message(TemperatureData)
    async def print_weather(ctx, sender, msg):
        terminal_interface.print_temperature_correct(msg)

    #create a Bureau to manage and run our agents
    bureau = Bureau()
    bureau.add(temperature_alert_agent)
    bureau.add(minimum_threshold_notify_agent)
    bureau.add(maximum_threshold_notify_agent)
    bureau.add(temperature_correct_notify_agent)
    bureau.run()

# This line ensures that the 'main' function is executed only when this script is run as the main program, rather than when it's imported as a module into another script.
if __name__ == '__main__':
    main()

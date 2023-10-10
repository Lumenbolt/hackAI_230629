from uagents import Bureau, Agent
from agents.temperature_alert import TemperatureAlert
from agents.terminal_interface import TerminalInterface
from messages.temperature_data import TemperatureData

def main():
    location = input("Enter the city to fetch weather data (blank for delhi): ") or 'delhi'
    minimum_temp = float(input("Enter the minimum temperature threshold (in Celsius): "))
    maximum_temp = float(input("Enter the maximum temperature threshold (in Celsius): "))

    temperature_alert = TemperatureAlert('b5ee09875753cc27f23fa008321ba336')
    terminal_interface = TerminalInterface()

    temperature_alert_agent = Agent(name="temp", seed="temp")
    minimum_threshold_notify_agent = Agent(name="minthres", seed="minthres")
    maximum_threshold_notify_agent = Agent(name="maxthres", seed="maxthres")
    temperature_correct_notify_agent = Agent(name="cli", seed="cli")

    @temperature_alert_agent.on_interval(period=1.0)
    async def fetch_weather(ctx):
        data = temperature_alert.fetch_temperature_data(location)
        if data.temperature < minimum_temp:
            await ctx.send(minimum_threshold_notify_agent.address, data)
        elif data.temperature > maximum_temp:
            await ctx.send(maximum_threshold_notify_agent.address, data)
        else:
            await ctx.send(temperature_correct_notify_agent.address, data)

    @minimum_threshold_notify_agent.on_message(TemperatureData)
    async def print_weather(ctx, sender, msg):
        terminal_interface.print_temperature_under(msg, minimum_temp)

    @maximum_threshold_notify_agent.on_message(TemperatureData)
    async def print_weather(ctx, sender, msg):
        terminal_interface.print_temperature_over(msg, maximum_temp)

    @temperature_correct_notify_agent.on_message(TemperatureData)
    async def print_weather(ctx, sender, msg):
        terminal_interface.print_temperature_correct(msg)

    bureau = Bureau()
    bureau.add(temperature_alert_agent)
    bureau.add(minimum_threshold_notify_agent)
    bureau.add(maximum_threshold_notify_agent)
    bureau.add(temperature_correct_notify_agent)
    bureau.run()

if __name__ == '__main__':
    main()

RED = '\033[91m'
GREEN = '\033[92m'
END = '\033[0m'

class TerminalInterface:
    def print_temperature_correct(self, data):
        print(GREEN, f'The temperature in {data.city} is {data.temperature}°C. Looks just fine!', END)

    def print_temperature_under(self, data, min):
        print(RED, f'The temperature in {data.city} is {data.temperature}°C. It is under {min}°C! Keep warm!', END)
    
    def print_temperature_over(self, data, max):
        print(RED, f'The temperature in {data.city} is {data.temperature}°C. It is over {max}°C! Keep cool!', END)
            
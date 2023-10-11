# ANSI escape codes for text color in the terminal
RED = '\033[91m'
GREEN = '\033[92m'
END = '\033[0m'

# The 'TerminalInterface' class provides methods to display temperature-related messages with colorful text in the terminal
class TerminalInterface:
     # to print a message when the temperature is within the desired range
    def print_temperature_correct(self, data):

        # print a message in green text, mentioning the city, current temperature, and that it's comfortably within the desired range
        print(GREEN, f'The temperature in {data.city} is {data.temperature}°C. Looks just fine!', END)

    # to print a message when the temperature falls below the specified minimum threshold
    def print_temperature_under(self, data, min):

        # print a message in red text, including the city, current temperature, and a reminder to stay warm as it's below the minimum threshold
        print(RED, f'The temperature in {data.city} is {data.temperature}°C. It is under {min}°C! Keep warm!', END)
    
    # to print a message when the temperature exceeds the specified maximum threshold
    def print_temperature_over(self, data, max):

        # print a message in red text, indicating the city, current temperature, and a suggestion to stay cool as it's above the maximum threshold
        print(RED, f'The temperature in {data.city} is {data.temperature}°C. It is over {max}°C! Keep cool!', END)
            
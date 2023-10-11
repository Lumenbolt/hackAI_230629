# Temperature Alert Agent

## DESCRIPTION
This Python program uses the uAgents library to connect to a weather API, fetch the real-time temperature for a specified location, and send an alert to the user when the temperature goes below or above a specified threshold.
This tool is designed to help users stay informed about temperature conditions in their desired location and take appropriate actions.

### Key Features
#### Real-Time Weather Data 
 The Temperature Alert Agent is your gateway to real-time weather information, thanks to its integration with the OpenWeather API. This means you'll always have the most accurate and current temperature data at your fingertips. Whether you're planning an outdoor adventure or just curious about the weather, this tool ensures you stay informed.

#### User-Defined Thresholds
We understand that your temperature preferences may vary. That's why the Temperature Alert Agent empowers you with the ability to set your own temperature range. Whether you prefer a cozy warmth or a refreshing coolness, you can specify both minimum and maximum temperature thresholds. No more generic alerts—receive notifications only when temperature conditions align with your unique criteria.

#### Alert Notifications
 The program sends alert notifications to users when the temperature crosses their set thresholds. These notifications are designed to be informative and provide quick updates on the weather. With your personalized temperature thresholds in experience, from setting your preferences to receiving alerts. The program's simplicity and customization options ensure that it caters to your specific needs and preferences.

#### Terminal Interaction
 A user-friendly terminal interface ensures easy interaction with the program. The use of colored text (green for normal messages and red for alerts) adds a visual dimension to the information displayed.


## Instructions to Run the Project
To run this program, you will need to install the uAgents library. You can do this by running the following command in a terminal:
### Prerequisites
Python installed on your system.

### Installation 
1. Clone or download this repository to your local machine.
2. Navigate to the project directory in your terminal.

### Install Required Libraries
You need to install the uAgents library to run the Temperature Alert Agent. You can do this by running the following command in your terminal:

"
pip install uagents
"
### Running the Program
Now, you can run the Temperature Alert Agent by following these steps:

In your terminal, navigate to the project directory where temperature_alert_agent.py is located.
Run the program with the following command:
"
python temperature_alert_agent.py
"
The program will start monitoring the temperature for the specified location. If the temperature falls below or rises above the specified thresholds, the program will send alerts to keep you informed.

## Special Considerations

1. The program uses ANSI escape codes for colored text in the terminal (red for alerts and green for normal messages). Ensure that your terminal supports these escape codes for accurate display.
2. Please configure your minimum and maximum temperature thresholds based on your preferences and requirements.


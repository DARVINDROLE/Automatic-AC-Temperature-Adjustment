# Automatic-AC-Temperature-Adjustment
The provided Python script automatically adjusts the target temperature for an air conditioning unit based on current weather conditions obtained from the OpenWeatherMap API. It calculates a target temperature using a simple formula and adjusts it based on the room temperature.

Components Used:
Python: Scripting language used for coding.
datetime: Module used to handle date and time operations.
requests: Module used to send HTTP requests to the OpenWeatherMap API and receive responses.
time: Module used to handle time-related operations like sleeping for specified intervals.
Functions Defined:
kelvin_to_celsius(kel):

Converts temperature from Kelvin to Celsius.
Formula: Celsius = Kelvin - 273.15.
AC_TEMP(temp_celsius, humidity):

Calculates the target AC temperature based on the current room temperature (in Celsius) and humidity.
Uses a conditional formula to determine the target temperature:
If the room temperature (temp_celsius) is less than or equal to 15°C, it uses a specific formula.
Otherwise, it uses another formula.
Returns the calculated target temperature.
Constants and Variables:
BASE_URL: Base URL for the OpenWeatherMap API.
API_KEY: API key for authentication with the OpenWeatherMap API.
CITY: Specifies the city for which weather data is requested (e.g., "Mumbai").
url: Combines BASE_URL, API_KEY, and CITY to form the complete URL for API requests.
current_hour: Retrieves the current hour from the local time using time.localtime().tm_min.
Main Loop:
While True Loop:
Outer While Loop: Runs continuously.
First Inner While Loop: Executes once.
Sends a request to the OpenWeatherMap API and retrieves weather data for the specified city (CITY).
Converts the temperature from Kelvin to Celsius using kelvin_to_celsius().
Retrieves humidity data from the API response.
Calculates the initial target AC temperature using AC_TEMP().
Prints the initial target AC temperature.
Sleeps for 1800 seconds (30 minutes) before proceeding to the next step.
Second Inner While Loop: Executes three times.
Adjusts the target AC temperature based on the room temperature (temp_celsius).
If temp_celsius is greater than 15°C, increments ac_temp by 1; otherwise, decrements it by 1.
Prints the adjusted AC temperature.
Sleeps for 480 seconds (8 minutes) before looping again.
Usage:
Ensure Python is installed on your system.
Install necessary libraries (requests).
Replace API_KEY with your own OpenWeatherMap API key.
Adjust CITY as needed for your location.
Run the script and observe the console output for the calculated AC temperatures.
Considerations:
Ensure stable internet connectivity for consistent API requests.
Handle API rate limits if making frequent requests.
Adjust sleep times (time.sleep()) as per your specific requirements and comfort preferences.
Verify and adjust the formulas in AC_TEMP() based on actual comfort and energy-saving considerations.
Improvement Suggestions:
Implement error handling for API requests (requests.exceptions.RequestException) to handle connection issues gracefully.
Enhance temperature adjustment logic based on more sophisticated algorithms or machine learning models for better comfort optimization.

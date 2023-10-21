import requests
import collections

Location = collections.namedtuple('Location', 'city country')


def main():

    print("-------------------------")
    print("WEATHER CLIENT APP".center(25, " "))
    print("-------------------------")

    # input location
    location = input("Enter your location(e.g Portland, OR, US)? ")

    # split information from input
    loc = location_splitter(location)

    # get weather information via API
    weather_api(loc.city)

    # show weather information


def weather_api(city_name):
    api_key = open('api_key', 'r').read()
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    response = requests.get(base_url)
    data = response.json()

    if data["cod"] == 200:
        # Weather data is in data["main"], data["weather"], and so on.

        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]     # convert to celsius or fahrenheit
        temp = temp_converter(temp)
        cloud = data["weather"][0]["main"]

        show_weather(city, country, temp, cloud)
    else:
        print("City not found")


def temp_converter(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit


def location_splitter(location):
    # check if the arguments are empty string or will be empty string
    if not location or not location.strip():
        return None

    # create default value
    city = ""
    country = ""

    location = location.lower().strip()
    parts = location.split(",")

    if len(parts) == 1:
        city = parts[0].strip()
    elif len(parts) == 2:
        city = parts[0].strip()
        country = parts[1].strip()
    else:
        return None

    # store stripped result in Location tuple
    return Location(city, country)


def show_weather(city, country, temp, cloud):
    print(f"The weather in {city}, {country} is {temp:.2f} F and Clouds: {cloud}.")


if __name__ == '__main__':
    main()

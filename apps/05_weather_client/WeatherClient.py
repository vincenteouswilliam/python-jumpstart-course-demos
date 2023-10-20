from bs4 import BeautifulSoup
import requests
import collections

Location = collections.namedtuple('Location', 'city state')


def main():

    print("-------------------------")
    print("WEATHER CLIENT APP".center(25, " "))
    print("-------------------------")

    # input location
    location = input("Enter your location(e.g Portland, OR, US): ")

    # split information from input
    loc = location_splitter(location)

    print(loc.city)

    access_weather_web(loc)

    # access the weather web

    # if "," in location:
    #     location_list = location.split(", ")
    #     city, nation = location_list
    #
    # print(city)
    # print(nation)

    # call_weather(location)


def location_splitter(location):
    # check if the arguments are empty string or will be empty string
    if not location or not location.strip():
        return None

    # create
    city = ""
    state = ""

    location = location.lower().strip()
    parts = location.split(",")

    if len(parts) == 1:
        city = parts[0].strip()
    elif len(parts) == 2:
        city = parts[0].strip()
        state = parts[1].strip()
    else:
        return None

    # print(f"city: {city}, state: {state}}")

    # store stripped result in Location tuple
    return Location(city, state)


def access_weather_web(loc: Location):
    # get base URL
    base_URL = f"https://www.wunderground.com/weather/{loc.state}/{loc.city}"
    page = requests.get(base_URL)

    soup = BeautifulSoup(page.content, "html.parser")

    # get the parent div that contains the information needed.
    current_condition = soup.find("div", class_="city-conditions")

    temp = current_condition.find("span", class_="wu-value")

    div_parent = current_condition.find_all('div', class_='conditions-extra')
    for div in div_parent:
        p_element = div.find("p")
        if p_element:
            condition = p_element.get_text()

    print(temp.text.strip())
    print(condition)

    print(f"The weather in {loc.city}, {loc.state} is {temp.text.strip()} F and Clouds:{condition}.")



if __name__ == '__main__':
    main()
from bs4 import BeautifulSoup
import requests

def main():

    print("-------------------------")
    print("WEATHER CLIENT APP".center(25, " "))
    print("-------------------------")

    # input location
    location = input("Enter your location(e.g Portland, OR, US): ")

    call_weather(location)
def call_weather(location):
    # get weather url
    base_URL = f"https://www.wunderground.com/weather/id/{location}"  #TODO: change id to nation_code later
    page = requests.get(base_URL)

    soup = BeautifulSoup(page.content, "html.parser")

    # get the parent div that contains the information needed.
    current_condition = soup.find("div", class_="city-conditions")

    city = soup.find_all("div", class_="city-header")
    temp = current_condition.find("span", class_="wu-value")

    # print(city[0].text.strip())
    # print(temp.text.strip())

    print(f"The weather in {location}, NATION is {temp.text.strip()} F and Clouds:CLOUDS.")


if __name__ == '__main__':
    main()
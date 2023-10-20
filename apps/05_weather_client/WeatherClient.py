from bs4 import BeautifulSoup
import requests

def main():
    print("-------------------------")
    print("WEATHER CLIENT APP".center(25, " "))
    print("-------------------------")

    # input location
    location = input("Enter your location(e.g Portland, OR, US): ")

    print("The weather in {location}, {nation} is {temp} F and Clouds:{clouds}.")

if __name__ == '__main__':
    main()
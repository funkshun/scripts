import urllib.request as urllib2
import forecastio
def main():
    api_key = "ceada1a781acce456e74810577e8ddbb"
    lat = 35.9132
    lng = -79.0558

    if network_up():
        weather = forecastio.load_forecast(api_key, lat, lng).currently()
        print(weather.summary + ", " + str(weather.temperature) + "F, " + str(weather.precipProbability) + "% Chance")
    else:
        print("Network Unavailable")
def network_up():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err:
        return False

if __name__ == "__main__":
    main()

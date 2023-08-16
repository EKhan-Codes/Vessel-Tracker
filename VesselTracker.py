import requests
from bs4 import BeautifulSoup
import folium


MMSI = input("Enter MMSI For Vessle Track:")
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'}

# URL of the ship you want to track, execute the request and parse it to the variable 'soup'
url = 'https://www.myshiptracking.com/vessels/mmsi-' + MMSI
reqs = requests.get(url, headers=headers)
soup = BeautifulSoup(reqs.content, 'html.parser')
s = soup.find('table', class_='table table-sm table-borderless my-0 w-50 w-sm-75')
content = s.find_all('td') # type: ignore
scraped_text = ' '.join(element.get_text() for element in content)

def Convert(string):
    li = list(string.split(" "))
    return li

str1 = scraped_text
print("Longitude:"+ " " + Convert(str1)[0])
print("Latitude:"+ " " + Convert(str1)[1])
print("Position Received:"+ Convert(str1)[13] + Convert(str1)[14] + " " + Convert(str1)[15])
Lon = Convert(str1)[0]
Lat = Convert(str1)[1]
Lon1 = Lon
Lat2 = Lat
Longitude = Lon1.replace("°", "")
Latitude = Lat2.replace("°", "")

my_map3 = folium.Map(location = [Latitude, Longitude],
                                        zoom_start = 15)
 
# Pass a string in popup parameter
folium.Marker([Latitude, Longitude],
               popup = ' Vessle').add_to(my_map3)
 
 
my_map3.save(" my_map4.html ")


 
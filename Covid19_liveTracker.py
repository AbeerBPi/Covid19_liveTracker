import requests
import bs4
import logging
import os

#country_name=input("Enter the Country name: ")
country_name="USA"

os.remove("message.txt")
f = open("message.txt", "a+")

def covid19(country):
    res = requests.get("https://www.worldometers.info/coronavirus/#countries")
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    index = -1
    data=soup.select('tr td')
    for i in range(len(data)):
        if data[i].text.lower()==country.lower():
            index=i
            break
    
    for i in range(7):
        if i == 0:
            print("\nCountry name: "+str(data[i+index].text))
            f.write("\nCountry name: "str(data[i+index].text))
        elif i == 1:
            print("Total cases: "+str(data[i+index].text))
            f.write("Total cases: "+str(data[i+index].text))
        elif i == 2:
            if data[i+index].text == '':
                f.write("New cases: 0")
                print("New cases: 0")
            else:
                f.write("New cases: "+str(data[i+index].text))
                print("New cases: "+str(data[i+index].text))
        elif i == 3:
            f.write("Total deaths: "+str(data[i+index].text))
            print("Total deaths: "+str(data[i+index].text))
        elif i == 4:
            if data[i+index].text == '':
                print("New deaths: 0")
                f.write("New deaths: 0")
            else:
                f.write("New deaths: "+str(data[i+index].text))
                print("New deaths: "+str(data[i+index].text))
        elif i == 5:
            f.write("Total Recovered: "+str(data[i+index].text))
            print("Total Recovered: "+str(data[i+index].text))
        elif i == 6:
            f.write("Active cases: "+str(data[i+index].text),end='\n\n')
            print("Active cases: "+str(data[i+index].text),end='\n\n')
        return "c"
    
covid19(country_name)
f.close()


#except Exception as e:
 #   logger.error

import requests
from typing import List,Dict


def get_temperature(city:str)->int:
    #restrected to 250 api req in a month
    #set params : apikey and city to check
    params = {
    'access_key': '663837148af3080348b77bffa067c1e0',
    'query': city
    }

    api_result = requests.get('http://api.weatherstack.com/current', params)

    api_response = api_result.json()
    return api_response['current']['temperature']

def return_tuple_MinMax(dict:Dict)->None:

    max_city = max(dict,key=dict.get)
    min_city = min(dict,key=dict.get)
    return ((max_city,dict[max_city]),(min_city,dict[min_city]))

def main(citys:List)-> tuple:
    temperature_dict = {}
    for city in citys:
        temperature = get_temperature(city)
        temperature_dict[city] = temperature
    return return_tuple_MinMax(temperature_dict)

if __name__ == '__main__':
    citys = ['New York','London','Haifa']
    print(main(citys=citys))
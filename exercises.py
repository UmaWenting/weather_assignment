import json
import csv
stats = {}

with open('stations.csv') as file:
    stations = list(csv.DictReader(file))

with open('precipitation.json', 'r+', encoding='utf-8') as file:
    precipitation_data = json.load(file)

for station in stations:
    station_data = []
    for key in precipitation_data:
        if key['station'] == station['Station']:
            station_data.append(key)

    monthly_precipitation = {}
    for measurement in station_data:
        date = measurement['date']  
        month = date.split('-')[1]
        precipitation = measurement['value']  
        if month in monthly_precipitation:
            monthly_precipitation[month] += precipitation
        else:
            monthly_precipitation[month] = precipitation

    total_monthly_precipitation = list(monthly_precipitation.values())
    total_yearly_precipitation = sum(total_monthly_precipitation)

    relative_monthly_precipitation = {}
    total_yearly_precipitation = sum(monthly_precipitation.values())

    date = key['date']  
    month = date.split('-')[1]
    percentation = key['value']  
    for month, precipitation in monthly_precipitation.items():
        percentage = ( int((precipitation)) / int(total_yearly_precipitation)) * 100
        relative_monthly_precipitation[month] = percentage


    for month, percentage in relative_monthly_precipitation.items():


        stats[station['Location']] = {
        'monthly_precipitation': monthly_precipitation,
        'total_yearly_precipitation': total_yearly_precipitation,
        'relative_montly_precipitation': relative_monthly_precipitation
        }

with open ('results.json', 'w') as file:
    json.dump(stats, file, indent=4,)
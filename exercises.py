import json

with open('precipitation.json', 'r+', encoding='utf-8') as file:
    precipitation_data = json.load(file)

seattle=[]
for key in precipitation_data:
    if key['station']== 'GHCND:US1WAKG0038':
        seattle.append(key)
# print(seattle)

monthly_precipitation = {}
for key in seattle:
    date = key['date']  
    month = date.split('-')[1]
    precipitation = key['value']  
    if month in monthly_precipitation:
        monthly_precipitation[month] += precipitation
    else:
        monthly_precipitation[month] = precipitation

total_monthly_precipitation = list(monthly_precipitation.values())
total_yearly_precipitation = sum(total_monthly_precipitation)

stats = {
    'monthly_precipitation': monthly_precipitation,
    'total_yearly_precipitation': total_yearly_precipitation,
    }

with open ('results.json', 'w') as file:
    json.dump(stats, file, indent=4,)
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
print(f"Total Monthly Precipitation List for Seattle: {total_monthly_precipitation}")

total_yearly_precipitation = sum(total_monthly_precipitation)
print(f"Total Yearly Precipitation List for Seattle: {total_yearly_precipitation}")
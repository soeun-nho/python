import pandas as pd

weather_data = pd.read_csv('csvfiles/weather.csv', encoding='utf-8')

print(weather_data)
print(type(weather_data))

#첫행 _ 키값 다시 제대로 받아와야할 듯?
weather_data['최저기온(℃)'].replace(-999, 999, inplace=True)
weather_data['최고기온(℃)'].replace(999,-999, inplace=True)

coldest_data= weather_data.loc[weather_data['최저기온(℃)'].idxmin()]
hottest_data=weather_data.loc[weather_data['최고기온(℃)'].idxmax()]

coldest_date = coldest_data['날짜']
hottest_date = hottest_data['날짜']

coldest_temp=coldest_data['최저기온(℃)']
hottest_temp = hottest_data['최고기온(℃)']

print(f"1980년 이후로 {coldest_date}일이 {coldest_temp}도로 가장 추웠다.")
print(f"1980년 이후 {hottest_date} 일이 {hottest_temp}로 가장 추웠다.")



import pandas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
data = pandas.read_csv("database.csv")
crop = pandas.read_csv("crop.csv")
city = data['city'].to_list()
max_temp = list(map(int, data['max temperature'].to_list()))
min_temp = list(map(int, data['min temperature'].to_list()))
max_humid = list(map(int, data['max humidity'].to_list()))
min_humid = list(map(int, data['min humidity'].to_list()))
min_ph = list(map(int, data['min ph'].to_list()))
max_ph = list(map(int, data['max ph'].to_list()))
wheat_humidity = 80.5
wheat_ph = 9
avg_humi = {}
avg_humidity = []
avg_tempa = {}
avg_temp = []
for i in range(len(data)):
    avg_tempa[city[i]] = (max_temp[i]+min_temp[i])/2
    avg_temp.append((max_temp[i]+min_temp[i])/2)
for i in range(27):
    avg_humi[city[i]] = (max_humid[i]+min_humid[i])/2
    avg_humidity.append((max_humid[i]+min_humid[i])/2)
avg_phs = {}
avg_ph = []
for i in range(27):
    avg_phs[city[i]] = (max_ph[i]+min_ph[i])/2
    avg_ph.append((max_ph[i]+min_ph[i])/2)
datafram = {'city': city, 'temp': avg_temp, 'ph': avg_ph, 'humidity': avg_humidity}
new = pd.DataFrame(datafram)
columns = list(new.head())[1:len(list(new.head()))]
clf = DecisionTreeClassifier()
target = 'crop'
clf.fit(crop[columns], crop[target])
predictions = clf.predict(new[columns])
final = pd.DataFrame({'City': city, 'Temperature': avg_temp, 'pH': avg_ph, 'Humidity': avg_humidity, 'Crop': predictions})
data['avg humidity'] = avg_humidity
data['avg_temp'] = avg_temp
data['avg ph'] = avg_ph
name = input("Enter the name of the city:").lower()
if name not in city:
    print("City Not Found....")
else:
    print("City Crop Predicted Data")
    plot_data = final[final['City'] == name]
    print(plot_data)
    crops=list(plot_data['Crop'])
    crop_data=crop[crop['crop']==crops[0]]
    print("Crop Data")
    print(crop_data)
    crop_cols=['temp','ph','humidity']
    plot_columns = list(plot_data.head())[1:len(list(plot_data.head()))-1]
    plot_array = []
    for i in list(final.head())[1:len(list(final.head()))-1]:
        plot_array.append(np.array(final[i]))
    for i in range(len(plot_array)):
        dt=pd.DataFrame({'City':city,name+"\'s "+plot_columns[i]:float(plot_data[plot_columns[i]]),plot_columns[i]:final[plot_columns[i]],crops[0]+'\'s '+plot_columns[i]:float(crop_data[crop_cols[i]])})
        dt.plot()
        plt.xlabel("City")
        plt.ylabel(plot_columns[i])
        plt.show()
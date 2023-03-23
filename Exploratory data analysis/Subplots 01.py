import matplotlib.pyplot as plt
from matplotlib import style

#define temp, wind, humidity, precipitation data and Time hrs data
temp_data = [79, 75, 74, 73, 81, 77, 81, 95, 93, 95]
wind_data = [14, 12, 10, 13, 9, 13, 12, 13, 17, 13]
time_hrs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
humidity_data = [73, 76, 78, 81, 81, 84, 84, 79, 71, 64]
precipitation_data = [26, 42, 69, 48, 11 ,16, 5, 11, 3, 48]

#draw subplots for (1,2,1) ans (1,2,2)
plt.figure(figsize=(8,4))
plt.subplots_adjust(hspace=.25)
plt.subplot(1,2,1)
plt.title('Temp')
plt.plot(time_hrs, temp_data, color = 'b', linestyle = '-', linewidth = 1)
plt.subplot(1,2,2)
plt.title('Wind')
plt.plot(time_hrs, wind_data, color = 'r', linestyle = '-', linewidth = 1)

#draw subplots for (2,1,1) and (2,1,2)
plt.figure(figsize = (6,6))
plt.subplots_adjust(hspace=.25)
plt.subplot(2,1,1)
plt.title('Humidity')
plt.plot(time_hrs, humidity_data, color = 'b', linestyle ='-', linewidth = 1)
plt.subplot(2,1,2)
plt.title('Precipitation')
plt.plot(time_hrs, precipitation_data, color = 'r', linestyle = '-', linewidth = 1)
plt.show()

#draw subplots for (2,2,1), (2,2,2), (2,2,3) and (2,2,4)
plt.figure(figsize=(9,9))
plt.subplots_adjust(hspace=.3)
plt.subplot(2,2,1)
plt.title('Temp (F)')
plt.plot(time_hrs, temp_data, color = 'b', linestyle ='-', linewidth = 1)
plt.subplot(2,2,2)
plt.title('Wind (MPH)')
plt.plot(time_hrs, wind_data, color = 'r', linestyle ='-', linewidth = 1)
plt.subplot(2,2,3)
plt.title('Humidity (%)')
plt.plot(time_hrs, humidity_data, color = 'g', linestyle ='-', linewidth = 1)
plt.subplot(2,2,4)
plt.title('Precipitation (%)')
plt.plot(time_hrs, precipitation_data, color = 'y', linestyle ='-', linewidth = 1)
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

#load flights data from sns dataset (buit in)
flight_data = sns.load_dataset('flights')
#view top 5 records
print('Top 5 records are: \n', flight_data.head())

#use pivot method to re-arrange the dataset
flight_data = flight_data.pivot('month', 'year', 'passengers')
#view the dataset
print('Flight data (after pivot): \n', flight_data)

#use heatmap method to generate the heatmap of the flights data
sns.heatmap(flight_data)
plt.show()

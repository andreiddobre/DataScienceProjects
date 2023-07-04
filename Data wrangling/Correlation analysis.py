#pip install pandas
#pip install seaborn
#pip install matplotlib

import pandas as pd, seaborn as sns, matplotlib.pyplot as plt

#Phase 1: Explore and examin the correlation between variables
#reading the .csv file
df = pd.readf = pd.read_csv('middle_tn_schools.csv')

#"describe" each variable or column in the dataset
print('Dataset described: \n', df.describe())

#data types of the variables
print('The data types in the dataset are: \n', df.dtypes)

#check for and clean missing values
print('Checking for na datas: \n', df.isna().any())

#which rows have missing data
null_data = df[df.isnull().any(axis=1)]
print('Rows with missing data: \n', null_data)

#define the columns we wish to replace values in
cols = ["state_percentile_15", "avg_score_15"]
df[cols]=df[cols].fillna(df.mean())

#check to see if there are any more missing / NaN values
print('Verify if are there any missing values anymore: \n', df.isna().any())

#verify if 'school_type' it's worth keeping or dropping
print('Check if school type is relevant data \n', df['school_type'].describe())

#list the unique values for school type
print('Unique school types: \n', df['school_type'].unique())


#Phase 2: Begin to explore the correlation
#dropping the non-integer columns
df2_sm = df.drop(['name','school_type'], axis=1)
print('Simplified data head \n', df2_sm.head())

#finding the correlation of each column in the DataFrame
df_corr = df2_sm.corr()
print('Correlated data \n', df_corr.head())

#pivot data grouped by school_rating
print('Pivout grouped by school_rating \n', df[['reduced_lunch', 'school_rating']].groupby(['school_rating']).describe().unstack())
#finding the correlation of each column in the DataFrame
print('Correlated sorted data \n', df[['reduced_lunch', 'school_rating']].corr())


#Phase 3: Visualization
#heatmap
sns.heatmap(df_corr, linewidths=0.1, cmap = 'copper', annot_kws={'fontsize': 7, 'fontweight': 'normal', 'fontfamily': 'verdana'}, annot=True, square=True)
sns.set(font_scale = 2)
plt.title("Correlated data [Copper]")
plt.gcf().set_size_inches(9, 6)

#Bivariate KDE plot
fig, ax = plt.subplots(1, figsize=(12,6))
sns.set(font_scale = 1)
plt.title("KDE data [winter_r]")
t = sns.kdeplot(df, x='reduced_lunch', y='school_rating', cmap='winter_r', cbar=True, clip=(-1,300), fill=True, alpha=.8)
plt.scatter(df.reduced_lunch, df.school_rating, sizes=(40, 200), marker="o", alpha=.5, color='orangered')
plt.show()

import matplotlib.pyplot as plt


#Data from Ohio state, leading causes of death in the state from year 2012
#cause of deaths
cause = 'Chronic Diseases', 'Unintentionat Injuries', 'Alzheimer', 'Infuenza and Pneumonia', 'Sepsis', 'Others'
#percentile
percentile = [62,5,4,2,1,26]

#set the pie chart plot properties
#set figure size
plt.figure(figsize=(10,10))
#explode the largest pie in the data set
explode = (0.05, 0, 0, 0, 0, 0)
#set pie chart properties
plt.pie(percentile, labels=cause, explode=explode, autopct='%1.1f%%', startangle=70)
#set axis equal to draw pie as circle
plt.axis('equal')
#set title of the pie chart
plt.title('Ohio State - 2012: Leading causes of death')
#show the plot (pie chart)
plt.show()

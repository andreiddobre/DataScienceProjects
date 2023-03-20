import matplotlib.pyplot as plt

#job data in percentile
job_data = ['40', '20', '17', '8', '5', '10']

#define label as different departments
labels = 'IT', 'Finance', 'Marketing', 'Admin', 'HR', 'Operations'

#explode the 1st slice which is IT
explode = (0.05, 0, 0, 0, 0, 0)

#draw the pie chart and set the parameters
plt.pie(job_data, labels=labels, explode=explode)

#show the plot
plt.show()

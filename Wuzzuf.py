# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 17:22:27 2021

@author: hp
"""
# to read data and displaying it

import pandas as pd
dataset=pd.read_csv("Wuzzuf_jobs.csv")
dataset.describe()
dataset

# to clean dublicated and null values

# a): sorting by title
dataset.sort_values("Title", inplace = True)

#  b): dropping ALL duplicated values

dataset.drop_duplicates(subset ="Title",
                       keep = False , inplace = True)
# to remove rows dublicated
dataset.drop_duplicates()	

# c): clean null values

dataset.dropna()

# another way to drop the rows where all elements are missing 
dataset.dropna(how='all')

# there are no nulls value in the dataset

dataset['Level'].isnull()
print (dataset['Level'].isnull())
 
# to count jobs for each company and displaying it in order 

jobs=dataset['Title'].value_counts()

# sorting company
dataset.sort_values("Title", inplace = True)


# 4,5

# pie chart
import matplotlib.pyplot as plt
plt.pie(jobs)  
plt.show() 

# pie chat for companies
import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('Wuzzuf_Jobs.csv')

x=dataset['Company'].value_counts()
plt.pie(x)
plt.show() 
print ('the most demanding companies for jobs are', x.index[0:5] )


#import numpy as np
import matplotlib.pyplot as plt

#6,7



import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('Wuzzuf_Jobs.csv')

z=dataset['Title'].value_counts()
print ('the Most popular jobs title are', z.index[0:5] )
fig = plt.figure(figsize = (10, 5))
plt.bar(z.index[0:5], z[0:5], color ='maroon',
		width = 0.4)

plt.xlabel("Most popular jobs title")
plt.ylabel("Number of popular jobs title")
plt.title("Popular jobs title")
plt.show()


#8.9


import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('Wuzzuf_Jobs.csv')

y=dataset['Location'].value_counts()
print ('the Most popular areas are', y.index[0:5] )
fig = plt.figure(figsize = (10, 5))
plt.bar(y.index[0:5], y[0:5], color ='maroon',
		width = 0.4)

plt.xlabel("Most popular areas")
plt.ylabel("Number of popular areas")
plt.title("Popular areas")
plt.show()

# bar chart for title 

#data2= {'Xceed ':'    .NET Angular Software Developer', 'Confidential':'  .NET Back-End Web Developer', 'IKEN Technology':'  .NET Developer - Internship',
	# 	'Obeikan Digital Solutions':'  .Net Core Developer'}
#Company = list(data2.keys())
#Title = list(data2.values())

#plt.bar(Company, Title, color ='maroon',
	#	width = 0.6)

#plt.xlabel("company name ")
#plt.ylabel("Title of jobs")
#plt.title("jobs in different companies")
#plt.show()

#bar chart for areas
#data = {'Xceed ':'    Maadi', 'Confidential':'  Cairo', 'IKEN Technology':'  Maadi',
#		'Obeikan Digital Solutions':'  New Cairo'}
#Company = list(data.keys())
#Location = list(data.values())

#plt.bar(Company, Location, color ='maroon',
#		width = 0.6)

#plt.xlabel("company name ")
#plt.ylabel("location of company")
#plt.title("LOcation of different companies")
#plt.show()


#10


# to print skills elements



Dict=dict()
for skills in dataset['Skills']:
    for skill in skills.split(','):
        if skill in Dict.keys():
            Dict[skill]+=1
        else:
            Dict[skill]=1
from collections import Counter          
Max =Counter(Dict)
MaxFive= dict(Max.most_common(5))
print("Top 5 skills :-")
for skill,count in MaxFive.items():    
    print("%s : %d"%(skill,count))


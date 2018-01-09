# -*- coding: utf-8 -*-
import numpy as np
import re
import pandas as pd
import matplotlib.pyplot as pl
from sklearn.cluster import KMeans

pl.rc('font', family='DejaVu Sans')

##first we get the import and the export in two dataframe using panda 
all_import=pd.read_csv("data/final_table_dist-export.csv") #this should reflect the path where you downlad the dataset
all_export=pd.read_csv("data/final_table_dist-import.csv") 
all_export.port=[item.strip().replace('[^\x00-\x7F]+','_').replace(' ','_') for item in all_export.port]



imp_boat_type=all_import.groupby(['port','type'])['boat'].sum().unstack() #we use the groupby function of pandas dateframe to count the total number of boat for both type (vessel vs steamboat) for each port for all the year of the dataset (below I started a loop to do the same year by year)

all_import.port=[item.strip().replace('[^\x00-\x7F]+','_').replace(' ','_') for item in all_import.port]

exp_boat_type=all_export.groupby(['port','type'])['boat'].sum().unstack() #same for export

kmeans=KMeans(n_clusters=3,random_state=0).fit(zip(np.log(imp_boat_type['vessel']).fillna(0),np.log(imp_boat_type['steamboat']).fillna(0)))

print(kmeans.labels_)


#imp_ratio=imp_boat_type['steamboat'].fillna(1)/imp_boat_type['vessel'].fillna(1)

#exp_ratio=exp_boat_type['steamboat'].fillna(1)/exp_boat_type['vessel'].fillna(1)

#pl.scatter(range(0,len(exp_ratio)),exp_ratio)
#pl.xticks(range(0,len(exp_ratio)),exp_ratio.index)
#pl.semilogy()
#pl.show()

###plot the graph "number of vessel vs number of steamboat"

#pl.subplot(121) #subgraph for export
#pl.plot(range(1,1000000),range(1,1000000))  #the x=y line to see if ratio > or < 1 
#pl.scatter(exp_boat_type['vessel'],exp_boat_type['steamboat'])  #plot the port given number of vessel and number of steamboat
#
##we add label to the plot !!!WARNING Problem here: in the dataset there are spaces in the port names for aestetical reason, python doesn't like it so this loop doesn't work
#for label in list(exp_boat_type.index):
#    pl.annotate(label,(exp_boat_type['vessel'][label],exp_boat_type['steamboat'][label]))  #add the name of the port on the plot
#
##set axes in log scale
#pl.semilogx()
#pl.semilogy() 
#
##set a title for the subgraph
#pl.title("export")
#
#
####We do all the same to generate a subgraph for the import:
#pl.subplot(122)
pl.plot(range(1,1000000),range(1,1000000)) 
pl.scatter(imp_boat_type['vessel'],imp_boat_type['steamboat'],c=kmeans.labels_) 
#
#for label in list(imp_boat_type.index):
#    pl.annotate(label,(imp_boat_type['vessel'][label],imp_boat_type['steamboat'][label]))  
#
pl.semilogx()
pl.semilogy() 
pl.title("import")
pl.xlabel("vessel")
pl.ylabel("steamboat")
#
#
pl.show() 
#
####it sould be easy to look at how this is evolving through by looking at the data for every year wit something like that:
#
#for y in range(min(all_import.year),max(all_import.year)):
#    subimport=all_import[all_import.year == y] #we filter the dataframe and select only the row where the column year is equal to the year
#    imp_boat_type=subimport.groupby(['port','type'])['boat'].sum().unstack() 
#    subexport=all_export[all_export.year == y]
#    exp_boat_type=subexport.groupby(['port','type'])['boat'].sum().unstack() 
#    #then we could do all the same that what we did previously
#    
#
#

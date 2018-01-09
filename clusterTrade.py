import numpy as np
import pandas as pd
import matplotlib.pyplot as pl


##first we get the import and the export in two dataframe using panda 
all_import=pd.read_csv("data/final_table_dist-export.csv") #this should reflect the path where you downlad the dataset
all_export=pd.read_csv("data/final_table_dist-import.csv") 


imp_boat_type=all_import.groupby(['port','type'])['boat'].sum().unstack() #we use the groupby function of pandas dateframe to count the total number of boat for both type (vessel vs steamboat) for each port for all the year of the dataset (below I started a loop to do the same year by year)
exp_boat_type=all_export.groupby(['port','type'])['boat'].sum().unstack() #same for export


###plot the graph "number of vessel vs number of steamboat"

pl.subplot(121) #subgraph for export
pl.plot(range(1,1000000),range(1,1000000))  #the x=y line to see if ratio > or < 1 
pl.scatter(exp_boat_type['vessel'],exp_boat_type['steamboat'])  #plot the port given number of vessel and number of steamboat

#we add label to the plot !!!WARNING Problem here: in the dataset there are spaces in the port names for aestetical reason, python doesn't like it so this loop doesn't work
for label in exp_boat_type.index:
    pl.annotate(label,(exp_boat_type['vessel'][label],exp_boat_type['steamboat'][label]))  #add the name of the port on the plot

#set axes in log scale
pl.semilogx()
pl.semilogy() 

#set a title for the subgraph
pl.title("export")


###We do all the same to generate a subgraph for the import:
pl.subplot(122)
pl.plot(range(1,1000000),range(1,1000000)) 
pl.scatter(imp_boat_type['vessel'],imp_boat_type['steamboat']) 
for label in imp_boat_type.index:
    pl.annotate(label,(exp_boat_type['vessel'][label],exp_boat_type['steamboat'][label]))  
pl.semilogx()
pl.semilogy() 
pl.title("import")


pl.show() 

###it sould be easy to look at how this is evolving through by looking at the data for every year wit something like that:

for y in range(min(all_import.year),max(all_import.year)):
    subimport=all_import[all_import.year == y] #we filter the dataframe and select only the row where the column year is equal to the year
    imp_boat_type=subimport.groupby(['port','type'])['boat'].sum().unstack() 
    subexport=all_export[all_export.year == y]
    exp_boat_type=subexport.groupby(['port','type'])['boat'].sum().unstack() 
    #then we could do all the same that what we did previously
    



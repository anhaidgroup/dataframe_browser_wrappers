from pandastable_wrapper import data_explore
import pandas
#get the pandas frame from file
df = pandas.read_csv('table.csv')
#show the pandastable application before you close the app, the process will be blocked
data_explore(df)
#use df after making change through the GUI

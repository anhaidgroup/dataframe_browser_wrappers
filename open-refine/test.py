from refine import Refine
import pandas

# read file to pandas
df = pandas.read_csv("table.csv")
# create a openrefine project
p = Refine(df)
# get the new dataframe after making changes to the data
# after calling export_pandas_frame, the openRefine project will be deleted automatically
newdf = p.export_pandas_frame()
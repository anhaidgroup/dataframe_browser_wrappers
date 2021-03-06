try:
   from tkinter import *
except ImportError as e:
   from Tkinter import *

from pandastable import Table, TableModel
import pandas


class data_explore(Frame):
	"""Basic GUI frame for the table
 		Returns:
		tkinter frame
	"""
	def __init__(self, df):
		self.parent = None
		Frame.__init__(self)
		self.main = self.master
		self.main.geometry('600x400+200+100')
		self.main.title('Explore Data')
		f = Frame(self.main)
		f.pack(fill=BOTH,expand=1)
        #set the table in the GUI
		self.table = pt = Table(f, dataframe=df,
			                    showtoolbar=True, showstatusbar=True)
		pt.show()
		self.mainloop()



#df = pandas.read_csv('./2.csv')
#app = ExploreData(df)

#launch the app
#app.mainloop()



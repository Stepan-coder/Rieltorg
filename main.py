import os

from RA.Manager.Manager import *
from RA.DataSet.DataSet import *

manager = Manager(path=os.getcwd(), project_name="MSK")
manager.create_DataSet("participants")
manager.DataSet("participants").load_csv_dataset(csv_file="OriginalData/auction_up_participants_20211026.csv",
                                                 delimiter=";")
manager.create_DataSet("proc")
manager.DataSet("proc").load_csv_dataset(csv_file="OriginalData/auction_up_proc_20211026.csv",
                                         delimiter=";")
print(manager.DataSet("participants"))
print(manager.DataSet("proc "))
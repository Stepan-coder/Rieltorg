import os
from RA.Manager.Manager import *
from RA.DataSet.DataSet import *
from sklearn.feature_extraction.text import TfidfVectorizer

manager = Manager(path=os.getcwd(), project_name="MSK")
# manager.create_DataSet("participants")
# manager.DataSet("participants").load_csv_dataset(csv_file="OriginalData/auction_up_participants_20211026.csv",
#                                                  delimiter=";")
# Работаем с процедурами
manager.create_DataSet("proc")
manager.DataSet("proc").load_csv_dataset(csv_file="OriginalData/auction_up_proc_20211026.csv",
                                         delimiter=";")
# Смотрим на таблицу с данными
# manager.DataSet("proc").head(full_view=True)
# Заполняем пустоты
manager.DataSet("proc").fillna()

# Ищем последние версии записей
platform_numbers = {}
for i in range(len(manager.DataSet("proc"))):
    this_row = manager.DataSet("proc").get_row(index=i)
    if this_row['platform_number'] not in platform_numbers:
        platform_numbers[this_row['platform_number']] = this_row['version']
    else:
        if int(this_row['version']) > int(platform_numbers[this_row['platform_number']]):
            platform_numbers[this_row['platform_number']] = this_row['version']
# Находим индексы строк, которые нужно удалить
to_datate = []
for i in range(len(manager.DataSet("proc"))):
    this_row = manager.DataSet("proc").get_row(index=i)
    if not platform_numbers[this_row['platform_number']] == this_row['version']:
        to_datate.append(i)
# Удаляем
for i in reversed(to_datate):
    manager.DataSet("proc").delete_row(index=i)
manager.DataSet("proc").set_delimiter(delimiter=";")
manager.DataSet("proc").export()
quit()
# Создаём файлик с текстовыми даными о процедурах
manager.create_DataSet("texts")
manager.DataSet("texts").add_column(column_name="procedure_name",
                                    values=manager.DataSet("proc").get_column("procedure_name"))
manager.DataSet("texts").add_column(column_name="lot_subject",
                                    values=manager.DataSet("proc").get_column("lot_subject"))
manager.DataSet("texts").add_column(column_name="unit_name",
                                    values=manager.DataSet("proc").get_column("unit_name"))
manager.DataSet("texts").set_delimiter(delimiter=";")
manager.DataSet("texts").export()


from faker import Faker
import pandas as pd

def generalRandData(out_file, country, number_of_records):
    out_file_name = ''
    fake = Faker(country)
    data_list = []
    columns_list = ['GROUPID', 'INDIVUDALID', 'Column1', 'Column2', 'Column3', 'Column4', 'Column5', 'Column6', 'Column7', 'Column8', 'Column9', 'Column10']
    for val in range(number_of_records):
        data_list.append([fake.bothify(text='?', letters='ABCDEFGHJ'), fake.port_number(), fake.random_int(min=10, max=15), 
        fake.random_int(min=15, max=30),fake.random_int(min=30, max=45), fake.random_int(min=45, max=60), fake.random_int(min=60, max=75), 
        fake.random_int(min=75, max=90),fake.random_int(min=90, max=105),fake.random_int(min=105, max=120),fake.random_int(min=120, max=135),
        fake.random_int(min=135, max=150) ])


    df = pd.DataFrame(data_list,columns=columns_list)
    df.to_csv(out_file, mode='w', index = False)


generalRandData(out_file= 'GeneralFormat12Col.csv', country='nl_NL', number_of_records=1000)
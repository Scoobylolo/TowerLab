#Author: Andy Carvajal    https://github.com/Scoobylolo

import csv
import cell_api
import datetime

def get_time(timestamp):
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    dt_string = dt_object.strftime("%Y-%m-%d %H:%M:%S %a")
    return dt_string

def read_file(filename,outfile):
    as_list=[]
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        passed=False
        
        for row in reader:
            if len(row) == 6:
                col1, col2, col3, col4, col5, col6 = row
                if col1=="Timestamp":
                    passed=True
                    continue
                if not passed:
                    continue

                what,where,country = cell_api.get_info(int(col2), int(col3), int(col4), int(col5),"city")

                useful_info="Time: {}\n{}: {}, {}\n\n".format(get_time(int(col1)),what,where,country)
                as_list.append(useful_info)

                print(useful_info)
            else:
                print('Invalid row:', row)

    with open(outfile, 'w') as f:
        for item in as_list:
            f.write("%s" % item)
        f.close()

if __name__ == '__main__':
    out="locations.log"
    read_file('CellTowerData.csv',out)

    print("Check the file",out,"for the results.")


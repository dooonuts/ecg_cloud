from bme590hrm import hrm_class as hrm_class
import pandas
import csv

def main():
   return 1;

def summary(data_dict):
   form = data_format(data_dict)
      
   return 1

def data_format(data_dict):
   list(t) for t in zip(*data_dict)
   print(data_dict2)
   times  = data_dict['times']
   voltages = data_dict['voltages']
   print(type(times))
   print(times)
   #with open('hrdata.csv', 'w') as f:  # Just use 'w' mode in 3.x
   # w = csv.DictWriter(f, data_dict.keys())
   # w.writeheader()
   # w.writerow(row)
   #f.close()
   #rows = zip(data_dict['times'],data_dict['voltages'])
   #with open('hrdata.csv', "w") as f:
   # writer = csv.writer(f,delimiter= '')
   # for row in rows:
   #     writer.writerow(row)
   with open('hrdata.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(zip(*data_dict)) 
 
   return 1

def average(data_dict):
   return 1

def init(data_dict):
   return 1

if __name__ == '__main__':
    main()

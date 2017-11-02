from bme590hrm import hrm_class as hrm_class
import pandas
import csv


def main():
    return 1


def average(data_dict):
     averaging_period = data_format_average(data_dict)
     hrm_object = init()
     average = hrm_object.average_hr
     tachy = hrm_object.anomaly_tf.tachy_tf
     brady = hrm_object.anomaly_tf.brady_tf
     return [data_dict['averaging_period'], data_dict['time'],
         average, tachy, brady]


def summary(data_dict):
    data_format_summary(data_dict)
    hrm_object = init()
    # need to add instant
    instant = hrm_object.instantaneous_hr
    tachy = hrm_object.anomaly_tf.tachy_tf
    brady = hrm_object.anomaly_tf.brady_tf
    return [data_dict['time'], instant, tachy, brady]


def data_format_summary(data_dict):
    times = data_dict['time']
    voltages = data_dict['voltage']
    rows = zip(times, voltages)
    with open('hrdata.csv', "w") as f:
        writer = csv.writer(f, delimiter=',')
        for row in rows:
            writer.writerow(row)


def data_format_average(data_dict):
    times = data_dict['time']
    voltages = data_dict['voltage']
    averaging_period = data_dict['averaging_period']
    rows = zip(times, voltages)
    with open('hrdata.csv', "w") as f:
         writer = csv.writer(f, delimiter=',')
         for row in rows:
             writer.writerow(row)
    return averaging_period


def init():
    hrm_object = hrm_class.HrmData('hrdata.csv')
    return hrm_object


if __name__ == '__main__':
    main()

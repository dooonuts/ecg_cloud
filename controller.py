from bme590hrm import hrm_class as hrm_class
import pandas
import csv


def main():
    """Main function of controller

       :rtype: always returns 1 if no syntax errors
    """

    return 1


def average(data_dict):
     """Function to get average data from hrm_class

	:param data_dict (dict): the dict to hold times, voltages, avg period
        :rtype: int avg period used, lists of the times, average heartbeat (bpm), \
          and true/false lists for if tachy and brady occurred in time period
     """
     
     averaging_period = data_format_average(data_dict)
     # try:
     # hrm_object = init()
     # except:	
     average = hrm_object.average_hr
     tachy = hrm_object.anomaly_tf.tachy_tf
     brady = hrm_object.anomaly_tf.brady_tf
     return [data_dict['averaging_period'], data_dict['time'],
         average, tachy, brady]


def summary(data_dict):
    """Function to get instantaneous data from hrm_class

       :param data_dict (dict): the dict to hold times and voltages
       :rtype: list of times where instant hr was tested, instantaneous \
         heart beat (bpm), and true/false lists for it tachy and brady occurred \
         in time period
    """

    data_format_summary(data_dict)
    hrm_object = init()
    # need to add instant
    instant = hrm_object.instantaneous_hr
    # print(hrm_object.anomaly_tf)
    tachy = hrm_object.anomaly_tf[0]
    brady = hrm_object.anomaly_tf[1]
    return [data_dict['time'], instant, tachy, brady]


def data_format_summary(data_dict):
    """Function to format the data for routing of summary

       :param data_dict (dict): the dictionary to hold times and voltages
       :rtype: writes in a text file
    """

    times = data_dict['time']
    voltages = data_dict['voltage']
    rows = zip(times, voltages)
    with open('hrdata.csv', "w") as f:
        writer = csv.writer(f, delimiter=',')
        for row in rows:
            writer.writerow(row)


def data_format_average(data_dict):
    """Function to format the data for routing of summary

       :param data_dict (dict): the dictionary to hold times, voltages, and \
         avg period
       :rtype: writes in a text file
    """

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
    """Function to instantiate the hrm object

       :rtype: the hrm_object created
    """

    hrm_object = hrm_class.HrmData('hrdata.csv')
    return hrm_object


if __name__ == '__main__':
    main()

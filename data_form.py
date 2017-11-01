import pandas
import numpy


def main(filename):
    change_data(filename)
    return 1


def file_checker(filename, names):
    """Function that checks the file has the right types
        for ECG_data

        :param self: the hrm object
        :param filename: csv file that contains the ecg data
        :param names: header to help pandas work
        :rtype: Boolean for if there is an error

    """

    try:
        df = pandas.read_csv(
            filename, header=None, names=names, converters={
                "times": float, "voltages": float})
        err_Bool = False
        return err_Bool
    except ValueError:
        err_Bool = True
        return err_Bool


def change_data(filename):
    names = ["times", "voltages"]
    data_error = file_checker('filename', names)
    if (data_error):
        print("Non-Numeric Value Entered")
        return [{}, {}]
    else:
        ecg_data = pandas.read_csv(
            self.file, header=None, names=names, converters={
                "times": float, "voltages": float})
        times = ecg_data.times.values
        voltages = ecg_data.voltages.values
        print(times)
        print(voltages)
        return [{}, {}]


if __name__ == '__main__':
    main('hrdata.csv')

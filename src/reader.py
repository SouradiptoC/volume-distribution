import pandas as pd
from printError import printErr
from compData import compData


def csvReader(filename: str, delimiter: str = ','):
    """Reads a properly formatted CSV file

    :param filename: Name of CSV file to read from
    :type filename: str
    :param delimiter: Delimiter used in CSV document, defaults to ','
    :type delimiter: str, optional
    :raises KeyError: If CSV file header is not properly formatted
    :return: Dose Data, Concentration Data, Time Data
    :rtype: compData
    """
    try:
        retData = pd.read_csv(filename, delimiter)
    except FileNotFoundError as err:
        printErr(err, 3)

    # Possible header for CSV file columns
    # Consult documentation for further clarification
    doseHead = ['Dose', 'dose', 'DOSE']
    concHead = ['Conc', 'conc', 'CONC', 'C_p']
    timeHead = ['Time', 'time', 'TIME', 'T']

    # Extract dose data
    for each in doseHead:
        doseData = retData.get(each, None)
        if doseData is not None:
            break
    else:
        raise KeyError('Dose data not found! Check Header')

    # Extract concentration data
    for each in concHead:
        concData = retData.get(each, None)
        if concData is not None:
            break
    else:
        raise KeyError('Conc data not found! Check Header')

    # Extract time data
    for each in timeHead:
        timeData = retData.get(each, None)
        if timeData is not None:
            break
    else:
        raise KeyError('Time data not found! Check Header')

    # Return dose, concentration and time data
    return compData(concData, timeData, doseData)


def dataReader(filename: str):
    """A general file reader which calls a specific reader depending on extension

    :param filename: Name of the file to read
    :type filename: str
    :return: Dose data, Concentration data, Time data
    :rtype: compData
    """
    # Check extension of given filename
    nameAsList = filename.split('.')
    fileExt = nameAsList[-1]

    # Use proper function to handle given file
    if fileExt == 'csv':
        return csvReader(filename)
    else:
        printErr('File type not compatible', 3)

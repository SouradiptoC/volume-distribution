import os
import pandas as pd
from printError import printErr


def reader(FileName):
    """Reads data from files with various extensions. Currently only working for csv extension

    :param FileName: Name of file from where data should be read
    :type FileName: str
    :return: A dataframe containing data from file
    :rtype: pandas.dataframe
    """
    # Check extension of given filename
    nameAsList = FileName.split('.')
    fileExt = nameAsList[-1]

    # Use proper function to handle given file
    if fileExt == 'csv':
        return pd.read_csv(FileName)
    else:
        printErr('File type not compatible', 3)


def comparison(FileName, VolumeDistribution, outFolder):
    """Produces a sorted .xlsx file, where one can compare the volume distribution of sample with some known drugs

    :param FileName: Name/Path of dataset containg name and volume distribution data of known drugs
    :type FileName: str
    :param VolumeDistribution: volume distribution of the sample
    :type VolumeDistribution: float
    :param outFolder: Folder to save all of output data (graphs, comparison data, computational result)
    :type outFolder: str
    """
    # Creating data heads
    nameHead = ['Name', 'NAME', 'name']

    # Reading data from file
    df1 = reader(FileName)

    # Setting and checking data heads
    (name, volume) = df1.keys()
    for i in nameHead:
        if name == i:
            break
    else:
        raise KeyError('Name data not found! Check Header')

    # Appending the sample volume distribution to the data read
    df2 = pd.DataFrame({name: ['Sample'],
                        volume: [VolumeDistribution]})

    df1 = df1.append(df2, ignore_index=True)

    outFile = os.path.join(outFolder, 'Drug_Comparison.xlsx')

    # Sorting the data and exporting it
    sorted_df = df1.sort_values(by=['V'], ascending=True)
    sorted_df.to_excel(outFile,
                       sheet_name='Comparison Sheet')

import os
from numpy import log
import matplotlib.pyplot as plt
from scipy import stats

from reader import dataReader
from findDistribution import findDistribution
from comparison import comparison


def plotConcTime(rData, outFolder):
    """Plots the concentration vs time curve

    :param rData: Data read by the reader
    :type rData: compData.compData
    :param outFolder: Folder to save the output graph
    :type outFolder: str
    """

    plt.plot(rData.timeData, rData.concData, 'o')
    plt.title('Concentration Vs Time')
    plt.xlabel('Time (hr)')
    plt.ylabel('Concentration (ng/mL)')
    # Saving the curve
    outFile = os.path.join(outFolder, 'ConcVsTime.svg')
    plt.savefig(outFile)
    plt.close()


def plotLogConcTime(rData, outFolder):
    """Plots the concentration times time vs time curve

    :param rData: Data read by the reader
    :type rData: compData.compData
    :param outFolder: Folder to save the output graph
    :type outFolder: str
    """
    # Calculating log of concentration data
    logConc = rData.logConc()
    res = stats.linregress(rData.timeData, logConc)
    # Plotting the values and fitted curve
    plt.plot(rData.timeData, logConc, 'o', label='Original Data')
    plt.plot(rData.timeData, (res.intercept + (res.slope * rData.timeData)),
             'r', label='Fitted Line')
    plt.title('log(Concentration) Vs Time')
    plt.xlabel('Time')
    plt.ylabel('log(Conc)')
    plt.text(17.5, 4, f'Slope = {round(res.slope, 5)}')
    plt.legend()
    # Saving the curve
    outFile = os.path.join(outFolder, 'logConcVsTime.svg')
    plt.savefig(outFile)
    plt.close()


def makeOutput(drugData, knwnMediData, outFolder):
    """Makes the final output

    :param drugData: The dataset containing the concentration vs time information
    :type drugData: str
    :param knwnMediData: The dataset containing names and distribution data of known drugs
    :type knwnMediData: str
    :param outFolder: Folder to save all of output data (graphs, comparison data, computational result)
    :type outFolder: str
    """
    # Reading and calculating necessary data
    rData = dataReader(drugData)
    (elim_const, AreaVol, StdyStVol) = findDistribution(rData)

    resFileLoc = os.path.join(outFolder, 'result.txt')
    # Creating the output file
    with open(resFileLoc, 'w') as outFile:
        print(f"Computation Result Log:\n----------------------\n", file=outFile)
        print(
            f"Elimination Constant for provided drug: {elim_const}", file=outFile)
        print(
            f"Half life for elimination for provided drug: {log(2)/(-1 * elim_const)}", file=outFile)
        print(
            f"Areal Volume Distribution (V_area) for provided drug: {AreaVol}", file=outFile)
        print(
            f"Steady State Volume Distribution (V_ss) for provided drug: {StdyStVol}", file=outFile)

    plotConcTime(rData, outFolder)
    plotLogConcTime(rData, outFolder)

    comparison(knwnMediData, StdyStVol, outFolder)


if __name__ == '__main__':
    parentDir = os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.pardir))
    drugFileName = os.path.join(parentDir, 'DrugData.csv')
    knwnMediFileName = os.path.join(parentDir, 'KnownDrugData.csv')

    outFolder = os.path.join(parentDir, 'result')
    if not os.path.exists(outFolder):
        os.makedirs(outFolder)

    makeOutput(drugFileName, knwnMediFileName, outFolder)

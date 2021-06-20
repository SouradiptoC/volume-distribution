from compData import compData


def findDistribution(readerData: compData):
    """Calculates the volume distribution and elemination constant by the help of compData methods

    :param readerData: The data returned by reader
    :type readerData: compData
    :return: Areal Volume Distribution, Steady State Volume Distribution, Elimination Constant
    :rtype: numpy.float64
    """

    k_el = readerData.elimConst()
    vArea = readerData.arealVolDist()
    vSs = readerData.sdStVolDist()

    return k_el, vArea, vSs

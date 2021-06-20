import numpy as np
import scipy.integrate as si
import scipy.stats as st


class compData:
    """Various methods and parameters are generated
    """

    def __init__(self, concData, timeData, doseData) -> None:
        """Necessary parameters are generated

        :param concData: Concentration of drug in plasma
        :type concData: numpy.ndarray
        :param timeData: Time
        :type timeData: numpy.ndarray
        :param doseData: Dose administered
        :type doseData: numpy.ndarray
        """
        self.concData = np.array(concData)
        self.timeData = np.array(timeData)
        self.doseData = np.array(doseData)
        self.areaConcByTimeVal = self.areaConcByTimeVal = si.trapezoid(
            self.concData, self.timeData)

    def logConc(self) -> np.ndarray:
        """Calculates the log of concentration data

        :return: The log of concentration data
        :rtype: numpy.ndarray
        """
        return np.log(self.concData)

    def concMulTime(self) -> np.ndarray:
        """Calculates the concentration times time data

        :return: The concentration times time data
        :rtype: numpy.ndarray
        """
        return self.concData * self.timeData

    def elimConst(self) -> np.float64:
        """Calculates the slope of lof of concentration data vs time data curve

        :return: The value of slope
        :rtype: numpy.float64
        """
        res = st.linregress(self.timeData, self.logConc())
        return res.slope

    def areaConcByTime(self) -> np.float64:
        """Calculates the area under the concentration vs time curve

        :return: The value of area
        :rtype: numpy.float64
        """
        return self.areaConcByTimeVal

    def areaConcTimeByTime(self) -> np.float64:
        """Calculates the area under the concentration times time vs time curve

        :return: The value of area
        :rtype: numpy.float64
        """
        return si.trapezoid(self.concMulTime(), self.timeData)

    def meanRsdncTime(self) -> np.float64:
        """Calculates Mean residence time of the drug

        :return: The value of Mean residence time
        :rtype: numpy.float64
        """
        return self.areaConcTimeByTime() / self.areaConcByTimeVal

    def arealVolDist(self) -> np.float64:
        """Calculates the areal volume distribution

        :return: The value of areal volume distribution
        :rtype: numpy.float64
        """
        return self.doseData[0] / (-1 * self.elimConst() * self.areaConcByTimeVal)

    def sdStVolDist(self) -> np.float64:
        """Calculates the steady state volume distribution

        :return: The value of steady state volume distribution
        :rtype: numpy.float64
        """
        return (self.doseData[0] / self.areaConcByTimeVal)*self.meanRsdncTime()

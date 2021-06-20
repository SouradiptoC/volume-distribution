Calculation of Volume Distribution
***********************************

The Volume of Distribution is calculated in the below written fashion:

Necessary Parameters
====================

.. csv-table::
    :header: Parameters, Insight

    :math:`X`, Dose Administered
    :math:`C`, Concentration dataset [provided]
    :math:`T`, Time dataset [provided]
    :math:`ln(C)`, The natural logarithm of concentration data
    :math:`CT`, The multiplication of :math:`C` with :math:`T`
    :math:`K_{el}`, Elimination constant
    :math:`AUC`, Area under :math:`C` ~ :math:`T` curve
    :math:`AUMC`, Area under :math:`CT` ~ :math:`T` curve
    :math:`MRT`, The ratio of :math:`AUMC` to :math:`AUC`

Manipulating Necessary Parameters
=================================

#. :math:`X` is taken from the Dose Data.
#. :math:`ln(C)` is made by applying :math:`log` to each element of :math:`C`.
#. :math:`CT` is made by multiplying :math:`C` with :math:`T`.
#. :math:`k_{el}` is calculated by linear regression from :math:`ln(C)` ~ :math:`T` curve, and will be plotted later.
#. :math:`AUC` is the area under :math:`C` ~ :math:`T` curve, calculated by trapizoidal rule.
#. :math:`AUMC` is the area under :math:`CT` ~ :math:`T` curve, calculated by trapizoidal rule.
#. :math:`MRT` is calculated by the ratio of :math:`AUMC` to :math:`AUC`

.. note::
    If :math:`C` and :math:`T` starts from 0, then program will try to compute :math:`ln(0)`, which is undefined.

Calculating Volume Distribution
===============================

#. :math:`V_{area}` is calculated by the formula 
    .. math::
        \frac{X}{K_{el} \times AUC}
#. :math:`V_{ss}` is calculated by the formula
    .. math::
        \frac{X}{AUC} \times MRT

An Insight to the Function Used
===============================

#. :func:`findDistribution.findDistribution`

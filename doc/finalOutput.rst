Computing the Final Output
***************************
Final output was computed by the help of function below. After successful completion one will get following things

Files Generated
===============
.. csv-table::
    :header: File Name, File Type, File Extension, Description

    Output, Text file, .txt, This file contains elimination constant etc data of the drug.
    ConcVsTime, Image file, .svg, This is the image of plot of concentration vs time data.
    logConcVsTime, Image file, .svg, This is the image of semi-log plot of concentration vs time data.
    Comparison_Datasheet, Excel file, .xlsx, This file holds a datasheet comprising of various known drugs name and their volume distribution value.

Outputs
=======

#. The .txt file looks like
    
    .. code-block:: text

        Computation Result Log:
        ----------------------

        Elimination Constant for provided drug: -0.12254209281701582
        Areal Volume Distribution (V_area) for provided drug: -0.00017461881862055508
        Steady State Volume Distribution (V_ss) for provided drug: 0.00014069457215783743

#. The plot of concentration vs time for my dataset is
    
    .. image:: ../doc/images/ConcVsTime_1.png

#. The semi-log plot of concentration vs time for my dataset is

    .. image:: ../doc/images/logConcVsTime_1.png

#. The .xlsx file looks like
 
   .. image:: ../doc/images/Comparison_Dataset.png

An Insight to the Function Used
================================
:func:`finalResult.makeOutput`
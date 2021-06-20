Comparison With Known Data
**************************

Known Data
==========

Known data is a dataset containing names and related V\ :sub:`d` \ values of various drugs. It is also an .csv file. The delimeter should be comma (,). The fields should be as followed.

.. csv-table::
    :header: File type, Name Data, :math:`V_d` Data

    csv, Name / NAME / name, V / Volume_Distribution / VOLUME_DISTRIBUTION / volume_distribution / V_d

In order to use the program, it has to be made sure that the data consists of the above written headings.

.. caution::
    Entertaining other headings will not work.

This is a sample data

.. csv-table::
    :header: Name, V

    Acetaminophen, 67
    Amikacin, 19
    Amoxicillin, 15
    Amphotericin, 53
    Ampicillin, 20
    Tubocurarine, 27
    Valproic acid, 9.1
    Vancomycin, 27
    Verapamil, 350
    Warfarin, 9.8
    Zidovudine, 98

Comparison
==========

Comparison is achieved by below written steps:

#. The provided dataset is read.
#. The Volume Distribution value is appended.
#. At last, that is sorted by the values of Volume Distribution, in ascending manner, and is exported.
    
Output of Comparison
====================

After the successful completion of the program, one file will be generated. Details are given below

.. csv-table::
    :header: Name, Insight

    File name, Comparison_Dataset
    File type, .xlsx
    Sheet Name, Comparison Sheet
    Column, As provided in the known data
    Row, Index numbers from parent dataset

An Insight to the Function Used
===============================

#. :func:`comparison.comparison`
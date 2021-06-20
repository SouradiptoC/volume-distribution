Basics of Volume of Distribution
********************************

Definition
==========

The volume of distribution (V\ :sub:`d`\) is a pharmacokinetic parameter representing an individual drug’s propensity to either remain in the plasma or redistribute to other tissue compartments. It is completely theoritical parameter.

Volume of distribution is proportional to the dose of administration (Dose) and is inversely proportional to the plasma concentration (Conc).

.. math::
    V_d = \frac{Dose}{Conc}

Generally, volume of distribution is the V\ :sub:`d` \ value after the equilibrium occurs.

Classifications
===============
There are some 'versions' of V\ :sub:`d` \which are used for different works, like:

* :Initial Volume Distribution: It is also called Volume Distribution for central compartment. It is shown as :math:`V_i`.
* :Extrapolated Volume Distribution: It is also known as :math:`V_d` of tissue compartment. It is shown as :math:`V_{extrp}`. It is used seldom.
* :Areal Volume Distribution: It is shown as :math:`V_{area}`. It is closer to actual volume distribution.
* :Steady State Distribution: It is shown as :math:`V_{ss}`. It is most widely used value of volume distribution. Generally, volume of distribution means Steady State distribution.

Formulae
========
.. csv-table::
    :header: Name, Formulae

    :math:`V_d`, :math:`\\{\frac{X}{C}}`
    :math:`V_i`, Null
    :math:`V_{area}`, :math:`\\{\frac{X}{K_{el} \times AUC}}`
    :math:`V_{ss}`, :math:`\\{\frac{X}{AUC} \times MRT}`

The parameters to the above formulae is illustrated below.

.. csv-table::
    :header: Name, Meaning, Derivation

    :math:`X`, Dose administered, --
    :math:`C`, Concentration of drug in plasma, --
    :math:`t`, time, --
    :math:`K_{el}`, Elimination factor, slope of semilog :math:`C` Vs :math:`t` curve
    :math:`AUC`, Area under curve, Area under :math:`C` Vs :math:`t` curve
    :math:`MRT`, Mean residence time, :math:`\\{\frac{AUMC}{AUC}}`
    :math:`AUMC`, Area under first moment curve, Area under :math:`(C \times t)` Vs :math:`t` curve
    
.. note::
    :math:`V_i` is calculated by extrapolation of Conc Vs Time curve to t = 0


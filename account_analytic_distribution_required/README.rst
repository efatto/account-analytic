======================================
Account Analytic Distribution Required
======================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:4cf526ddfb9a6c05b86a33c4e7a7bc126698d9deac29d8a06bf271ecf9e4fae3
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Faccount--analytic-lightgray.png?logo=github
    :target: https://github.com/OCA/account-analytic/tree/12.0/account_analytic_distribution_required
    :alt: OCA/account-analytic
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/account-analytic-12-0/account-analytic-12-0-account_analytic_distribution_required
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/account-analytic&target_branch=12.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module extends account_analytic_required and adds 2 policies to
control the use of analytic distributions. The policies behave as follow

* never: no analytic account nor analytic distribution allowed
* always: analytic account required
* always_plan: analytic_distribution required
* always_plan_or_account: analytic distribution or analytic account required
* optional: do what you like,

In any case analytic account and analytic distribution are mutually exclusive.

**Table of contents**

.. contents::
   :local:

Configuration
=============

To configure this module, you need to:

#. Go to *Invoicing > Configuration > Accounting > Account
   Types* and select the correct **Policy for analytic account** for every
   account type you want.

Usage
=====

To use this module, you need to:

#. Create an invoice and add a line with an account of the same type you
   are configured above.
#. Add a tag that has an analytical distribution
   ('Analytic Distribution' field set to true) or an analytic account to that
   line.
#. When you validate the invoice you get a message if analytic account or
   distribution are incorrect.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/account-analytic/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/account-analytic/issues/new?body=module:%20account_analytic_distribution_required%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* ACSONE SA/NV
* Tecnativa

Contributors
~~~~~~~~~~~~

* Stéphane Bidoul <stephane.bidoul@acsone.eu>
* `Tecnativa <https://www.tecnativa.com>`_:

  * Vicent Cubells
  * Ernesto Tejeda

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/account-analytic <https://github.com/OCA/account-analytic/tree/12.0/account_analytic_distribution_required>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.

django-occupations
=============================

|pypi-badge| |travis-badge| |codecov-badge| |doc-badge| |pyversions-badge|
|license-badge|


django-occupations is a reusable Django App for importing, updating, and managing structured occupation data.


Overview (please modify)
------------------------

The structure of this data is currently based primarily on the US Federal Government's Standard Occupational Classification (SOC) system, but in the future we aspire to support other structured occupation sources. The US Federal Government's Office of Management and Budget is responsible for maintaining the Standard Occupational Classification (SOC) system. For more information on SOC, please visit https://www.bls.gov/soc/ or https://www.bls.gov/soc/2018/soc_2018_manual.pdf or https://www.bls.gov/soc/2018/soc_2018_definitions.pdf and https://www.bls.gov/soc/2018/soc_structure_2018.pdf 


Roadmap
-------------
- Update documentation
- Add model relationships
- Add test coverage
- Add management command to pull the latest SOC data
- Add latest SOC data to version control and add a migration to populate data from SOC data
- Clean up some lingering references to edX that no longer make sense (this repo was set up using an edX-authored cookiecutter https://github.com/edx/edx-cookiecutters/tree/master/cookiecutter-django-app )

Documentation
-------------

(TODO: Set up documentation)


License
-------

The code in this repository is licensed under the Apache Software License 2.0 unless
otherwise noted.

Please see `LICENSE.txt <LICENSE.txt>`_ for details.

How To Contribute
-----------------

Contributions are very welcome.
Please read `How To Contribute <https://github.com/edx/edx-platform/blob/master/CONTRIBUTING.rst>`_ for details.
Even though they were written with ``edx-platform`` in mind, we are happy to invite contributions using the same guidelines.

The pull request description template should be automatically applied if you are creating a pull request from GitHub. Otherwise you
can find it at `PULL_REQUEST_TEMPLATE.md <.github/PULL_REQUEST_TEMPLATE.md>`_.

The issue report template should be automatically applied if you are creating an issue on GitHub as well. Otherwise you
can find it at `ISSUE_TEMPLATE.md <.github/ISSUE_TEMPLATE.md>`_.

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email hello@careervillage.org.

Getting Help
------------

If you're having trouble, please comment in the Github Issues for this repo or contact us at hello@careervillage.org

.. |pypi-badge| image:: https://img.shields.io/pypi/v/django-occupations.svg
    :target: https://pypi.python.org/pypi/django-occupations/
    :alt: PyPI

.. |travis-badge| image:: https://travis-ci.org/edx/django-occupations.svg?branch=master
    :target: https://travis-ci.org/CareerVillage/django-occupations
    :alt: Travis

.. |codecov-badge| image:: https://codecov.io/github/edx/django-occupations/coverage.svg?branch=master
    :target: https://codecov.io/github/CareerVillage/django-occupations?branch=master
    :alt: Codecov

.. |doc-badge| image:: https://readthedocs.org/projects/django-occupations/badge/?version=latest
    :target: https://django-occupations.readthedocs.io/en/latest/
    :alt: Documentation

.. |pyversions-badge| image:: https://img.shields.io/pypi/pyversions/django-occupations.svg
    :target: https://pypi.python.org/pypi/django-occupations/
    :alt: Supported Python versions

.. |license-badge| image:: https://img.shields.io/github/license/edx/django-occupations.svg
    :target: https://github.com/CareerVillage/django-occupations/blob/master/LICENSE.txt
    :alt: License

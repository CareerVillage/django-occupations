"""
Database models for django_occupations.
"""
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from model_utils.models import TimeStampedModel


@python_2_unicode_compatible
class Occupation(TimeStampedModel):
    """
    An occupation is a grouping of a number of individual jobs. Thus, an
    occupational definition is a collective description of a number of similar individual jobs
    performed, with minor variations, in different establishments.

    If you are planning to restrict your use of django-occupations to occupations listed on the US 
    Office of Management and Budget Standard Occupational Classification (SOC) system, then you 
    will end up with one Occupation for every SOCDetailedOccupation. Occupations are separated out 
    to allow for one extra layer of abstraction in case you want to specify occupations outside of 
    the SOC standard. 

    .. no_pii:
    """

    name = models.CharField(max_length=256, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    soc_occupation = models.ForeignKey(SOCDetailedOccupation, null=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        # TODO: return a string appropriate for the data fields
        return '<Occupation, ID: {}>'.format(self.id)

    def get_description():
        """
        TODO: Return local description if it's available, or the SOC description as a backup, or empty if neither is available
        """
        return

    def is_catchall():
        """
        TODO: Returns True if the SOC code ends in a 9 or have "All other" at the end of the description
        """
        return


@python_2_unicode_compatible
class SOCDetailedOccupation(TimeStampedModel):
    """
    TODO: replace with a brief description of the model.

    .. no_pii:
    """

    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True)
    broad_occupation = models.ForeignKey(SOCBroadOccupation, null=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        # TODO: return a string appropriate for the data fields
        return '<SOCDetailedOccupation, ID: {}>'.format(self.id)


@python_2_unicode_compatible
class SOCBroadOccupation(TimeStampedModel):
    """
    TODO: replace with a brief description of the model.

    .. no_pii:
    """

    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True)
    minor_group = models.ForeignKey(SOCMinorGroup, null=True,
                                   on_delete=models.SET_NULL)


    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        # TODO: return a string appropriate for the data fields
        return '<SOCBroadOccupation, ID: {}>'.format(self.id)


@python_2_unicode_compatible
class SOCMinorGroup(TimeStampedModel):
    """
    SOC Minor Occupational Groups

    .. no_pii:
    """

    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True)
    major_group = models.ForeignKey(SOCMajorGroup, null=True,
                                   on_delete=models.SET_NULL)


    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        # TODO: return a string appropriate for the data fields
        return '<SOCMinorGroup, ID: {}>'.format(self.id)


@python_2_unicode_compatible
class SOCMajorGroup(TimeStampedModel):
    """
    SOC Major Occupational Groups

    .. no_pii:
    """

    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True)
    intermediate_aggregation_group = models.ForeignKey(SOCIntermediateAggregationGroup, null=True,
                                   on_delete=models.SET_NULL)
    high_level_aggregation_group = models.ForeignKey(SOCHighLevelAggregationGroup, null=True,
                                   on_delete=models.SET_NULL)


    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        # TODO: return a string appropriate for the data fields
        return '<SOCMajorGroup, ID: {}>'.format(self.id)


@python_2_unicode_compatible
class SOCIntermediateAggregationGroup(TimeStampedModel):
    """
    BLS recommended intermediate-level aggregations

    Refer to Table 6 on https://www.bls.gov/soc/2018/soc_2018_manual.pdf

    .. no_pii:
    """

    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        # TODO: return a string appropriate for the data fields
        return '<SOCIntermediateAggregationGroup, ID: {}>'.format(self.id)


@python_2_unicode_compatible
class SOCHighLevelAggregationGroup(TimeStampedModel):
    """
    BLS recommended high-level aggregations

    Refer to Table 6 on https://www.bls.gov/soc/2018/soc_2018_manual.pdf

    .. no_pii:
    """

    # TODO: add field definitions

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        # TODO: return a string appropriate for the data fields
        return '<SOCHighLevelAggregationGroup, ID: {}>'.format(self.id)


@python_2_unicode_compatible
class SOCDirectMatchTitles(TimeStampedModel):
    """
    TODO: This is a placeholder for DirectMatchTitles. Refer to https://www.bls.gov/soc/2018/home.htm#match 

    .. no_pii:
    """

    # TODO: add field definitions

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        # TODO: return a string appropriate for the data fields
        return '<SOCDirectMatchTitles, ID: {}>'.format(self.id)

from django.db import models


class Event(models.Model):
    AREA = (('t', 'testing'), ('p', 'production'),)
    RUN = (('y', 'yes'), ('n', 'not'),)
    area = models.CharField(max_length=1, choices=AREA)
    date = models.DateField('date of deployment')
    run = models.CharField(max_length=1, choices=RUN, default='n')

    def __str__(self):
        if self.area == 't':
            return 'Test Deploy: {:%Y-%m-%d %H:%M:%S}'.format(self.date)
        elif self.area == 'p':
            return 'Production Deploy: {:%Y-%m-%d %H:%M:%S}'.format(self.date)


class Update(models.Model):
    CLASSIFICATION = (
        ('s', 'security'),
        ('c', 'critical'),
        ('o', 'other'),
        ('n', 'not defined'),
    )
    PRODUCT = (
        ('w7', 'windows 7'),
        ('w10', 'windows 10'),
        ('o10', 'office 10'),
        ('o13', 'office 13'),
        ('oth', 'other product')
    )
    kb_name = models.CharField(max_length=50)
    release_date = models.DateField('date of release', blank=True)
    classification = models.CharField(
        max_length=1, choices=CLASSIFICATION, default='n')
    product = models.CharField(max_length=4, choices=PRODUCT)
    test_deploy = models.ManyToManyField(
        Event, verbose_name='test deploy', blank=True)

    def __str__(self):
        return self.kb_name

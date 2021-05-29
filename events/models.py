from django.db import models
# from members.models import Member, Shepherd

# Create your models here.


class EventType(models.Model):
    event_type = models.CharField(
        max_length=40, blank=False, unique=True, null=False)
    Remarks = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.event_type


class Event(models.Model):
    service_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    # shepherd = models.OneToOneField('Shepherd', on_delete=models.CASCADE)
    # litergist = models.OneToOneField('Member', on_delete=models.CASCADE)
    topic = models.CharField(max_length=255, null=True, blank=True)
    scriptures = models.CharField(max_length=255, null=True, blank=True)

    groom_name = models.CharField(max_length=255, null=True, blank=True)
    bride_name = models.CharField(max_length=255, null=True, blank=True)
    invited_paster = models.CharField(max_length=255, null=True, blank=True)

    event_date = models.DateField()
    event_time_start = models.TimeField()
    event_end_time = models.TimeField()
    Remarks = models.CharField(max_length=256, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_type.event_type + ' on ' + str(self.event_date)


class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    adult_male = models.IntegerField(blank=True)
    adult_female = models.IntegerField(blank=True)
    youth_male = models.IntegerField(blank=True)
    youth_female = models.IntegerField(blank=True)
    young_adults_male = models.IntegerField(blank=True)
    young_adults_female = models.IntegerField(blank=True)
    children = models.IntegerField(blank=True)
    total_male = models.IntegerField(default=0)
    total_female = models.IntegerField(default=0)
    total_attendance = models.IntegerField(default=0)

# redefining the save here makes sure that the calulations for the totals are made and the column updated

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.total_male:
            self.total_male = self.adult_male + self.youth_male + self.young_adults_male
        if not self.total_female:
            self.total_female = self.adult_female + \
                self.youth_female + self.young_adults_female
        if not self.total_attendance:
            self.total_attendance = self.total_male + self.total_female + self.children
        return super(Attendance, self).save(force_insert=False, force_update=False, using=None,
                                            update_fields=None)

    def __str__(self):
        return "Total attendance last " + str(self.event.service_type) + str(self.event.event_date.strftime('%A %d %B %Y')) + " is " + str(self.total_attendance)

    class Meta:
        verbose_name_plural = "attendance"

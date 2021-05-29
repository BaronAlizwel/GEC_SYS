from django.db import models

# Create your models here.


class Shepherd(models.Model):
    id = models.AutoField(primary_key=True)
    # membership_details = models.OneToOneField(
    #     "members.ShepherdMember", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Ministry(models.Model):
    Adult = "Adult"
    Youth = "Youth"
    Young_Adults = "Young_Adults"
    Children = "Children"
    Other = "Other"
    ministry_choices = ((Adult, "Adult"),
                        (Youth, "Youth"),
                        (Young_Adults, "Young_Adults"),
                        (Children, "Children"),
                        (Other, "Other"))
    ministry = models.CharField(max_length=15, unique=False, blank=False, choices=ministry_choices,
                                default=Adult)
    remarks = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.ministry + " " + self.remarks

    class Meta:
        verbose_name_plural = "ministries"
        # verbose names should conventionally not be capitalized.. Django does that auto


class Member(models.Model):

    id = models.AutoField(primary_key=True)

    title_choices = (('Mr', 'Mr'),
                     ('Mrs', 'Mrs'),
                     ('Miss', 'Miss'),
                     ('Pastor', 'Pastor'),
                     ('Reverend', 'Reverend'),
                     ('Minister', 'Minister'),
                     ('Presbyter', 'Presbyter'),
                     ('Presbyteress', 'Presbyteress'))
    title = models.CharField(choices=title_choices, max_length=20)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_names = models.CharField(max_length=255)

    # name = str(first_name) + ' ' + str(other_names) + ' ' + str(last_name)

    gender_choices = (('Male', 'Male'), ('Female', 'Female'))
    gender = models.CharField(choices=gender_choices, max_length=10)

    date_of_birth = models.DateField()

    # gender_selection = (('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
    #                     ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'))

    # days_of_week = ((1, "Monday"), (2, "Tuesday"), (3, "Wednesday"),
    #                 (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday'))

    day_of_week_choices = (('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
                           ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'))
    day_of_birth = models.CharField(choices=day_of_week_choices, max_length=10)
    place_of_birth = models.CharField(max_length=255, null=True, blank=True)
    hometown = models.CharField(max_length=255, null=True, blank=True)
    nationality = models.CharField(max_length=255, default="Ghanaian")

    profile_pic = models.FileField()
    # picture = models.ImageField(upload_to = upload_image_path, null = True, blank = True)

    telephone = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)

    working = models.BooleanField()
    occupation = models.CharField(max_length=255, null=True, blank=True)
    schooling = models.BooleanField()
    school = models.CharField(max_length=255, null=True, blank=True)

    fathers_name = models.CharField(max_length=255, null=True, blank=True)
    mothers_name = models.CharField(max_length=255, null=True, blank=True)
    guardians_name = models.CharField(max_length=255, null=True, blank=True)

    # shepherd = models.ForeignKey(
    #     Shepherd, on_delete=models.CASCADE, null=True, blank=True)

    baptized = models.BooleanField()
    baptism_date = models.DateField(null=True, blank=True)

    confirmed = models.BooleanField()
    confirmation_date = models.DateField(null=True, blank=True)
    confirmation_church = models.CharField(
        max_length=255, null=True, blank=True)

    new_believer_school = models.BooleanField()

    ministry = models.ForeignKey(
        Ministry, on_delete=models.CASCADE, null=True, blank=True)

    # group = models.ForeignKey(
    #     Group, on_delete=models.CASCADE, null=True, blank=True)

    active = models.BooleanField()
    pays_tithe = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    leader = models.CharField(max_length=255)
    description = models.TextField()
    responsibilities = models.TextField()

    group_members = models.ManyToManyField(
        Member, through='GroupMembership', through_fields=('group', 'member'),)

    established_on = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class GroupMembership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)


# class Ministry(models.Model):
#     id = models.AutoField(primary_key=True)
#     ministry_name = models.CharField(max_length=255)
#     description = models.TextField()
#     leader = models.CharField(max_length=255)

#     ministry_members = models.ManyToManyField(
#         Member, through='MinistryMembership', through_fields=('ministry', 'member'),)

#     def __str__(self):
#         return self.ministry_name


# class MinistryMembership(models.Model):
#     id = models.AutoField(primary_key=True)
#     ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
#     member = models.ForeignKey(Member, on_delete=models.CASCADE)


# class Committee(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     leader = models.CharField(max_length=255)

#     committee_members = models.ManyToManyField(
#         Member, through='CommitteeMembership', through_fields=('committee', 'member'),)

#     description = models.TextField()
#     responsibilities = models.TextField()
#     designated_lifespan = models.DateField()

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# class CommitteeMembership(models.Model):
#     id = models.AutoField(primary_key=True)
#     committee = models.ForeignKey(Committee, on_delete=models.CASCADE)
#     member = models.ForeignKey(Member, on_delete=models.CASCADE)
#     # member = models.ManyToManyField(self, on_delete=models.CASCADE)


class Committee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    leader = models.CharField(max_length=255)

    committee_members = models.ManyToManyField(Member)

    description = models.TextField()
    responsibilities = models.TextField()
    designated_lifespan = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

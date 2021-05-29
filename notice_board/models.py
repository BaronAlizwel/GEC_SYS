from django.db import models
from members.models import *

# Create your models here.


class NotificationMessage(models.Model):
    id = models.AutoField(primary_key=True)
    member_ID = models.ForeignKey(Member, on_delete=models.CASCADE)
    # audience_group = models.ForeignKey(Choices=Group, on_delete=models.CASCADE)
    # audience_ministry = models.ForeignKey(
    #     Choices=Ministry, on_delete=models.CASCADE)

    audience_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    audience_ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Sugession(models.Model):
    id = models.AutoField(primary_key=True)
    member_ID = models.ForeignKey(Member, on_delete=models.CASCADE)
    segession_message = models.TextField()
    # feedback = models.TextField()
    # feedback = models.ForeignKey(SugessionFeedback, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class SugessionFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    member_ID = models.ForeignKey(Member, on_delete=models.CASCADE)
    # segession_message = models.TextField()
    segession_message = models.ForeignKey(Sugession, on_delete=models.CASCADE)
    sugession_feedback_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Complaint(models.Model):
    id = models.AutoField(primary_key=True)
    member_ID = models.ForeignKey(Member, on_delete=models.CASCADE)
    complaint_message = models.TextField()
    audience_ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    audience_ministry = models.ForeignKey(Group, on_delete=models.CASCADE)
    # audience_ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    # feedback = models.TextField()
    # feedback = models.ForeignKey(ComplaintFeedback, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class ComplaintFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    member_ID = models.ForeignKey(Member, on_delete=models.CASCADE)
    complaint_message = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    complaint_feedback_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

from django.contrib import admin
from notice_board.models import Complaint, Sugession, NotificationMessage, ComplaintFeedback, SugessionFeedback

# Register your models here.

# admin.site.register(FeedBack)
admin.site.register(Complaint)
admin.site.register(Sugession)
admin.site.register(NotificationMessage)
admin.site.register(ComplaintFeedback)
admin.site.register(SugessionFeedback)

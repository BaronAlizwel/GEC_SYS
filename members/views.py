from django.shortcuts import render
from django.views.generic import ListView
from members.models import Member, Shepherd, Group, Ministry

# Create your views here.


class MemberListView(ListView):
    model = Member
    # template_name = 'members/list.html'

    context_object_name = 'members'

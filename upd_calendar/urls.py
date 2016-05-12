from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /updcalendar/
    url(r'^$', views.draw_calendar, name='draw_calendar'),
    # ex: /updcalendar/update/kb555999
    url(
        r'^update/(?P<update_id>[kb0-9]+)/$',
        views.update_detail, name='update_detail'
    ),
    # ex: /updcalendar/event/1
    url(
        r'^event/(?P<event_date>)/$',
        views.event_detail, name='event_detail'
    ),
]

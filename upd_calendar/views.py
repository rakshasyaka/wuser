# from django.shortcuts import render
import datetime
from datetime import date
import calendar
# from django.http import HttpResponse
from .models import Event, Update
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied


# пригодиццо
def check_access_rights(request):
    if request.user.have_access or request.user.is_staff:
        return request
    raise PermissionDenied


# in this we are take all events from model where month eq current month
def event_list():
    return Event.objects.all()


# here we taked list of updates whos refer to the event
def update_list(event):
    pass


def update_detail(request):
    pass


# TODO: WARNING! TEST! event_detail and redirect_to_event MUST be remaked!
def event_detail(request, event_date):
    r_events = str(event_date)
    # events = Event.objects.filter(date=event_date)
    q_events = get_object_or_404(Event, date=event_date)
    if q_events is not list:
        events = []
        events.append(q_events)
    else:
        events = q_events
    context = {
        'r_events': r_events,
        'events': events
    }
    return render(request, 'upd_calendar/event.html', context)


def redirect_to_event(request):
    event_date = '7/5/2016'
    return HttpResponseRedirect(reverse('event_detail', args=(event_date,)))


def single_event(inp_date):
    if type(inp_date) is not date:
        try:
            dd, mm, yy = map(int, inp_date.split('/'))
        except:
            return "Not a valid date come"
    two_weeks = datetime.timedelta(weeks=2)
    old_date = inp_date - two_weeks
    s_event = Event.objects.filter(
        date__lte=inp_date).filter(date__gt=old_date)
    return s_event


# get all dates and add to list where month eq current month
# it smells bad
# TODO: rebuild this
def ev_date_list(q_month):
    q_month = int(q_month)
    ev_date_list = []
    for event in Event.objects.dates("date", "day"):
        if event.month == q_month:
            ev_date_list.append(event)
    return ev_date_list


# put calendar on screen
def draw_calendar(request):
    today = date.today()
    calend = calendar.Calendar()
    monthes = {
        1: "Январь", 2: "Февраль", 3: "Март",
        4: "Апрель", 5: "Май", 6: "Июнь",
        7: "Июль", 8: "Август", 9: "Сентябрь",
        10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"
    }
    today_m = monthes[today.month]
    month_cal = calend.monthdatescalendar(
        month=today.month,
        year=today.year
    )
    show_events = single_event(today)
    ev_dates = ev_date_list(today.month)
    context = {
        'month_cal': month_cal,
        'today_m': today_m,
        'today': today,
        'show_events': show_events,
        'ev_dates': ev_dates,
    }
    return render(request, 'upd_calendar/upd_calendar.html', context)

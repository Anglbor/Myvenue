from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Meet, MyUsers, Venue
from .forms import VenueForm, MeetForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import csv
# File PDF needed imports
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# pagination imports
from django.core.paginator import Paginator




def venue_pdf(request):
    #create bytestream buffer
    bufr = io.BytesIO()
    # create canvas
    can = canvas.Canvas(bufr, pagesize=letter, bottomup=0)
    # create takst object
    textobject = can.beginText()
    textobject.setTextOrigin(inch, inch)
    textobject.setFont('Helvetica', 12)

    # #adding some lines
    # lines = ['klkkok'
    #          'jkllp']

    # for line in lines:
    #     textobject.textLine(line)


    # venues from model
    venues = Venue.objects.all()
    lines =[]
    for venue in venues:
        lines.append(f'Venue name : {venue.name}')
        lines.append(f'Venue address : {venue.address}')
        lines.append(f'Zip code : {venue.zip_code}')
        lines.append(f'Phone : {venue.phone}')
        lines.append(f'Web : {venue.web}')
        lines.append(f'Email : {venue.email}')
        lines.append(' ')

    for line in lines:
        textobject.textLine(line)

    # finishing creating
    can.drawText(textobject)
    can.showPage()
    can.save()
    bufr.seek(0)

    return FileResponse(bufr, as_attachment=True, filename='venue.pdf')



def venue_csv(request):
    responce = HttpResponse(content_type='csv/plain')
    responce['Content-Disposition'] = 'attachment; filename = venues.csv'

    # creating writer

    writer = csv.writer(responce)

    # add columns
    writer.writerow(['Venue name', 'Address', 'Zip Code ', 'Phone', 'Web', 'Email'])

    venues = Venue.objects.all()
    for venue in venues:
        writer.writerow([venue.name, venue.address, venue.zip_code, venue.phone, venue.web, venue.email])

    return responce


# create tekst file
def venue_tekst(request):
    responce = HttpResponse(content_type='tekst/plain')
    responce['Content-Disposition'] = 'attachment; filename = venues.txt'
    # lines = ['klkkok \n'
    #          'jkllp']

    lines =[]

    venues = Venue.objects.all()
    for venue in venues:
        lines.append(f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n{venue.email}\n\n\n\n')

    responce.writelines(lines)
    return responce


def delete_meet(request, meet_id):
    meet = Meet.objects.get(pk=meet_id)
    meet.delete()
    return redirect('meets')

def update_meet(request, meet_id):
    meet = Meet.objects.get(pk=meet_id)
    form = MeetForm(request.POST or None, instance=meet)
    if form.is_valid():
        form.save()
        return redirect('meets')

    ctx = {'meet': meet,
           'form': form}
    return render(request, 'meet_app/update_meet.html', ctx)

def add_meet(request):
    submitted = False
    if request.method == 'POST':
        form = MeetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_meet?submitted=True')

    else:
        form = MeetForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'meet_app/add_meet.html', {'submitted': submitted, 'form': form})


def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('venues_all')


def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('venues_all')

    ctx = {'venue': venue,
           'form': form}
    return render(request, 'meet_app/update_venue.html', ctx)

def search_venues(request):
    if request.method == 'POST':
        searched_venue = request.POST['searched_venue']
        venues = Venue.objects.filter(name__contains=searched_venue)
        return render(request, 'meet_app/search_venues.html', {'searched_venue': searched_venue,
                                                               'venues': venues})
    else:
        return render(request, 'meet_app/search_venues.html')

def venue_show(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    ctx = {'venue': venue}
    return render(request, 'meet_app/venue_show.html', ctx)

def venues_all(request):
    # venue_list = Venue.objects.all().order_by('name')
    # order.by('?')
    venue_list = Venue.objects.all()
    # order.by('?')

    # setup pagination
    pg = Paginator(Venue.objects.all(), 2)
    page = request.GET.get('page')
    venues = pg.get_page(page)

    ctx = {'venue_list': venue_list,
           'venues': venues}
    return render(request, 'meet_app/venue_list.html', ctx)


def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')

    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'meet_app/add_venue.html', {'submitted': submitted, 'form': form})


def meets_all(request):
    meet_list = Meet.objects.all().order_by('meet_date')
    ctx = {'meet_list': meet_list}
    return render(request, 'meet_app/meets_list.html', ctx)


def home(request, month=datetime.now().strftime('%B'), year=datetime.now().year):
    name ='Anna'
    month = month.title()
    # convert string to number
    month_number = list(calendar.month_name).index(month)
    month_number =int(month_number)

    calen = HTMLCalendar().formatmonth(year, month_number)

    now = datetime.now()
    year_now = now.year
    time =now.strftime('%I:%M:%p')

    return render(request, 'meet_app/home.html',
                  {'month': month,
                   'year': year,
                   'name': name,
                   'month_number': month_number,
                   'calen': calen,
                   'year_now': year_now,
                   'time': time})

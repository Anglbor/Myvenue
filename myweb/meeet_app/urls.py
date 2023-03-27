from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('meets', views.meets_all, name="meets"),
    path('add_venue', views.add_venue, name='add_venue'),
    path('venues_all', views.venues_all, name='venues_all'),
    path('venue_show/<venue_id>', views.venue_show, name='venue_show'),
    path('search_venues', views.search_venues, name='search_venues'),
    path('update_venue/<venue_id>', views.update_venue, name='update_venue'),
    path('add_meet', views.add_meet, name='add_meet'),
    path('update_meet/<meet_id>', views.update_meet, name='update_meet'),
    path('delete_meet/<meet_id>', views.delete_meet, name='delete_meet'),
    path('delete_venue/<venue_id>', views.delete_venue, name='delete_venue'),
    path('venue_tekst', views.venue_tekst, name='venue_tekst'),
    path('venue_csv', views.venue_csv, name='venue_csv'),
    path('venue_pdf', views.venue_pdf, name='venue_pdf'),


]

from django.shortcuts import render, redirect
# from .models import Category, Item
from .models import *
from datetime import date, timedelta  # Add this line to import the 'date' class
# from .forms import ReservationForm

# Create your views here.

def home(request):
    return render(request,'home.html');

def appetizer(request):
    # Assuming 'Appetizer' is the name of the appetizer category
    appetizer_category = Category.objects.get(name='Appetizer')
    appetizers = Item.objects.filter(category=appetizer_category)
    return render(request, 'appetizer.html', {'appetizers': appetizers})

def management(request):
    return render(request,'management.html')

def orders(request):
    return render(request,'orders.html')

def bookings(request):
    return render(request,'bookings.html')

def staff(request):
    employees = Employee.objects.all()
    context = {'employees': employees}

    return render(request,'staff.html', context)

def timetable(request):
    return render(request,'timetable.html')


def timetable(request):
    # Retrieve duties for the current day (you can customize this based on your requirements)
    current_day_duties = DailyDuty.objects.filter(day=date.today())

     # Delete entries older than the current day
    older_than_today = date.today() - timedelta(days=1)
    DailyDuty.objects.filter(day__lt=older_than_today).delete()

    context = {
        'current_day_duties': current_day_duties,
    }

    return render(request, 'timetable.html', context)


# def reservation_page(request):
#     available_dates = Reservation.objects.values_list('available_dates', flat=True)
    
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('reservation_success')  # Redirect to a success page
#     else:
#         form = ReservationForm()

#     return render(request, 'tableReservation.html', {'form': form, 'available_dates': available_dates})


def reservation_form(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
#     #     email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        number_of_guests = request.POST.get('number_of_guests')
        special_request = request.POST.get('special_request')
        reservation_date = request.POST.get('reservation_date')
#     # # now we save the data to the database
        reservation = Reservation(customer_name=customer_name, reservation_date=reservation_date, phone_number=phone_number, number_of_guests=number_of_guests, special_request=special_request)
        reservation.save()
        
#         return redirect('reservation_success')
#     #     # Perform any necessary validation or processing here
#     #     # For simplicity, you can directly save to the database or perform other actions

#     #     # Redirect to a success page or render a thank you message
#     #     # return redirect('custom_reservation_success')
    
    return render(request, 'tableReservation.html')

def reservation_success(request):
    return render(request,'reservation_success.html')

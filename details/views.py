from django.shortcuts import render, redirect, get_object_or_404
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

def main(request):
    main_category = Category.objects.get(name='Main')
    mainDish = Item.objects.filter(category=main_category)

    return render(request,'mainCourse.html',{'mainDish':mainDish})

def dessert(request):
    dessert_category = Category.objects.get(name='Dessert')
    dessertDish = Item.objects.filter(category=dessert_category)

    return render(request,'dessert.html',{'dessertDish':dessertDish})

def management(request):
    return render(request,'management.html')

def orders(request):
    return render(request,'orders.html')

def bookings(request):
    reservations = Reservation.objects.all()

    return render(request,'bookings.html',{'reservations': reservations})

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
    reservations = None  # Initialize the variable outside of the conditional block
    
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        number_of_guests = request.POST.get('number_of_guests')
        special_request = request.POST.get('special_request')
        reservation_date = request.POST.get('reservation_date')
#     # # now we save the data to the database
        # reservation = Reservation(customer_name=customer_name, reservation_date=reservation_date, phone_number=phone_number, number_of_guests=number_of_guests, special_request=special_request, email=email)
        # reservation.save()
          # Create a new Reservation object
        reservation = Reservation.objects.create(
            customer_name=customer_name,
            reservation_date=reservation_date,
            phone_number=phone_number,
            number_of_guests=number_of_guests,
            special_request=special_request,
            email=email
        )

        # Fetch all reservations from the database
        # reservations = Reservation.objects.all()
        

        # Fetch all reservations from the database and at the end of this function pass it there
    # reservations = reservation.objects.all()
        
#         return redirect('reservation_success')
#     #     # Perform any necessary validation or processing here
#     #     # For simplicity, you can directly save to the database or perform other actions

#     #     # Redirect to a success page or render a thank you message
#     #     # return redirect('custom_reservation_success')
    
    return render(request, 'tableReservation.html', {'reservations': reservations})




def reservation_success(request):
    return render(request,'reservation_success.html')


def policies(request):
    return render(request,'policies.html')


def feedback(request):
    if request.method == 'POST':
        # Process form data when the form is submitted
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')

        feedback_info = Feedback( name=name, email=email, rating=rating, comments=comments)
        feedback_info.save()

        # Perform your custom form validation and processing here
       

        # Process the feedback data (e.g., save to a database)
        # Add your logic here
        # return redirect('success_page')  # Redirect to a success page

    return render(request, 'feedback.html', {'error': None})


def viewFeedback(request):

    feedbacks = Feedback.objects.all()
    
    return render(request,'viewFeedback.html',{'feedbacks':feedbacks})




    # views.py


def show_categories(request):
    categories = Category.objects.all()
    return render(request, 'items.html', {'categories': categories})
    # return render(request, 'categories.html', {'categories': categories})

def show_items(request, category_id=None):
    categories = Category.objects.all()
    selected_category = None
    items = BaseItem.objects.all()

    if category_id:
        selected_category = Category.objects.get(pk=category_id)
        items = BaseItem.objects.filter(category=selected_category)

    return render(request, 'items.html', {'categories': categories, 'items': items, 'selected_category': selected_category})

def show_items_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    items = BaseItem.objects.filter(category=category)
    return render(request, 'items_by_category.html', {'category': category, 'items': items})

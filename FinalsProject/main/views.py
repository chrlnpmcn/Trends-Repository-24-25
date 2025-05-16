from django.shortcuts import render

def homepage(request):
    return render(request, 'home_page.html')

def homepage_with_account(request):
    return render(request, 'home_page_with_account.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def account(request):
    return render(request, 'account.html')

def create_account(request):
    return render(request, 'create_account.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def signin(request):
    return render(request, 'signin.html')

def user_registration(request):
    return render(request, 'user_registration.html')

def registration(request):
    return render(request, 'registration.html')

def showcase_with_account(request):
    return render(request, 'showcase_with_account.html')

def regulations(request):
    return render(request, 'regulations.html')

def maintenance_main(request):
    return render(request, 'maintenance_main.html')

def maintenance_battery(request):
    return render(request, 'maintenance_battery.html')

def maintenance_services(request):
    return render(request, 'maintenance_services.html')

def maintenance_tire(request):
    return render(request, 'maintenance_tire.html')

# Admin-related views
def admin_dashboard(request):
    return render(request, 'admin-dashboard.html')

def admin_content(request):
    return render(request, 'admin-content.html')

def admin_logout(request):
    return render(request, 'admin-logout.html')

def admin_registrations(request):
    return render(request, 'admin-registrations.html')

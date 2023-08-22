from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
def index(request):
    if request.method == 'POST':
        # Get the form data
        email = request.POST.get('email')
        password = request.POST.get('psw')
        
        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            return redirect('main')  # Redirect to the main page after successful login
        else:
            # Authentication failed
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')
def main(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render({},request))
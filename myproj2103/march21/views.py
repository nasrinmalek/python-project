from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
def index(request):
	return render(request, 'index.html')
	#return HttpResponse('India is a grate country')
def register(request):
	return render(request, 'register.html')
	
def customerlist(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		contact = request.POST.get('contact')
		address = request.POST.get('address')

		# Create a dictionary for the current data entry
		data_entry = {'name': name, 'email': email, 'contact': contact, 'address': address}
        
        # Get the existing data list from the session, or create a new one if it doesn't exist
		data_list = request.session.get('data_list', [])
        
        # Append the current data entry to the data list
		data_list.append(data_entry)
        
        # Store the updated data list back into the session
		request.session['data_list'] = data_list
        
        # Render the display template with the collected data list
		return render(request, 'customerlist.html', {'data_list': data_list})
	else:
        # If request method is not POST, render the register form
		return render(request,'register.html')
	
	


	

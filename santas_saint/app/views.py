# backend/app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Child, BehaviorData

def dashboard(request):
    """Render the dashboard with a list of all children."""
    children = Child.objects.all()
    return render(request, 'dashboard.html', {'children': children})

def submit_behavior(request):
    """Handle behavior submissions for a child."""
    if request.method == "POST":
        child_id = request.POST.get('child_id')  # Use .get() for safe access
        description = request.POST.get('description')

        # Validate input
        if not child_id or not description:
            return render(request, 'error.html', {'message': 'Invalid data submitted.'})

        # Get the child or return a 404 error if not found
        child = get_object_or_404(Child, id=child_id)
        
        # Create a new behavior record
        BehaviorData.objects.create(child=child, description=description)

        # Redirect to the dashboard after successful submission
        return redirect('dashboard')
    
    return render(request, 'submit_behavior.html')  # Add a form template if needed

def appeal_status(request, child_id):
    """Placeholder for handling child status appeals."""
    child = get_object_or_404(Child, id=child_id)
    
    # Implement appeal logic here
    return render(request, 'appeal_status.html', {'child': child})

def add_child(request):
    """Handle adding a new child."""
    if request.method == "POST":
        name = request.POST.get('name')
        status = request.POST.get('status')

        # Validate input
        if not name or not status:
            return render(request, 'error.html', {'message': 'Please provide both name and status.'})

        # Create a new Child object
        Child.objects.create(name=name, status=status)

        # Redirect to the dashboard after successful addition
        return redirect('dashboard')

    return render(request, 'add_child.html')  # Render the add child form

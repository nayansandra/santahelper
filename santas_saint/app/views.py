
from django.shortcuts import render, redirect
from .models import Child, BehaviorData

def dashboard(request):
    children = Child.objects.all()
    return render(request, 'dashboard.html', {'children': children})

def submit_behavior(request):
    if request.method == "POST":
        child_id = request.POST['child_id']
        description = request.POST['description']
        child = Child.objects.get(id=child_id)
        BehaviorData.objects.create(child=child, description=description)
        # Update score logic can be added here.
        return redirect('dashboard')

def appeal_status(request, child_id):
    # Logic for appealing status can be implemented here.
    pass

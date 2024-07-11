from django.shortcuts import render 
from .forms import UnitConversionForm


def unit_conversion(request):
    # Post request so data must be processed
    if request.method == "POST":
        # Creata a form instance and populate it with data from the request:
        form = UnitConversionForm(request.POST)
        # Check if it's valid
        if form.is_valid():
            # Process the data in form.cleaned_data as required. What does this mean?
        
           ...
    else:
        form = UnitConversionForm()

    return render(request, "unit_conversion.html", {"form": form})

def views(request):
    if request.method == 'POST':
        form = UnitConversionForm(request.POST)
        if form.is_valid():
            value_in = form.cleaned_data['value_in']
            units_from = form.cleaned_data['units_from']
            units_to = form.cleaned_data['units_to']
            value_out = form.cleaned_data['value_out']
    else:
        form = UnitConversionForm()
        
    return render(request, 'unit_conversion.html', {'form': form})
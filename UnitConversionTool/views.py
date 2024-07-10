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
            # Redirect to a new url. ??
           ...
    else:
        form = UnitConversionForm()

    return render(request, "unit_conversion.html", {"form": form})
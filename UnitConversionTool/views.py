from django.shortcuts import render 
from .forms import UnitConversionForm
from .convert import convert


def unit_conversion(request):    
    value_out = None  
                                  
    if request.method == 'POST':
        form = UnitConversionForm(request.POST)
        if form.is_valid():
            value_in = form.cleaned_data['value_in']
            units_from = form.cleaned_data['units_from']
            units_to = form.cleaned_data['units_to']
            value_out = convert(value_in, units_from, units_to)
        else:
            print(form.errors)
    else:
        form = UnitConversionForm()
    
    context = {
        'form': form, 
        'value_out': value_out,
    }
    return render(request, 'unit_conversion.html', context)


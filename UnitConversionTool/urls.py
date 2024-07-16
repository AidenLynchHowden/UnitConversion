"""
URL configuration for UnitConversionTool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    # defined unit_conversion here, but it isn't highlighted. 
    unit_conversion,
    update_unit_choices,
)

app_name = 'UnitConversionTool'
urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='unit/conversion/', view=unit_conversion, name='unit_conversion'),
    path(route='update/unit/choices/', view=update_unit_choices, name='update_unit_choices'),
]

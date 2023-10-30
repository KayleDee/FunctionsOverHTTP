from django.contrib import admin
from django.urls import path

from app.views import hey_you, how_old, can_i_take_your_order

urlpatterns = [
    path('order-total/<int:burgers>/<int:fries>/<int:drinks>',can_i_take_your_order),
    path('age-in/<int:end>/<int:birthyear>', how_old),
    path('hey/<name>', hey_you),
    path('admin/', admin.site.urls),
]
 
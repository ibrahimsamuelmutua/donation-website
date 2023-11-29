from django.urls import path
from . import views as sam

urlpatterns = [
    path('add_event/', sam.add_event, name='add-event-url'),
    path('donate/', sam.donate, name='donate-url'),
    path('update_events/<int:id>/', sam.update_event, name='update-event-url'),
    path('delete/<int:id>/', sam.delete_event, name='delete-url'),
    path('pay/<int:id>/', sam.pay, name='pay-url'),
    path('pay2/', sam.pay_option2, name='pay2-url')

]

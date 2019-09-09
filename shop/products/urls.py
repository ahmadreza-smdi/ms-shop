from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'buy.',views.buy_product),
    url(r'',views.show_product),

]

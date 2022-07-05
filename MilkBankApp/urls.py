from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('index',views.index),
    path('changepass', views.changepass),

    path('donar_register',views.donar_register),
    path('donar_today_collect',views.donar_today_collect),
    path('donar_mini_statement',views.donar_mini_statement),
    path('donar_detail_statement',views.donar_detail_statement),

    path('own_mother_register', views.own_mother_register),
    path('own_to_donar',views.own_to_donar),
    path('own_today_collect',views.own_today_collect),
    path('own_mini_statement',views.own_mini_statement),
    path('own_detail_statement',views.own_detail_statement),

    path('pasturization',views.pasturization),
    path('past_today_collect',views.past_today_collect),
    path('past_mini_statement',views.past_mini_statement),
    path('past_detail_statement',views.past_detail_statement),

    path('culture',views.culture),
    path('culture_today_collect',views.culture_today_collect),
    path('culture_mini_statement',views.culture_mini_statement),
    path('culture_detail_statement',views.culture_detail_statement),

    path('discard', views.discard),
    path('discard_today_collect', views.discard_today_collect),
    path('discard_mini_statement', views.discard_mini_statement),
    path('discard_detail_statement', views.discard_detail_statement),

    path('dispense', views.dispense),
    path('dispense_today_collect', views.dispense_today_collect),
    path('dispense_mini_statement', views.dispense_mini_statement),
    path('dispense_detail_statement', views.dispense_detail_statement),

]
from django.contrib import admin
from django.urls import path, include
from tickets import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('guests', views.viewsets_guest)
router.register('movie', views.viewsets_movie)
router.register('reservations', views.viewsets_reservation)

urlpatterns = [
    path('admin/', admin.site.urls),

    #First Way 
    path('django/jsonresponsenomodel/', views.no_rest_no_model),

    #Secound Way
    path('django/jsonresponsefrommodel/', views.no_rest_from_model),

    # 3.1TH
    path('rest/fbv/', views.FBV_List),

    # 3.2TH
    path('rest/fbv/<int:pk>', views.FBV_pk),

    # 4.1 
    path('rest/cbv/', views.CBV_List.as_view()),

    #4.2
    path('rest/cbv/<int:pk>', views.CBV_pk.as_view()),

    #5.1
    path('rest/mixins/', views.mixins_list.as_view()),

    #5.2
    path('rest/mixins/<int:pk>', views.mixins_pk.as_view()),

    #6.1
    path('rest/generics/', views.generics_list.as_view()),

    #6.2
    path('rest/generics/<int:pk>', views.generics_pk.as_view()),

    #7
    path('rest/viewsets/', include(router.urls)),

    # 8 finde movie
    path('rest/fbv/findemovie', views.finde_movie),

    #9 new reservation
    path('rest/fbv/newreservation', views.new_reservation)

]

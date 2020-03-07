from . import views
from django.urls import path, include,re_path
from rest_framework_nested import routers
router = routers.SimpleRouter()
router.register(r'schools', views.StudentschoolViewSet)

school_router = routers.NestedSimpleRouter(router,r'schools', lookup='school')
school_router.register(r'students', views.StudentschoolViewSet)





urlpatterns = [
    path('students/',views.StudentdetailViewSet.as_view({'get': 'list', 'post':'create'}),name='students'), #for getting all student object
    path('schools/',views.SchooldetailViewSet.as_view({'get': 'list', 'post':'create'}),name='school'),  #for getting all school object
    re_path(r'^students/(?P<id>\d+)/$',views.StudentViewSet.as_view({'get':'list','put': 'update','patch': 'partial_update', # for getting the particular student
    'delete': 'destroy'})),
    re_path(r'^schools/(?P<id>\d+)/$',views.SchoolViewSet.as_view({'get':'list','put': 'update','patch': 'partial_update',  # for getting the particular school
    'delete': 'destroy'}))
    ]

urlpatterns += router.urls
urlpatterns +=school_router.urls

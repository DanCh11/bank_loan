from django.urls import path, include
from rest_framework import routers
from rest_framework import views
from .views import myform, approve_reject, ApprovalsView

router = routers.DefaultRouter()
router.register('loanAPI', ApprovalsView)

urlpatterns = [
    path('form/', myform, name='myform'),
    path('', include(router.urls)),
    path('status/', approve_reject)
]
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import *


app_name = "app"
router = routers.DefaultRouter()
router.register('object', Object_v)
router.register('position', Position_v)
router.register('mode', Mode_v)
router.register('call_status', Call_Status_v)
router.register('call_type', Call_Type_v)
router.register('type_chp', Type_ChP_v)
router.register('status_chp', Status_ChP_v)
router.register('period', Period_v)
router.register('plan', Plan_v)
router.register('plan_raw', Plan_raw_v)
router.register('tick_chp', Tick_ChP_v)
router.register('close_chp', Close_ChP_v)
router.register('call', Call_v)
router.register('employee', Employee_v)
#router.register('verify', Verify)

urlpatterns = [
    path('app/verify', Verify2.as_view()),
    path('app/today', Today.as_view()),
    path('app/enter_to_job', Enter_to_job.as_view()),    
    path('app/this_day', This_day.as_view()),
    path('app/', include(router.urls)),
]

#router.register('app/v', Verify2.as_view(), basename='v')
#urlpatterns = router.urls
#urlpatterns = [
#   path('app/v', Verify.as_view())]

#urlpatterns = router.urls
# app_name will help us do a reverse look-up latter.
#urlpatterns = [
#    path('app/', TickView2.as_view()),
#    path('app/employee/verify', Verify.as_view()),
#    path('app/employee', Employee_v.as_view()),
#    path('app/object', Object_v),
#    path('app/position', Position_v.as_view()),
#    path('app/mode', Mode_v.as_view()),
#    path('app/call_status', Call_Status_v.as_view()),
#    path('app/call_type', Call_Type_v.as_view()),
#    path('app/type_chp', Type_ChP_v.as_view()),
#    path('app/status_chp', Status_ChP_v.as_view()),
#    path('app/Period', Period_v.as_view()),
#    path('app/plan', Plan_v.as_view()),
#    path('app/plan_raw', Plan_raw_v.as_view()),
#    path('app/tick_chp', Tick_ChP_v.as_view()),
#    path('app/close_chp', Close_ChP_v.as_view()),
#    path('app/call', Call_v.as_view())
#    

#]

from django.contrib import admin
from payments.views import signin, signup, signout, create_groups, groups_payout, settings, delete_task, task_detail
from expenses.views import create_payout, delete_payout, complete_payout
from .views import go_index
from django.urls import path, include

urlpatterns = [
    path('', go_index, name='index'),
    path('admin/', admin.site.urls),
    path('signin/', signin),
    path('signup/', signup),
    path('logout/', signout),
    path('create_groups/<str:pk>', create_groups, name="create_groups"),
    path('update-user/', settings, name="update_user"),
    
    path('delete_groups/<int:pk>', delete_task, name="delete_groups"),
    path('groups/', groups_payout, name="groups"),
    path('payouts/<int:pk>', create_payout, name="payouts"),
    path('edit/<int:task_id>', task_detail, name="edit"),
    path('delete_payouts/<str:id_group>/<int:pk>', delete_payout, name="delete_payouts"),
    path('complete_payouts/<str:id_group>/<int:pk>', complete_payout, name="complete_payouts"),
]

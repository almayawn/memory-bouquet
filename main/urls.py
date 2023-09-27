from django.urls import path
from main.views import show_main, create_entry, show_xml, show_json, show_xml_by_id, show_json_by_id 
from main.views import register, login_user, logout_user
from main.views import increment_flower_amount, decrement_flower_amount, delete_flower

app_name = 'main'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', show_main, name='show_main'),
    path('create-entry', create_entry, name='create_entry'),
    path('int-flower/<int:pk_id>/', increment_flower_amount, name='inc_flower'),
    path('dec-flower/<int:pk_id>/', decrement_flower_amount, name='dec_flower'),
    path('del-flower/<int:pk_id>/', delete_flower, name='del_flower'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]
from django.urls import path

from freebo.views import base_views, freewriting_views, replying_views

app_name = 'freebo'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:freewriting_id>/', base_views.detail, name='detail'),

    # freewriting_views.py
    path('freewriting/create', freewriting_views.freewriting_create, name='freewriting_create'),
    path('freewriting/modify/<int:freewriting_id>/', freewriting_views.freewriting_modify, name='freewriting_modify'),
    path('freewriting/delete/<int:freewriting_id>/', freewriting_views.freewriting_delete, name='freewriting_delete'),

    # replying_views.py
    path('replying/create/<int:freewriting_id>/', replying_views.replying_create, name='replying_create'),
    path('replying/modify/<int:replying_id>/', replying_views.replying_modify, name='replying_modify'),
    path('replying/delete/<int:replying_id>/', replying_views.replying_delete, name='replying_delete'),

    ]

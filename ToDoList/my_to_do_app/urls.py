from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    path('', views.index, name='index'),
    path('createTodo/', views.createTodo, name='createTodo'),
    path('finishTodo/', views.finishTodo, name='finishTodo'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

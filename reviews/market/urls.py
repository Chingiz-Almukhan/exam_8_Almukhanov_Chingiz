from django.urls import path

from market.views.base import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    # path('task/<int:pk>', TaskView.as_view(), name='task'),
    # path('add/<int:pk>', AddView.as_view(), name='add'),
    # path('edit/<int:pk>', EditView.as_view(), name='edit'),
    # path('delete/confirm/<int:pk>', Delete.as_view(), name='delete'),
    # path('projects/', ProjectView.as_view(), name='projects'),
    # path('project/<int:pk>', ProjectDetailView.as_view(), name='project'),
    # path('add/project', AddProjectView.as_view(), name='add_project'),
    # path('edit/user/<int:pk>', EditUserView.as_view(), name='edit_user'),
    # path('delete/project/<int:pk>', DeleteProjectView.as_view(), name='delete_project'),
    # path('edit/project/<int:pk>', EditProjectView.as_view(), name='edit_project')
]

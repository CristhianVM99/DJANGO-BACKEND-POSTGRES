from django.urls import path
from . import views

urlpatterns = [
    ### ROUTER ALL ####
    path('users/', views.getUsers, name='users-all'),
    path('boards/', views.getBoards, name='boards-all'),
    path('lists/', views.getLists, name='lists-all'),
    path('tasks/', views.getTasks, name='tasks-all'),
    ### ROUTER GET ####
    path('user/<str:id>', views.getUser, name='user-find'),
    path('board/<str:id>', views.getBoard, name='board-find'),
    path('list/<str:id>', views.getList, name='list-find'),
    path('task/<str:id>', views.getTask, name='task-find'),
    ### ROUTER CREATE ####
    path('createUser/', views.addUser, name='user-create'),
    path('createBoard/', views.addBoard, name='board-create'),
    path('createList/', views.addList, name='list-create'),
    path('createTask/', views.addTask, name='task-create'),
    ### ROUTER UPDATE ####
    path('updateUser/<str:id>', views.updateUser, name='user-update'),
    path('updateBoard/<str:id>', views.updateBoard, name='board-update'),
    path('updateList/<str:id>', views.updateList, name='list-update'),
    path('updateTask/<str:id>', views.updateTask, name='task-update'),
    ### ROUTER DELETE ####
    path('deleteUser/<str:id>', views.deleteUser, name='user-delete'),
    path('deleteBoard/<str:id>', views.deleteBoard, name='board-delete'),
    path('deleteList/<str:id>', views.deleteList, name='list-delete'),
    path('deleteTask/<str:id>', views.deleteTask, name='task-delete'),    
]

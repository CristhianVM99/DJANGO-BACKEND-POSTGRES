from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import UserModel,BoardModel,ListModel,TaskModel
from .serializer import UserSerializer,BoardSerializer,ListSerializer,TaskSerializer
from django.core.cache import cache

###============== VIEWS USERS ================###

@api_view(['GET'])
def getUsers(request):
    key = 'users-all'
    cached_users = cache.get(key)
    if cached_users:
        return Response(cached_users)
    
    users = UserModel.objects.all()
    serializer = UserSerializer(users, many=True)
    
    cache.set(key,serializer.data,timeout=10)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request,id):
    key = f'users-{id}'
    cached_user = cache.get(key)
    if cached_user:
        return Response(cached_user)
    
    user = get_object_or_404(UserModel, id=id)
    serializer = UserSerializer(user, many=False)
    
    cache.set(key,serializer.data,timeout=10)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['PUT'])
def updateUser(request,id):
    user = UserModel.objects.get(id=id)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request,id):
    user = UserModel.objects.get(id=id)
    user.delete()
    return Response('User susccessfully deleted!')

###============== VIEWS BOARDS ================###

@api_view(['GET'])
def getBoards(request):
    key = 'boards-all'
    cached_boards = cache.get(key)
    if cached_boards:
        return Response(cached_boards)
    
    boards = BoardModel.objects.all()
    serializer = BoardSerializer(boards,many=True)
    
    cache.set(key,serializer.data,timeout=10)
    return Response(serializer.data)

@api_view(['GET'])
def getBoard(request,id):
    key = f'board-{id}'
    cached_board = cache.get(key)
    if cached_board:
        return Response(cached_board)
    
    board = get_object_or_404(BoardModel, id=id)
    serializer = BoardSerializer(board, many=False)
    
    cache.set(key,serializer.data,timeout=10)
    return Response(serializer.data)

@api_view(['POST'])
def addBoard(request):
    serializer = BoardSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    print(request.data)

    return Response(serializer.data)

@api_view(['PUT'])
def updateBoard(request,id):
    board = BoardModel.objects.get(id=id)
    serializer = BoardSerializer(instance=board, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteBoard(request,id):
    board = BoardModel.objects.get(id=id)
    board.delete()
    return Response('Board successfully deleted!')

###============== VIEWS LISTS ================###

@api_view(['GET'])
def getLists(request):
    key = 'lists-all'
    cached_lists = cache.get(key)
    if cached_lists:
        return Response(cached_lists)
    
    lists = ListModel.objects.all()
    serializer = ListSerializer(lists, many=True)
    
    cache.set(key,serializer.data,timeout=10)
    return Response(serializer.data)

@api_view(['GET'])
def getList(request,id):
    key = f'list-{id}'
    cached_list = cache.get(key)
    if cached_list:
        return Response(cached_list)
    
    list = get_object_or_404(ListModel, id=id)
    serializer = ListSerializer(list, many=False)
    
    cache.set(key,serializer.data,timeout=10)
    return Response(serializer.data)

@api_view(['POST'])
def addList(request):
    serializer = ListSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def updateList(request,id):
    list = ListModel.objects.get(id=id)
    serializer = ListSerializer(instance=list, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteList(request,id):
    list = ListModel.objects.get(id=id)
    list.delete()
    return Response('List successfully deleted!')

###============== VIEWS TASKS ================###

@api_view(['GET'])
def getTasks(request):
    key = 'tasks-all'
    cached_tasks = cache.get(key)
    if cached_tasks:
        return Response(cached_tasks)
    
    tasks = TaskModel.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    
    cache.set(key,serializer.data,timeout=10)
    return Response(serializer.data)

@api_view(['GET'])
def getTask(request,id):
    key = f'task-{id}'
    cached_task = cache.get(key)
    if cached_task:
        return Response(cached_task)
    
    task = get_object_or_404(TaskModel, id=id)
    serializer = TaskSerializer(task, many=False)
    
    cache.set(key,serializer.data,timeout=10)
    return Response(serializer.data)

@api_view(['POST'])
def addTask(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def updateTask(request,id):
    task = TaskModel.objects.get(id=id)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request,id):
    task = TaskModel.objects.get(id=id)
    task.delete()
    return Response('Task successfully deleted!')

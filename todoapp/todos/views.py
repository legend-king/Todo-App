from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['Get'])
def getData(request):
    items=Todo.objects.all().values()
    return Response(items)

@api_view(['POST'])
def addData(request):
    # serializer = TodoSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    data=request.data
    print(data)
    if 'completed' not in data:
        completed=False
    else:
        completed=data["completed"]
    x=Todo.objects.create(name=data["name"], completed=completed)
    return Response({"id":x.id,"name":x.name, "completed":x.completed})


@api_view(['PUT'])
def updateData(request, id):
    x=Todo.objects.filter(id=id)
    if x:
        data=request.data
        if "name" in data:
            x.update(name=data["name"])
        elif "completed" in data:
            x.update(completed=data["completed"])
        return Response({"id":x[0].id,"name":x[0].name,"completed":x[0].completed})

@api_view(['DELETE'])
def deleteData(request, id):
    x=Todo.objects.filter(id=id).delete()
    if x[0]:
        return Response({"message":"Deleted Successfully"})
    return Response({"message":"Error in deleting"})

# Create your views here.
# class TodoViewSet(viewsets.ModelViewSet):
#     serializer_class = TodoSerializer
#     queryset = Todo.objects.all()
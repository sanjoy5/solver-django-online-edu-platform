from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/room/:id',
    ]

    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def getRoom(request,pk):
    if request.method == 'GET':
        rooms = Room.objects.get(id=pk)
        serializer = RoomSerializer(rooms, many=False)
        return Response(serializer.data)
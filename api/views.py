from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework import status
from .models import Comment, Fav
from .serializers import CommentSerializer, FavSerializer

# Create your views here.

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class FavViewSet(viewsets.ModelViewSet):
    queryset = Fav.objects.all()
    serializer_class = FavSerializer

class FavsCharacterIDListView(views.APIView):
  def get(self, request):
    character_ids = Fav.objects.values_list('character_id', flat=True)
    return Response(character_ids, status=status.HTTP_200_OK)
  
class IsFavView(views.APIView):
  def get(self, request, character_id):
    try:
      fav = Fav.objects.get(character_id=character_id)
      return Response({"is_fav": True}, status=status.HTTP_200_OK)
    except Fav.DoesNotExist:
      return Response({"is_fav": False}, status=status.HTTP_200_OK)


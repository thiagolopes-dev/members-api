from rest_framework import permissions, viewsets
from .models import Member
from .serializers import MemberSerializer, MemberSimpleSerializer
from rest_framework.response import Response

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def list(self, request, *args, **Kwargs):
        queryset = Member.objects.all()
        serializer = MemberSimpleSerializer(queryset, many=True)
        return Response(serializer.data)


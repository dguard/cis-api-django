from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Valute
from .serializers import ValuteSerializer
from .pagination import CustomPagination


class get_valute(RetrieveUpdateDestroyAPIView):
    serializer_class = ValuteSerializer

    def get_queryset(self, pk):
        try:
            valute = Valute.objects.get(pk=pk)
        except Valute.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return valute

    # Get a valute
    def get(self, request, pk):

        valute = self.get_queryset(pk)
        serializer = ValuteSerializer(valute)
        return Response(serializer.data, status=status.HTTP_200_OK)



class get_valutes(ListCreateAPIView):
    serializer_class = ValuteSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
       valutes = Valute.objects.all()
       return valutes

    # Get all valutes
    def get(self, request):
        valutes = self.get_queryset()
        paginate_queryset = self.paginate_queryset(valutes)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)



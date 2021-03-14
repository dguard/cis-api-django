from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Webhook
from .serializers import WebhookSerializer
from .pagination import CustomPagination


class get_delete_update_webhook(RetrieveUpdateDestroyAPIView):
    serializer_class = WebhookSerializer

    def get_queryset(self, pk):
        try:
            webhook = Webhook.objects.get(pk=pk)
        except Webhook.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return webhook

    # Get a webhook
    def get(self, request, pk):
        webhook = self.get_queryset(pk)
        serializer = WebhookSerializer(webhook)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a webhook
    def put(self, request, pk):
        webhook = self.get_queryset(pk)

        serializer = WebhookSerializer(webhook, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Delete a webhook
    def delete(self, request, pk):
        webhook = self.get_queryset(pk)

        webhook.delete()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)


class get_post_webhooks(ListCreateAPIView):
    serializer_class = WebhookSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
       webhooks = Webhook.objects.all()
       return webhooks

    # Get all webhooks
    def get(self, request):
        webhooks = self.get_queryset()
        paginate_queryset = self.paginate_queryset(webhooks)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new webhook
    def post(self, request):
        serializer = WebhookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

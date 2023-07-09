from django.shortcuts import render
from .models import Campaign,Subscriber
# Create your views here.
from rest_framework import generics,response
from .serializers import CampaignSerializer,SubscriberSerializer

class CampaignListAPIView(generics.ListCreateAPIView):
    serializer_class = CampaignSerializer


    def get_queryset(self):
        return Campaign.objects.all()
class CampaignDetailAPIView(generics.GenericAPIView):
    serializer_class = CampaignSerializer
    def get(self, request,slug):

        campaign = Campaign.objects.filter(slug=slug).first()
        if campaign:
         return response.Response(self.serializer_class(campaign).data)
        return response.Response({'message': 'Campaign not found'}, status=404)
class SubscribeToCampaignAPIView(generics.CreateAPIView):
    serializer_class = SubscriberSerializer


    def get_queryset(self):
        return Subscriber.objects.all()


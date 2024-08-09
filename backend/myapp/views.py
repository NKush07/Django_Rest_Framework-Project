from django.shortcuts import render
from .models import Order
from .serializers import OrderSerialzers

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

#Packages for Email Notofication
from django.core.mail import send_mail
from backend.settings import EMAIL_HOST_USER

class OrderView(APIView):
    # GET Method
    def get(self, req):
        try:
            orders = Order.objects.all()
            serializer = OrderSerialzers(orders, many=True)
            return Response({'data': serializer.data, 'message':"Orders data fetched successfully"}, status = status.HTTP_200_OK)
        
        except:
            return Response({'data': {}, 'message':"Somethin  went wrong fetchin the data"}, status = status.HTTP_400_BAD_REQUEST)
       
    # POST Method
    def post(self, req):
        try:
            data = req.data
            
            serializer = OrderSerialzers(data=data)
            
            if serializer.is_valid():
            # Code for Email
                subject = "New Order is Placed"
                message = "Dear Friend" + " " + data["customer_name"] + "this is my first Backend project. Hope this message excites you too."
                c_email = data['email']
                recipient_list = [c_email]
                send_mail(subject, message, EMAIL_HOST_USER, recipient_list, fail_silently=True)
                
                serializer.save()
                return Response({'data': serializer.data, 'message': "New order is created"}, status=status.HTTP_201_CREATED)
            
            else:
                return Response({'data': serializer.errors, 'message': "Something went wrong fetching the data"}, status=status.HTTP_400_BAD_REQUEST)
            
        
        except Exception as e:
            return Response({'data': {}, 'message': "Something went wrong creating order"}, status=status.HTTP_400_BAD_REQUEST)


        
    # PATCH METHOD
    def patch(self, req):
        try: 
            data = req.data
            order = Order.objects.filter(id=data.get('id'))
            
            if not order.exists():
                return Response({'data':{}, 'message':"Order is not found"}, status = status.HTTP_404_NOT_FOUND)
            
            serializer = OrderSerialzers(order[0], data=data, partial=True)
            
            if not serializer.is_valid():
                return Response({'data': serializer.errors, 'message':"Somethin went wron fechin the data"}, status = status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response({'data': serializer.data, 'message':"Order updated successfully"}, status = status.HTTP_200_OK)
        
        except:
            return Response({'data':{}, 'message': "Somethin went wrong with updation"}, status =  status.HTTP_400_BAD_REQUEST)
        
    # DELETE METHOD 
    def delete(self, req):
        try:
            data=req.data
            orders = Order.objects.filter(id=data.get('id'))
            
            if not orders.exists():
                return Response({'data':{}, 'message':"Order is not found"}, status = status.HTTP_404_NOT_FOUND)
            
            orders[0].delete()
            return Response({'data':{}, 'message':"Order deleted succesfully"}, status = status.HTTP_200_OK)
            
        except:
            return Response({'data':{}, 'message': "Something went wrong in deletion of order"}, status = status.HTTP_400_BAD_REQUEST)
            
        
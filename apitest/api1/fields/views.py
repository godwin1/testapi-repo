from django.shortcuts import render
from rest_framework.response import Response
from .serializer import ContactSerializer
from rest_framework.views import APIView
from .models import Contacts
from rest_framework import status

class ContactList(APIView):

	def get(self, request, format=None):
		contacts = Contacts.objects.all()
		serializer = ContactSerializer(contacts, many=True)
		return Response(serializer.data);


	def post(self, request, format=None):
		serializer = ContactSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, statu = status.HTTP_404_BAD_REQUEST)

class ContactDetail(APIView):
	def get_object(self, pk):
		try:
			return Contacts.objects.get(pk=pk)
		except Contacts.DoesNotExist:
			raise Http404
	def get(self, request, pk, format =None):
		contact =  self.get_object(pk)
		serializer = ContactSerializer(contact)
		return Response(serializer.data)

	def put(self, request, pk, format =None):
		contact = self.get_object(pk)
		serializer = ContactSerializer(contact, request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)
	def delete(self, request, pk, format =None):
		contact = self.get_object(pk)
		contact.delete()
		return Response (status = status.HTTP_204_NO_CONTENT)
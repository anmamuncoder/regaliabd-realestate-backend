from rest_framework.generics import CreateAPIView
from .models import Contact
from .serializers import ContactSerializer


class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

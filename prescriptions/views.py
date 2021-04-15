from rest_framework import viewsets, status
from rest_framework.response import Response
from prescriptions.models import Prescription
from . import serializer
from prescriptions.serializer import PrescriptionSerializer
from prescriptions.views_helper import PrescriptionsViewHelper


class PrescriptionsViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    http_method_names = ['post']
    def create(self, request):
        view_helper = PrescriptionsViewHelper()
        formated_request = view_helper.format_post_request(request.data)

        if formated_request:
            serializer = PrescriptionSerializer(data=formated_request)    
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':{'message':'malformed request', 'code': '01'}}, status=status.HTTP_400_BAD_REQUEST)


import logging
from rest_framework import viewsets, status
from rest_framework.response import Response
from prescriptions.models import Prescription
from prescriptions.serializers.serializer import PrescriptionSerializer
from prescriptions.views_helper import PrescriptionsViewHelper

logger = logging.getLogger('api.log')

class PrescriptionsViewSet(viewsets.ModelViewSet):
    http_method_names = ['post']

    def create(self, request):
        view_helper = PrescriptionsViewHelper()
        formated_request = view_helper.format_post_request(request.data)

        if formated_request:
            serializer = PrescriptionSerializer(data=formated_request)    
            if serializer.is_valid():
                serializer.save()
                response = view_helper.format_response(serializer.data)
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                logger.error({'status':status.HTTP_500_INTERNAL_SERVER_ERROR,'request':request.data, 'response': serializer.errors})
                return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            error = {'error':{'message':'malformed request', 'code': '01'}}
            logger.warning({'status':status.HTTP_400_BAD_REQUEST,'request':request.data, 'response': error})
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


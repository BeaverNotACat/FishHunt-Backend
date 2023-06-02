import base64

from rest_framework import status, viewsets
from rest_framework.response import Response

from FishHunt.settings import TEMP_FILE_PATH
from classification.serializers import ValidateRequestSerializer
from classification.neural_model import Model
from fish.models import Fish


class ValidateFishViewSet(viewsets.ViewSet):
    http_method_names = ['post']


    def __init__(self, **kwargs):
        self.neural_model = Model()
        super().__init__(**kwargs)
    

    def create(self, request):
        serializer = ValidateRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        fish = Fish.objects.filter(id=serializer.data['fish_id']).first()
        #For some reason serializer image None
        image = base64.b64decode(request.data['image'])

        with open(TEMP_FILE_PATH, 'wb') as file:
            file.write(image)
            file.close()
        
        try: prediction = self.neural_model.predict_fish_name(image_path=TEMP_FILE_PATH)
        except: return Response({'details': 'Picture cannot be processed'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'result': prediction == fish.model_label})


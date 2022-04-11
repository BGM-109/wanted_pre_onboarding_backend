from django.http import JsonResponse
from .models import Funding
from .serializers import FundingSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def funding_list(request):

    if request.method == 'GET':
        # 모든 펀딩 리스트를 받아서 직렬화 한 뒤 json 으로 반환
        fundings = list(Funding.objects.values())
        serializer = FundingSerializers(fundings, many = True)
        return JsonResponse({"fundings" : serializer.data}, safe=False)

    elif request.method == 'POST':
        serializer = FundingSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)


    
    

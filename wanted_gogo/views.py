from xmlrpc.client import ResponseError
from django.http import JsonResponse
from .models import Funding
from .serializers import FundingSerializers, PutFundingSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def funding_list(request):

    if request.method == 'GET':
        # 모든 펀딩 리스트를 받아서 직렬화 한 뒤 json 으로 반환
        fundings = list(Funding.objects.values())
        serializer = FundingSerializers(fundings, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FundingSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def funding_detail(request, id):

    try:
        funding = Funding.objects.get(pk=id)
    except Funding.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FundingSerializers(funding)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PutFundingSerializers(funding, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'DELETE':
        funding.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else :
        pass
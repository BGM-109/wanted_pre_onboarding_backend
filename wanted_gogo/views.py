from django.http import JsonResponse
from .models import Funding
from .serializers import FundingSerializers

def funding_list(request):
    # 모든 펀딩 리스트를 받아서 직렬화 한 뒤 json 으로 반환
    fundings = list(Funding.objects.values())
    print(fundings)
    serializer = FundingSerializers(fundings, many = True)
    return JsonResponse({"fundings" : serializer.data}, safe=False)

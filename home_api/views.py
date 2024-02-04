from django.http import JsonResponse
from .models import TestItem
from .serializers import TestItemSerializer


def get_items(request):
    items = TestItem.objects.all()
    print(items)
    serializer = TestItemSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False)
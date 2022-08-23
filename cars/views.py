from rest_framework.decorators import api_view

@api_view(['GET'])
def cars_list(request):
    
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from account.api.serializers import RegistrationSerializer, AccountProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

@api_view (['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = "successfull registered a new user"
        data['email'] = account.email
        data['username'] = account.username
        data['f_name'] = account.f_name
        data['l_name'] = account.l_name
        data['pk'] = account.pk
        token = Token.objects.get(user=account).key
        data['token'] = token
    else:
        data = serializer.errors
    return Response(data)

@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
def profile_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountProfileSerializer(account)
        return Response(serializer.data)

@api_view(['PUT',])
@permission_classes((IsAuthenticated, ))
def profile_update_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AccountProfileSerializer(account, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Account updated successfully"
            return Response(data = data)
        return Response(status=status.HTTP_404_NOT_FOUND)     

@api_view(['DELETE',])
def logout_view(request):
    if request.method == 'DELETE':
        request.user.auth_token.delete()
        return Response("Account Logout successfull")
    return Response(status=status.HTTP_404_NOT_FOUND)  
    



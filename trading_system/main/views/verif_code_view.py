from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

class VerifCodeView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get("username")
        code = request.data.get("code",0)
        if isinstance(code, str):
            if code.isdigit():
                code = int(code)
            else:
                return Response({"status":"Code must be numeric"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = get_user_model().objects.get(username=username)
        except get_user_model().DoesNotExist:
            return Response({"status":"Incorrect user"},status=status.HTTP_403_FORBIDDEN)
        if user.verif_code is None or user.is_active:
            return Response({"status":"User already activated"},status=status.HTTP_200_OK)
        if code == user.verif_code.verification_code:
            user.is_active = True
            user.save()
            user.verif_code.delete()
            return Response({"status":"Ok"},status=status.HTTP_200_OK)
        else:
            return Response({"status":"Incorrect code"},status=status.HTTP_403_FORBIDDEN)

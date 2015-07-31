from django.shortcuts import render
from rest_framework.decorators import api_view
from validation.models import RegisterModel
from django.forms.fields import ValidationError
from rest_framework import status
from rest_framework.response import Response
import sys
# Create your views here.


@api_view(('POST',))
def validation(request):
    try:
        data = request.DATA

        test_data = {"telephone": "username", "password": "password"}
        errors = {}
        try:
            r = RegisterModel(**test_data)
            r.full_clean()
        except ValidationError, e:
            errors = e.message_dict
        except:
            print "Unexpected error:", sys.exc_info()[0]
        if len(errors) == 0:
            return Response(request.DATA, status.HTTP_200_OK)
        else:
            return Response(
                    {
                        "message": "can not register user using received data",
                        "errors": errors,
                    },
                    status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"message":"can not register user using received data"},
                        status.HTTP_400_BAD_REQUEST)
import json
from string import digits
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from password_generator import PasswordGenerator



@api_view(['GET', 'POST'])
def generate(request):
    length = 10    

    data = json.loads(json.dumps(request.GET))

 
    try:
        print(data)
        length = int(request.GET.get('length'))

        uppercase = int(request.GET.get('uppercases'))
        lowercase = int(request.GET.get('lowercases'))
        digits = int(request.GET.get('digits'))
        specials  = int(request.GET.get('specials'))

       

    except Exception as e :
        return Response({'error': str(e)})
    

    pwo = PasswordGenerator()
    pwo.minuchars = 2
    pwo.minlchars = 2
    pwo.minnumbers = 2
    pwo.minschars = 2

    pwo.minlen = length # (Optional)
    pwo.maxlen = length # (Optional)
    if uppercase:
        pwo.minuchars = uppercase # (Optional)
    if lowercase:
        pwo.minlchars = lowercase # (Optional)
    if digits:
        pwo.minnumbers = digits # (Optional)
    if specials:
        pwo.minschars = specials # (Optional)

    password = pwo.generate()

    print(password)

    if password:

        return Response({"password": password})


    return Response({"success": "got request , but something went wrong"})

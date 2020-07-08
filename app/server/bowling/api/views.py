import json
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .scoring import Bowling
from .individual_scoring import ScoreBowling

@api_view(['GET', ])
def get_score(request):
    if request.method == 'GET':
        game = Bowling()
        game.get_score()
        result = game.return_data()
        return Response(result)


@api_view(['POST', ])
def get_individual_score(request):
    if request.method == 'POST':
        data = request.data['data']
        game = ScoreBowling()
        game.get_score(data)
        result = game.return_data()
        return Response(result)

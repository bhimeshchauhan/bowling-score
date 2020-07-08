from django.urls import path
from bowling.api.views import (
	get_score,
	get_individual_score,
)


app_name = 'justices_data'

urlpatterns = [
	path('score/', get_score, name="getscore"),
	path('score', get_individual_score, name="getscore"),
]

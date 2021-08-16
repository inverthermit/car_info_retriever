from django.forms.models import model_to_dict
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from info_service.coreapp.models import Car


class CarView(ViewSet):
    def exact_search(self, request):
        self._check_params(["name"], request)
        try:
            car: Car = Car.objects.get(name=request.query_params["name"])
        except ObjectDoesNotExist:
            car = None

        response_data = {"result": model_to_dict(car) if car else None}
        return Response(response_data)

    def term_search(self, request):
        self._check_params(["term"], request)
        cars = list(
            Car.objects.filter(name__icontains=request.query_params["term"])
            .all()
            .values()
        )
        response_data = {"result": cars}
        return Response(response_data)

    def _check_params(self, params, request):
        for param in params:
            if param not in request.query_params:
                raise ValidationError("Missing parameter: " + param)
        return

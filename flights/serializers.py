from rest_framework import serializers
from .models import Country, City, Airport, AirplaneType, Airplane, Crew, Route, Flight, Order, Ticket

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    country_id = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), source="country", write_only=True)
    class Meta:
        model = City
        fields = ["id", "name", "country", "country_id"]

class AirportSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    city_id = serializers.PrimaryKeyRelatedField(queryset=City.objects.all(), source="city", write_only=True)
    class Meta:
        model = Airport
        fields = ["id", "name", "city", "city_id", "closest_big_city"]

class AirplaneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneType
        fields = "__all__"

class AirplaneSerializer(serializers.ModelSerializer):
    airplane_type = AirplaneTypeSerializer(read_only=True)
    airplane_type_id = serializers.PrimaryKeyRelatedField(queryset=AirplaneType.objects.all(), source="airplane_type", write_only=True)
    class Meta:
        model = Airplane
        fields = ["id", "name", "rows", "seats_in_row", "airplane_type", "airplane_type_id"]

class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = "__all__"

class RouteSerializer(serializers.ModelSerializer):
    source = AirportSerializer(read_only=True)
    source_id = serializers.PrimaryKeyRelatedField(queryset=Airport.objects.all(), source="source", write_only=True)
    destination = AirportSerializer(read_only=True)
    destination_id = serializers.PrimaryKeyRelatedField(queryset=Airport.objects.all(), source="destination", write_only=True)
    class Meta:
        model = Route
        fields = ["id", "source", "source_id", "destination", "destination_id", "distance"]

class FlightSerializer(serializers.ModelSerializer):
    route = RouteSerializer(read_only=True)
    route_id = serializers.PrimaryKeyRelatedField(queryset=Route.objects.all(), source="route", write_only=True)
    airplane = AirplaneSerializer(read_only=True)
    airplane_id = serializers.PrimaryKeyRelatedField(queryset=Airplane.objects.all(), source="airplane", write_only=True)
    crew = CrewSerializer(many=True, read_only=True)
    crew_ids = serializers.PrimaryKeyRelatedField(queryset=Crew.objects.all(), source="crew", many=True, write_only=True)
    class Meta:
        model = Flight
        fields = ["id", "route", "route_id", "airplane", "airplane_id", "departure_time", "arrival_time", "crew", "crew_ids"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class TicketSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only=True)
    flight_id = serializers.PrimaryKeyRelatedField(queryset=Flight.objects.all(), source="flight", write_only=True)
    order = OrderSerializer(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), source="order", write_only=True)
    class Meta:
        model = Ticket
        fields = ["id", "row", "seat", "flight", "flight_id", "order", "order_id"]

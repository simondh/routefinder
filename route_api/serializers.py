from rest_framework import serializers

from route_api.models import Routes


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Routes
        fields = ['node_a', 'node_b']
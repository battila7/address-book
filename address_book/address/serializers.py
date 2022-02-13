from rest_framework import serializers

from .models import Address


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Addresses.

    I prefer being explicit when it comes to serialization and list fields
    by hand.
    """

    class Meta:
        model = Address
        fields = (
            "url",
            "id",
            "created_at",
            "title",
            "country",
            "state",
            "zip_code",
            "city",
            "address_line_one",
            "address_line_two",
        )

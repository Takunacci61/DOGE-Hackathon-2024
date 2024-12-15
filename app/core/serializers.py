from rest_framework import serializers


# Country serializer

class CountryInputSerializer(serializers.Serializer):
    """
    Serializer for entering a country.
    """
    country = serializers.CharField(max_length=100, required=True)

    def validate_country(self, value):
        """
        Validate the entered country.
        """
        # Optionally, you can validate against a list of allowed countries
        allowed_countries = ["United Kingdom", "United States", "Canada", "Australia"]
        if value not in allowed_countries:
            raise serializers.ValidationError(f"{value} is not a recognized country.")
        return value



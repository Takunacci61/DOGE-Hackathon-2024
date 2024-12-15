from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CountryInputSerializer
from django.conf import settings
import json
from grok import Grok


# Initialize xAI Grok client
class CountryAPIView(APIView):
    """
    API view to handle country input.
    """

    def post(self, request):
        serializer = CountryInputSerializer(data=request.data)
        if serializer.is_valid():
            country = serializer.validated_data['country']
            # Return a response with the entered country
            return Response({"message": f"Country '{country}' has been accepted."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Initialize xAI Grok client

class ResidencyInfoAPIView(APIView):
    """
    API view to handle country input and provide residency info.
    """

    def post(self, request):
        serializer = CountryInputSerializer(data=request.data)
        if serializer.is_valid():
            country = serializer.validated_data['country']

            # Get residency information for the provided country
            residency_info = get_residency_info(country)

            if "error" in residency_info:
                return Response(
                    {"message": f"Failed to retrieve residency info for '{country}'.",
                     "error": residency_info["error"]},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

            return Response(
                {
                    "message": f"Country '{country}' has been accepted.",
                    "residency_info": residency_info,
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_residency_info(country):
    """
    Get residency types for a given country using Grok Beta.
    Returns a JSON response with residency types including name, description, URL, and requirements.
    """
    try:
        grok = Grok(
            """
            {
                "residency_types": [
                    {
                        "name": str,
                        "description": str,
                        "url": str,
                        "requirements": [str]
                    }
                ]
            }
            """
        )

        # Define the structured expectation with Grok Beta
        prompt = (
            f"You are a knowledgeable immigration specialist. "
            f"Provide a JSON object containing residency types for {country}. "
            "The JSON must include a key 'residency_types' which is an array of objects. "
            "Each object must include the following keys: 'name', 'description', 'url', and 'requirements'. "
            "The 'requirements' field must be an array of strings. "
            "Return only the JSON, with no additional text or commentary."
        )

        # Generate response using Grok Beta
        response = grok.completion(prompt=prompt, temperature=0)

        try:
            # Parse response into JSON
            response_json = json.loads(response)
            if "residency_types" in response_json:
                return response_json
            else:
                return {"error": "The response JSON does not contain the 'residency_types' key."}
        except json.JSONDecodeError:
            return {"error": "Failed to parse the response text as JSON."}

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

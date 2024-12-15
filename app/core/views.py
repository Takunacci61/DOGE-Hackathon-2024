from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CountryInputSerializer
from django.conf import settings
import json
import openai

# Initialize xAI Grok client

# Set the API key directly
openai.api_key = settings.OPENAI_ENDPOINT


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
    Get residency types for a given country using OpenAI's GPT-4 model.
    Returns a JSON response with residency types including name, description, URL, and requirements.
    """
    try:
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a knowledgeable immigration specialist. "
                    "You must return ONLY a valid JSON object, no extra text, no code fences, and no commentary. "
                    "The JSON must contain a top-level key 'residency_types' whose value is an array of objects. "
                    "Each object must include the following keys: 'name', 'description', 'url', and 'requirements'. "
                    "'requirements' must be an array of strings. "
                    "List all available residency options without omission."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Provide a strictly formatted JSON object for {country} with the key 'residency_types'. "
                    "Each item in the array should have 'name', 'description', 'url', and 'requirements'. "
                    "Do not add any text other than the JSON."
                )
            }
        ]

        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0
        )

        response_text = completion.get("choices", [{}])[0].get("message", {}).get("content", "")

        try:
            response_json = json.loads(response_text)
            if "residency_types" in response_json:
                return response_json
            else:
                return {"error": "The response JSON does not contain the 'residency_types' key."}
        except json.JSONDecodeError:
            return {"error": "Failed to parse the response text as JSON."}

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .data_handler import DataHandler

class SubmitDataView(APIView):
    def post(self, request):
        data = request.data

        # Проверка наличия необходимых полей
        required_fields = ['beauty_title', 'title', 'coords', 'user', 'level', 'images']
        for field in required_fields:
            if field not in data:
                return Response({
                    "status": 400,
                    "message": f"Поле {field} отсутствует.",
                    "id": None
                }, status=status.HTTP_400_BAD_REQUEST)

        try:
            pereval_id = DataHandler.submit_data(data)
            return Response({
                "status": 200,
                "message": None,
                "id": pereval_id
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": 500,
                "message": str(e),
                "id": None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetSubmissionView(APIView):
    def get(self, request, id):
        try:
            submission = DataHandler.get_submission(id)
            if submission:
                return Response({
                    "status": 200,
                    "data": submission
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": 404,
                    "message": "Запись не найдена."
                }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "status": 500,
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditSubmissionView(APIView):
    def put(self, request, id):
        data = request.data

        # Проверка наличия необходимых полей (можно настроить по необходимости)
        required_fields = ['beauty_title', 'title', 'coords', 'user', 'level', 'images']
        for field in required_fields:
            if field not in data:
                return Response({
                    "status": 400,
                    "message": f"Поле {field} отсутствует.",
                    "id": None
                }, status=status.HTTP_400_BAD_REQUEST)

        try:
            updated_submission = DataHandler.edit_submission(id, data)
            if updated_submission:
                return Response({
                    "status": 200,
                    "message": "Запись успешно обновлена.",
                    "data": updated_submission
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": 404,
                    "message": "Запись не найдена."
                }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "status": 500,
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetUser SubmissionsView(APIView):
    def get(self, request):
        user_email = request.query_params.get('user__email')
        if not user_email:
            return Response({
                "status": 400,
                "message": "Поле 'user__email' обязательно."
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            submissions = DataHandler.get_user_submissions(user_email)
            return Response({
                "status": 200,
                "data": submissions
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": 500,
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


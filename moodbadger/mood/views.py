from .models import Mood
from .serializers import MoodSerializer
from django.db.models import Max
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response


class MoodViewSet(viewsets.ViewSet):

    queryset = Mood.objects.all().order_by('-created_at')
    serializer_class = MoodSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        mood_history = Mood.objects.filter(user=request.user).order_by('-created_at')
        serializer = MoodSerializer(mood_history, many=True)

        response = {
            'history': serializer.data,
            'current_streak': mood_history[0].streak if len(mood_history) else 0,
        }

        longest_streak = max(m.streak for m in mood_history)

        # Get (max streak of all users < this user's streak) / all user count
        streak_percentile = Mood.objects.values('user')\
            .annotate(max_streak=Max('streak'))\
            .filter(max_streak__lte=longest_streak)\
            .order_by().count() / User.objects.count()

        if streak_percentile > .5:
            response['streak_percentile'] = round(streak_percentile * 100)

        return Response(response)

    def create(self, request):
        serializer = MoodSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(creator=request.user)

        return Response(serializer.data)

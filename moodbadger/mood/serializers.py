from .models import Mood
from rest_framework import serializers
from datetime import date, timedelta


class MoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mood
        fields = ['description', 'streak', 'date', 'created_at']
        read_only_fields = ['streak', 'date', 'created_at']

    def create(self, validated_data):
        current_user = self.context['request'].user

        yesterdays_mood = Mood.objects.filter(user=current_user).filter(date=date.today() - timedelta(days=1)).first()
        current_streak = yesterdays_mood.streak if yesterdays_mood else 0

        mood = Mood(
            user=current_user,
            description=validated_data['description'],
            streak=current_streak + 1
        )

        mood.save()
        return mood

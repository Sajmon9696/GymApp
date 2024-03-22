from django.db import models

from accounts.models import User
from training_programs.models import TrainingPlan, TrainingPlanInfo


# Create your models here.


class Conversation(models.Model):
    """
        Model reprezentujący konwersację pomiędzy użytkownikami.
        """
    members = models.ManyToManyField(User, related_name='conversation')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)



class ConversationMessage(models.Model):
    """
        Model reprezentujący wiadomość w ramach konwersacji.
        """
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
    sent_to = models.ForeignKey(User, related_name='created_messages2', on_delete=models.CASCADE)
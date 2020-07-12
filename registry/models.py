from django.db import models
import uuid


class Passport(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    entered = models.DateField()
    vaccination = models.BooleanField()
    cage_num = models.CharField(max_length=16)

    def __str__(self):
        # if hasattr(self, 'cat'):
        #     return f'{self.cat} ({self.cage_num})'
        # elif hasattr(self, 'dog'):
        #     return f'{self.dog} ({self.cage_num})'
        # elif hasattr(self, 'animal'):
        #     return f'{self.animal} ({self.cage_num})'
        # else:
        #     return 'blank'

        if hasattr(self, 'abstractanimal'):
            return f'{self.abstractanimal} ({self.cage_num})'
        else:
            return 'blank'

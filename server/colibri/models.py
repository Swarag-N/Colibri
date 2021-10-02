from django.db import models
from Authentication.models import User
from django.core.exceptions import ValidationError


# TODO: 
# Create your models here.
class Colibri(models.Model):
    """
    Colibri Model
    """
    ORIGINAL = 'O'
    COMMENT = 'C'
    REPOST = 'R'
    TYPE_CHOICES = (
        (ORIGINAL, 'O'),
        (COMMENT, 'C'),
        (REPOST, 'R'),
    )

    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,  blank=True, null=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # class Meta:
    #     db_table = 'colibri'
    #     ordering = ['-created_at']
    
    # TODO Add Validation for type such that if type is set original, parent must be null
    def clean(self) -> None:
        if self.type == self.ORIGINAL and self.parent is not None:
            raise ValidationError('Original Colibri cannot have parent')
        return super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


    def __str__(self):
        return str(self.id)  +"  "+ str(self.type) +"  "+ str(self.created_at)
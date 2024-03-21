from django.core.exceptions import ValidationError

def validate_alpha(value):
    if not value.isalpha():
        raise ValidationError('This field cannot contain numbers, spaces, or special characters.')

def validate_name_length(value):
    if len(value) < 2:
        raise ValidationError('This field must be at least 2 characters long.')
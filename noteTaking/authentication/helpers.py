
from django.utils import timezone
from django.contrib.auth import get_user_model
def delete_not_activated_users():
    ten_minutes_before = timezone.now() - timezone.timedelta(minutes=10)
    users_to_delete = get_user_model().objects.filter(creation_date__lt=ten_minutes_before, is_active=False)
    users_to_delete.delete()

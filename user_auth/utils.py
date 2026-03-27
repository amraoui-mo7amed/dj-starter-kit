import os
import re
import time
from django.db import transaction
from django.contrib.auth.models import User


def create_user_account(user_data, profile_data, registration_doc):
    """
    Helper to create a User and UserProfile within a transaction.
    """
    from .models import UserProfile

    username = user_data["last_name"]
    if User.objects.filter(username=username).exists():
        username = f"{username}_{int(time.time())}"

    with transaction.atomic():
        user = User.objects.create_user(
            username=username,
            email=user_data["email"],
            password=user_data["password"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
        )

        UserProfile.objects.create(
            user=user,
            business_name=profile_data["business_name"],
            phone_number=profile_data["phone_number"],
            sex=profile_data["sex"],
            activity_type=profile_data["activity_type"],
            detailed_sector=profile_data.get("detailed_sector"),
            registration_doc=registration_doc,
        )
    return user


def user_profile_upload_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"registration_doc_{instance.user.id}.{ext}"
    return os.path.join("registration_docs/", filename)


def validate_algerian_phone(phone):
    """
    Validates Algerian phone numbers (mobile).
    Supports formats: 05, 06, 07, +213, 213.
    """
    pattern = r"^(0|\+213|213)[567]\d{8}$"
    return bool(re.match(pattern, str(phone)))

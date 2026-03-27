from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .utils import user_profile_upload_path


class UserProfile(models.Model):
    class sexChoices(models.TextChoices):
        MALE = "male", _("Male")
        FEMALE = "female", _("Female")

    class activityTypeChoices(models.TextChoices):
        TRADER = "trader", _("Trader (Retail / Wholesale)")
        MANUFACTURER = "manufacturer", _("Manufacturer (Production)")

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    business_name = models.CharField(_("Business Name"), max_length=255)
    phone_number = models.CharField(_("Phone Number"), max_length=20)
    sex = models.CharField(_("Sex"), max_length=10, choices=sexChoices.choices)
    activity_type = models.CharField(
        _("Activity Type"), max_length=20, choices=activityTypeChoices.choices
    )
    detailed_sector = models.CharField(
        _("Detailed Sector"), max_length=255, blank=True, null=True
    )
    registration_doc = models.FileField(
        _("Registration Document"),
        upload_to=user_profile_upload_path,
        help_text=_("Upload image or PDF (max 5MB)"),
    )
    is_approved = models.BooleanField(_("Is Approved"), default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.business_name}"

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")

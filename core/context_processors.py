from django.conf import settings
from django.utils.translation import gettext_lazy as _
from decouple import config


def site_settings(request):
    """
    Returns global site configuration and branding details.
    """
    return {
        "site_config": {
            "name": config("SITE_NAME", default=_("StarterKit")),
            "ar_name": config("SITE_AR_NAME", default="ستارتر كيت"),
            "tagline": config("SITE_TAGLINE", default=_("Modern Django Scaffolding")),
            "logo": config("SITE_LOGO_URL", default=None),
            "favicon": config("SITE_FAVICON_URL", default=None),
            "contact_email": config("CONTACT_EMAIL", default="admin@example.com"),
            "phone": config("CONTACT_PHONE", default="+000 000 000"),
            "social": {
                "facebook": config("SOCIAL_FB", default="#"),
                "twitter": config("SOCIAL_TWITTER", default="#"),
                "instagram": config("SOCIAL_INSTA", default="#"),
            },
            "seo": {
                "description": config(
                    "SEO_DESCRIPTION", default=_("Generic Django Starter Kit.")
                ),
                "keywords": config(
                    "SEO_KEYWORDS", default=_("django, boilerplate, starter kit")
                ),
            },
            "branding": {
                "primary_color": config("PRIMARY_COLOR", default="#0d6efd"),
                "secondary_color": config("SECONDARY_COLOR", default="#6c757d"),
                "accent_color": config("ACCENT_COLOR", default="#ffc107"),
                "success_color": config("SUCCESS_COLOR", default="#198754"),
                "danger_color": config("DANGER_COLOR", default="#dc3545"),
                "dark_color": config("DARK_COLOR", default="#212529"),
                "light_color": "#f8f9fa",
            },
        }
    }

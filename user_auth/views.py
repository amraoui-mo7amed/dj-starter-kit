from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from .models import UserProfile
from .utils import (
    create_user_account,
    user_profile_upload_path,
    validate_algerian_phone,
)


def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy("dash:dash_home"))

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        errors = []

        if not username or not password:
            errors.append(_("Please fill in all required fields."))

        if errors:
            return JsonResponse({"success": False, "errors": errors})

        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse(
                    {"success": True, "redirect_url": reverse("dash:dash_home")}
                )
            else:
                return JsonResponse(
                    {
                        "success": False,
                        "errors": [
                            _("Invalid username or password. Please try again.")
                        ],
                    }
                )
        except Exception as e:
            return JsonResponse({"success": False, "errors": [str(e)]})

    return render(request, "auth/login.html")


def logout_view(request):
    logout(request)
    return redirect("user_auth:login")


def signup_view(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy("dash:dash_home"))

    if request.method == "POST":
        # Extract data
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        business_name = request.POST.get("business_name")
        phone_number = request.POST.get("phone_number")
        sex = request.POST.get("sex")
        activity_type = request.POST.get("activity_type")
        detailed_sector = request.POST.get("detailed_sector", "")
        registration_doc = request.FILES.get("registration_doc")

        errors = []

        # Validation
        if not first_name:
            errors.append(_("First name is required."))
        if not last_name:
            errors.append(_("Last name is required."))
        if not email:
            errors.append(_("Email is required."))
        if not password:
            errors.append(_("Password is required."))
        if password != confirm_password:
            errors.append(_("Passwords do not match."))
        elif len(password) < 8:
            errors.append(_("Password must be at least 8 characters long."))
        if not business_name:
            errors.append(_("Business name is required."))
        if not phone_number:
            errors.append(_("Phone number is required."))
        elif not validate_algerian_phone(phone_number):
            errors.append(
                _("Enter a valid Algerian phone number (e.g., 05/06/07 XXXXXXXX).")
            )

        if not sex:
            errors.append(_("Sex is required."))
        if not activity_type:
            errors.append(_("Activity type is required."))
        if not registration_doc:
            errors.append(_("Registration document is required."))

        if errors:
            return JsonResponse({"success": False, "errors": errors})

        # Check existing user
        if User.objects.filter(username=email).exists():
            return JsonResponse(
                {"success": False, "errors": [_("This email is already registered.")]}
            )

        try:
            # Data dictionaries for helper
            user_data = {
                "email": email,
                "password": password,
                "first_name": first_name,
                "last_name": last_name,
            }
            profile_data = {
                "business_name": business_name,
                "phone_number": phone_number,
                "sex": sex,
                "activity_type": activity_type,
                "detailed_sector": detailed_sector,
            }

            user = create_user_account(user_data, profile_data, registration_doc)

            return JsonResponse(
                {
                    "success": True,
                    "message": "you're account is now under review, we will let you know when it's approved",
                }
            )
        except Exception as e:
            return JsonResponse({"success": False, "errors": [str(e)]})

    return render(
        request,
        "auth/signup.html",
        {
            "sex_choices": UserProfile.sexChoices.choices,
            "activity_choices": UserProfile.activityTypeChoices.choices,
        },
    )

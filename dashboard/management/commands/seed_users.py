import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from user_auth.models import UserProfile
from django.db import transaction


class Command(BaseCommand):
    help = "Seeds the database with a specified number of randomized users and profiles"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="Number of users to create")

    def handle(self, *args, **kwargs):
        count = kwargs["count"]

        ar_first_names = [
            "محمد",
            "أحمد",
            "ياسين",
            "عمر",
            "إيمان",
            "مريم",
            "ليلى",
            "سمير",
        ]
        ar_last_names = ["بن علي", "بن عمر", "منصوري", "حداد", "بلقاسم", "زروقي"]
        en_first_names = ["John", "Sarah", "Alex", "Emma", "David", "Sophia", "Robert"]
        en_last_names = ["Smith", "Jones", "Williams", "Brown", "Miller", "Davis"]

        ar_business_types = ["محل", "مؤسسة", "ورشة", "متجر"]
        en_business_types = ["Store", "Enterprise", "Workshop", "Shop"]

        sectors = [
            "Electronics",
            "Clothes",
            "Food",
            "Furniture",
            "Hardware",
            "Construction",
        ]

        self.stdout.write(f"Seeding {count} users...")

        created_count = 0
        with transaction.atomic():
            for i in range(count):
                lang = random.choice(["ar", "en"])
                if lang == "ar":
                    first = random.choice(ar_first_names)
                    last = random.choice(ar_last_names)
                    b_type = random.choice(ar_business_types)
                    business_name = f"{b_type} {first} {last}"
                else:
                    first = random.choice(en_first_names)
                    last = random.choice(en_last_names)
                    b_type = random.choice(en_business_types)
                    business_name = f"{first}'s {b_type}"

                # Generate a unique username
                base_username = first.lower().replace(" ", "")
                username = f"{base_username}_{random.randint(100, 999)}_{i}"
                email = f"{username}@example.com"

                while User.objects.filter(username=username).exists():
                    username = f"{base_username}_{random.randint(100, 9999)}_{i}"

                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password="password123",
                    first_name=first,
                    last_name=last,
                )

                sex = random.choice(UserProfile.sexChoices.values)
                activity = random.choice(UserProfile.activityTypeChoices.values)
                approved = random.choice([True, False])
                phone = f"0{random.choice(['5', '6', '7'])}{random.randint(10000000, 99999999)}"

                UserProfile.objects.create(
                    user=user,
                    business_name=business_name,
                    phone_number=phone,
                    sex=sex,
                    activity_type=activity,
                    detailed_sector=random.choice(sectors),
                    is_approved=approved,
                )
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created {created_count} users and profiles."
            )
        )

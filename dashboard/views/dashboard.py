from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from user_auth.models import UserProfile
from django.contrib.auth.models import User
import json


@login_required
def dash_home(request):
    user_profile = getattr(request.user, "profile", None)
    role = user_profile.activity_type if user_profile else "trader"

    # Common Data
    context = {
        "role": role,
        "notifications": [
            {
                "type": "warning",
                "title": _("Low Stock"),
                "message": _("Product 'A' is below threshold."),
                "time": "2h ago",
            },
            {
                "type": "info",
                "title": _("Payment Due"),
                "message": _("Supplier 'X' invoice is due in 2 days."),
                "time": "5h ago",
            },
        ],
    }

    if request.user.is_superuser:
        # Platform Admin Statistics
        total_users = User.objects.count()
        approved_merchants = UserProfile.objects.filter(is_approved=True).count()
        pending_approval = UserProfile.objects.filter(is_approved=False).count()
        traders_count = UserProfile.objects.filter(activity_type="trader").count()
        manufacturers_count = UserProfile.objects.filter(
            activity_type="manufacturer"
        ).count()

        context.update(
            {
                "role": "admin",
                "stat_1": {
                    "title": _("Total Users"),
                    "value": total_users,
                    "icon": "fa-users",
                    "color": "primary",
                },
                "stat_2": {
                    "title": _("Approved Merchants"),
                    "value": approved_merchants,
                    "icon": "fa-user-check",
                    "color": "success",
                },
                "stat_3": {
                    "title": _("Pending Approval"),
                    "value": pending_approval,
                    "icon": "fa-user-clock",
                    "color": "warning",
                },
                "stat_4": {
                    "title": _("Staff Members"),
                    "value": User.objects.filter(is_staff=True).count(),
                    "icon": "fa-user-shield",
                    "color": "info",
                },
                "chart_title": _("Users Distribution"),
                "user_dist_labels": json.dumps(
                    [str(_("Traders")), str(_("Manufacturers"))]
                ),
                "user_dist_values": json.dumps([traders_count, manufacturers_count]),
                "list_title": _("Recent Registrations"),
                "recent_users": UserProfile.objects.select_related("user").order_by(
                    "-created_at"
                )[:5],
            }
        )
    elif role == "manufacturer":
        # Manufacturer specific dummy data
        context.update(
            {
                "stat_1": {
                    "title": _("Raw Materials"),
                    "value": "1,200 kg",
                    "trend": "5.4",
                    "icon": "fa-fill-drip",
                    "color": "info",
                },
                "stat_2": {
                    "title": _("Production Cost"),
                    "value": "240.00 DZD",
                    "trend": "2.1",
                    "icon": "fa-coins",
                    "color": "primary",
                },
                "stat_3": {
                    "title": _("Active Batches"),
                    "value": "12",
                    "trend": "10.5",
                    "icon": "fa-industry",
                    "color": "success",
                },
                "stat_4": {
                    "title": _("Ready Products"),
                    "value": "850",
                    "icon": "fa-box",
                    "color": "warning",
                },
                "chart_title": _("Production Volume (Week)"),
                "chart_values": json.dumps([120, 150, 180, 200, 170, 220, 250]),
                "list_title": _("Active Production Orders"),
                "list_items": ["Order #102", "Order #105", "Order #108"],
            }
        )
    else:
        # Trader specific dummy data
        context.update(
            {
                "stat_1": {
                    "title": _("Daily Liquidity"),
                    "value": "45,000.00 DZD",
                    "trend": "12.5",
                    "icon": "fa-wallet",
                    "color": "success",
                },
                "stat_2": {
                    "title": _("Total Sales"),
                    "value": "125,000.50 DZD",
                    "trend": "8.2",
                    "icon": "fa-shopping-cart",
                    "color": "primary",
                },
                "stat_3": {
                    "title": _("Overdue Invoices"),
                    "value": "5",
                    "trend": "1.5",
                    "icon": "fa-file-invoice-dollar",
                    "color": "danger",
                    "trend_dir": "up",
                    "trend_color": "danger",
                },
                "stat_4": {
                    "title": _("Inventory Items"),
                    "value": "1,240",
                    "icon": "fa-boxes",
                    "color": "info",
                },
                "chart_title": _("Weekly Sales Revenue"),
                "chart_values": json.dumps(
                    [12000, 15000, 8000, 19000, 22000, 18000, 25000]
                ),
                "list_title": _("Top Selling Products"),
                "list_items": ["Product A", "Product B", "Product C"],
                "top_products": json.dumps(
                    ["Product A", "Product B", "Product C", "Product D", "Product E"]
                ),
                "top_qty": json.dumps([50, 40, 35, 30, 25]),
            }
        )

    return render(request, "dash/dash_home.html", context)

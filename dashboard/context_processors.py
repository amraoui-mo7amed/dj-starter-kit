from django.utils.translation import gettext_lazy as _


def dashboard_sidebar(request):
    """
    Returns the dashboard menu items with RBAC flags.
    """
    return {
        "dashboard_menu": [
            {
                "title": _("Dashboard"),
                "icon": "fas fa-th-large",
                "url_name": "dash:dash_home",
                "admin_only": False,
            },
            {
                "title": _("users"),
                "icon": "fas fa-users",
                "url_name": "dash:user_list",
                "admin_only": True,
            },
            {
                "title": _("Inventory"),
                "icon": "fas fa-boxes",
                "url_name": "#",
                "admin_only": False,
            },
            {
                "title": _("Sales"),
                "icon": "fas fa-file-invoice",
                "url_name": "#",
                "admin_only": False,
            },
            {
                "title": _("Purchases"),
                "icon": "fas fa-shopping-basket",
                "url_name": "#",
                "admin_only": False,
            },
            {
                "title": _("Partners"),
                "icon": "fas fa-user-friends",
                "url_name": "#",
                "admin_only": False,
            },
            {
                "title": _("Reports"),
                "icon": "fas fa-chart-pie",
                "url_name": "#",
                "admin_only": True,
            },
        ],
    }

# Django Starter Kit

A robust, centralized, and highly customizable Django boilerplate designed for rapid project scaffolding. This kit focuses on "Single Point of Truth" configuration, multi-language support (RTL/LTR), and modern UI components.

## Key Features

- **Centralized Configuration**: Manage site name, logo, contact details, and SEO metadata from a single Python file (`core/context_processors.py`).
- **Dynamic Branding**: UI colors are driven by CSS variables injected from the backend. Change your brand colors in one place, and the entire site (Dashboard & Frontend) updates instantly.
- **Full i18n & RTL Support**: Built-in support for Arabic (RTL) and English (LTR) with automatic layout switching and translatable metadata.
- **Modern Component Library**: Ready-to-use generic components including:
  - Custom brand-aware Select tags.
  - Modern File Input widgets.
  - Specialized Pagination.
  - SweetAlert2 integration for all object actions.
- **Unified Design System**: Consistent visual identity across the landing page and the administrative dashboard using a shared variable-driven CSS architecture.
- **AJAX-First Pattern**: Guidelines and utilities for standardizing AJAX updates and deletes with translatable feedback.

## Tech Stack

- **Backend**: Django 5.2+
- **Environment**: python-decouple (for .env management)
- **Styling**: Bootstrap 5.3 + Custom CSS Variables
- **Icons**: FontAwesome 5
- **Animations**: AOS (Animate On Scroll)
- **Real-time**: Django EventStream + SSE support

## Getting Started

1. **Clone & Install**:
   ```bash
   git clone <repo-url>
   pip install -r requirements.txt
   ```

2. **Configure Environment**:
   Create a .env file based on the project requirements (SECRET_KEY, DB settings, etc.).

3. **Database Setup**:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run Server**:
   ```bash
   python manage.py runserver
   ```

## Customization

### 1. Site Details & Branding
Edit `core/context_processors.py` to change global settings:
```python
"site_config": {
    "name": _("Your Project"),
    "ar_name": "مشروعك",
    "branding": {
        "primary_color": "#0d6efd", # Your brand primary
        "secondary_color": "#6c757d",
        ...
    }
}
```

### 2. Styling
All stylesheets reference the original variables in `frontend/static/css/index.css`. **Never use hardcoded hex colors** in new CSS files; always reference `var(--brand-primary)`, `var(--brand-secondary)`, etc.

### 3. Adding Translations
Run the standard Django translation commands to update the locale files:
```bash
python manage.py makemessages -l ar
python manage.py compilemessages
```

## Development Guidelines

- **Components**: Always use `dashboard/templates/components/` for selects and pagination.
- **Forms**: Add the .form class and use `partials/errorList.html` for validation errors.
- **Logic**: Helper functions belong in <app>/utils.py.
- **UI Actions**: Use SweetAlert for confirmation and AJAX for object updates/deletions.

## License

This is a generic boilerplate for future projects. Customize and extend as needed.

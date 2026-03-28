# Django Starter Kit

A robust, centralized, and highly customizable Django boilerplate designed for rapid project scaffolding. This kit focuses on a "Single Point of Truth" configuration, multi-language support (AR/EN/FR), and modern UI components.

## Key Features

- **Centralized Configuration**: Manage site name, logo, contact details, and SEO metadata from a single Python file (`core/context_processors.py`).
- **Dynamic Branding**: UI colors are driven by CSS variables injected from the backend. Change your brand colors in one place, and the entire site (Dashboard & Frontend) updates instantly.
- **Full i18n & RTL Support**: Built-in support for Arabic (RTL), English (LTR), and French (LTR) with automatic layout switching and translatable metadata.
- **Dynamic Dashboard Menu**: Manage navigation links and Role-Based Access Control (RBAC) via `dashboard/context_processors.py`.
- **SVG Logo System**: Includes a scalable SVG component fallback for the logo to ensure a clean UI even without uploaded assets.
- **Modern Component Library**: Ready-to-use generic components including custom Select tags, File Input widgets, and specialized Pagination.
- **AJAX-First Pattern**: Guidelines and utilities for standardizing AJAX updates and deletes with translatable SweetAlert2 feedback.

## Tech Stack

- **Backend**: Django 5.2+
- **Environment**: python-decouple (for security settings)
- **Styling**: Bootstrap 5.3 + Custom CSS Variables
- **Icons**: FontAwesome 5
- **Animations**: AOS (Animate On Scroll)
- **Real-time**: Django EventStream + SSE support

## Getting Started

1. **Clone & Install**:
   ```bash
   git clone https://github.com/amraoui-mo7amed/dj-starter-kit
   pip install -r requirements.txt
   ```

2. **Configure Environment**:
   Copy `.env.example` to `.env` and set your `APP_SECRET` and database settings.
   ```bash
   cp .env.example .env
   ```

3. **Database Setup**:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Seed Database (Optional)**:
   Generate randomized generic user profiles for development:
   ```bash
   python manage.py seed_users 10
   ```

5. **Run Server**:
   ```bash
   python manage.py runserver
   ```

## Customization

### 1. Project Identity & Branding
All global settings are hardcoded for simplicity in `core/context_processors.py`. Edit the `site_config` dictionary to change:
- **Site Names**: `name` (English/Generic) and `ar_name` (Arabic).
- **Branding**: Primary, Secondary, and functional colors (Hex codes).
- **SEO**: Global meta descriptions and keywords.
- **Contact**: Email, Phone, and Social links.

### 2. Dashboard Navigation & RBAC
Manage menu items in `dashboard/context_processors.py`. Use the `admin_only: True` flag to restrict specific links to superusers.

### 3. Styling
All stylesheets reference the original variables in `frontend/static/css/index.css`. **Never use hardcoded hex colors** in new CSS files; always reference `var(--brand-primary)`, `var(--brand-secondary)`, etc.

### 4. Internationalization
Run these commands to update or add translations:
```bash
python manage.py makemessages -l ar -l fr
python manage.py compilemessages
```

## Development Guidelines

- **Components**: Always use `dashboard/templates/components/` for selects and pagination.
- **Forms**: Add the `.form` class and use `partials/errorList.html` for validation errors.
- **Logic**: Helper functions belong in `<app>/utils.py`.
- **UI Actions**: Always use SweetAlert for confirmation and AJAX for object updates/deletions.

## License

This is a generic boilerplate for future projects. Customize and extend as needed.

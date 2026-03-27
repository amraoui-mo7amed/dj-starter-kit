# Smart Operating Cycle (SOC) 

Ps: in arabic, its `ذكي الإستغلال`

A comprehensive SaaS platform for managing operating cycles of small and medium enterprises (SMEs) in Algeria.

## Project Overview

Smart Operating Cycle is a graduation project developed at **Kasdi Merbah University – Ouargla, Algeria** by:
- Amal Bensherif
- Soumahan Tembokto

The platform helps SMEs (retailers, wholesalers, and manufacturers) manage their daily operations through intelligent inventory tracking, sales/purchase management, and AI-powered recommendations.

## Target Users

1. **Trader (تاجر)**: Retail/wholesale businesses focused on sales speed, inventory tracking, and daily liquidity
2. **Manufacturer (مصنع)**: Production businesses focused on raw materials, production tracking, and supplier relationships
3. **Admin (مسؤول)**: Platform management team responsible for system monitoring, users, and subscriptions

## Core Features

### 1. Smart Onboarding
- Role-based registration (Trader/Manufacturer)
- Adaptive forms based on user type
- Barcode/QR scanning for quick data entry

### 2. Role-Based Dashboards
- **Trader Dashboard**: Cash liquidity, inventory status, sales performance, overdue invoices, weekly sales charts
- **Manufacturer Dashboard**: Raw materials status, production unit cost, production batches, material consumption alerts

### 3. Inventory Management
- Add products via barcode scanning with automatic data extraction
- Real-time quantity tracking
- Low stock alerts with configurable thresholds
- Product images and supplier linking

### 4. Sales & Purchase Management
- **Purchase Invoices**: Scan supplier QR/barcodes, auto-extract data, update inventory, track supplier debts
- **Sales Invoices**: Quick product scanning, quantity adjustment, customer selection, payment tracking
- Support for cash and credit transactions

### 5. Production Management (Manufacturers)
- Create production orders
- Automatic raw material consumption calculation (Bill of Materials)
- Track finished goods inventory
- Production batch tracking

### 6. Smart Alerts & Recommendations
- Low stock warnings
- Overdue payment alerts (customers/suppliers)
- Cash flow warnings
- Business optimization suggestions

### 7. Admin Panel
- User management (view, edit, ban)
- Subscription & billing management
- Revenue reports and analytics
- System monitoring
- Broadcast notifications

## Signup Data Requirements

### Common Fields (All Users)
| Field | Type | Required |
|-------|------|----------|
| Full Name | Text | Yes |
| Business/Shop/Workshop Name | Text | Yes |
| Phone Number | Text | Yes (with format validation) |
| Email | Text | Yes (with format validation) |
| Password | Text | Yes (encrypted) |
| Activity Type | Select | Yes (Trader or Manufacturer) |
| Detailed Sector | Text | Optional |

## Design System

### Color Palette
```css
:root {
  /* Brand Primary Colors */
  --soc-blue-dark: #2A4B8C;    /* Character 'S' and Cube Frame */
  --soc-blue-medium: #6B8EBF;  /* Character 'O' */
  --soc-blue-light: #9DBBDD;   /* Character 'C' */

  /* Icon & Text Colors */
  --soc-icon-red: #A63636;     /* Delivery Truck Icon */
  --soc-icon-gold: #8C7A3D;    /* People/Group Icon */
  --soc-text-main: #1A1A1A;    /* "SMART OPERATING CYCLE" Text */

  /* Background & Accents */
  --soc-bg-canvas: #D9D9D9;    /* Image Background */
  --soc-white-accent: #FFFFFF; /* Inner Cube and Outlines */
}
```

### Typography
- **Primary Font**: Cairo
- **Language Support**: Arabic (AR), English (EN)

### Design Principles
- Modern SaaS interface
- Status indicators (Green/Yellow/Red)
- Clear cards with large numbers
- Easy-to-read fonts
- Focus on decision-making, not just data display
- Smooth transitions between screens
- Dynamic alerts
- Simulated AI-driven recommendations

## Subscription Plans

| Plan | Price | Features |
|------|-------|----------|
| Basic | 3,000 DZD/month | Trader only, basic features |
| Pro | 7,000 DZD/month | Trader/Manufacturer, smart alerts, advanced features |
| Enterprise | 15,000 DZD/month | Manufacturer only, priority support, advanced reports |

## Technical Stack

- **Frontend**: Modern web technologies with RTL support
- **Backend**: Django (based on user preference)
- **Database**: Relational database for structured business data
- **Barcode/QR**: Scanning integration for product and invoice entry

## Key Workflows

### Adding a Product (First Time)
1. Scan product barcode
2. If product doesn't exist, quick entry form opens
3. Enter: Name, Purchase price, Sale price, Initial quantity, Alert threshold
4. Save to inventory

### Adding Purchase Invoice
1. Scan invoice QR/barcode (or enter manually)
2. Select supplier
3. For each item: Scan product barcode → Enter quantity
4. System updates inventory and supplier account

### Adding Sale Invoice
1. Scan product barcode
2. Product appears in invoice list with quantity field (default: 1)
3. Adjust quantity and price if needed
4. Select customer (if credit) or cash payment
5. System deducts from inventory and records sale

### Production Order (Manufacturers)
1. Select "New Production Order"
2. Choose finished product from list
3. Enter production quantity
4. System displays required raw materials and available quantities
5. If materials sufficient, confirm order
6. System deducts raw materials and adds to finished goods

## Admin Revenue Collection Process (MVP - Manual)

1. New user registers → Gets free trial or Basic plan
2. After trial or when choosing paid plan → Admin creates invoice manually
3. Invoice status: "Unpaid" → User sees notification in dashboard
4. User pays externally (bank transfer or other method) → Notifies admin via WhatsApp/Email
5. Admin logs in → Finds user → Changes invoice status to "Paid" manually
6. System sends confirmation to user and activates subscription

## Project Status

This is an **MVP (Minimum Viable Product)** / Proof of Concept focusing on:
- Core user flows
- Basic feature demonstration
- Simulated smart recommendations
- Manual admin processes

## License

Graduation Project - Kasdi Merbah University, Ouargla
Ministry of Higher Education and Scientific Research - Algeria
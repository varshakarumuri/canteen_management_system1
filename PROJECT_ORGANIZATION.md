# E-Canteen Project Organization & Guidelines

**Version 1.0 | Last Updated: March 24, 2026**

---

## 📂 Project Structure

```
canteen_management_system1/
├── db.sqlite3                    # Django database
├── manage.py                     # Django management script
├── E_Canteen/                    # Main project settings
│   ├── __init__.py
│   ├── settings.py              # Django configuration
│   ├── urls.py                  # Main URL router
│   ├── views.py
│   ├── wsgi.py
│   └── asgi.py
├── user/                         # User app (customers)
│   ├── migrations/              # Database migrations
│   ├── admin.py
│   ├── apps.py
│   ├── models.py               # User models
│   ├── urls.py                 # User-specific routes
│   ├── views.py                # User views
│   └── signals.py
├── staff/                        # Staff app (management)
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py               # Staff models
│   ├── urls.py                 # Staff-specific routes
│   └── views.py                # Staff views
├── templates/                    # HTML templates
│   ├── base.html               # Master template (DO NOT MODIFY LIGHTLY)
│   ├── home.html               # Landing page
│   ├── user/                   # User templates
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── menu.html
│   │   ├── cart.html
│   │   ├── active_orders.html
│   │   ├── profile.html
│   │   ├── change_password.html
│   │   ├── verify_email.html
│   │   ├── forgot_password.html
│   │   ├── reset_password.html
│   │   └── receipt.html
│   └── staff/                  # Staff templates
│       ├── login.html
│       ├── orders.html
│       ├── profile.html
│       └── completed_orders.html
├── static/                       # Static files
│   ├── css/
│   │   ├── styles.css          # Main stylesheet (SOURCE OF TRUTH)
│   │   ├── staff/
│   │   │   └── css/staff.css   # (Legacy - deprecated)
│   │   └── user/
│   │       └── css/menu.css    # (Legacy - deprecated)
│   └── media/                  # Uploaded content
│       └── menu_photos/        # Menu item images
├── myenv/                        # Virtual environment (DO NOT COMMIT)
├── DESIGN_SYSTEM.md            # Design system documentation
└── README.md                    # Project documentation

```

---

## 🎯 Directory Purpose & Rules

### `/templates/` - HTML Templates

**Purpose:** Django template files for rendering pages

**Organization:**

- `base.html` - Master template defining overall structure
- `home.html` - Public landing page
- `user/` - Customer-facing templates
- `staff/` - Staff admin templates

**Rules:**

1. All templates MUST inherit from `base.html`
2. All templates MUST include navbar using block: `{% block navbar %}`
3. All templates MUST include content using block: `{% block content %}`
4. Use `{{ }}` for variables, `{% %}` for logic
5. Names should be descriptive: `user_profile.html` not `p.html`
6. One template = One view responsibility

**File Naming Convention:**

```
user/[action_or_view_name].html
staff/[action_or_view_name].html
home.html (public pages)
```

Examples:

- ✅ `user/menu.html` (menu listing)
- ✅ `staff/orders.html` (order management)
- ❌ `u_menu.html` (abbreviations not allowed)
- ❌ `user_menu_page.html` (redundant)

### `/static/css/` - Stylesheets

**Purpose:** Centralized styling using CSS variables

**Organization:**

- `styles.css` - **SINGLE SOURCE OF TRUTH** for all styling
- Legacy folders (deprecated): `user/css/` and `staff/css/`

**Rules:**

1. ALL styling goes into `styles.css`
2. No inline styles in templates (except temporary debugging)
3. Use CSS variables: `var(--primary)` instead of `#ff6b35`
4. Use CSS classes for all styling: `.card-modern`, `.btn-primary-custom`, etc.
5. Document component patterns in the file header
6. Keep file organized with section comments

**Do NOT:**

- ❌ Create separate CSS files per page
- ❌ Use inline `style=""` attributes
- ❌ Hardcode colors (use CSS variables)
- ❌ Leave commented code

### `/user/` & `/staff/` - Django Apps

**Purpose:** Application logic separated by role

**Models Structure:**

**User App Models** (`user/models.py`):

- `Customer` - User account info
- `Menu` - Available menu items
- `Order` - Customer orders
- `Cart` - Shopping cart items

**Staff App Models** (`staff/models.py`):

- `StaffMember` - Staff accounts
- Other staff-specific models

**Rules:**

1. Use descriptive model names
2. Keep related models in the same app
3. Use `on_delete=models.CASCADE` where appropriate
4. Add `__str__()` to all models
5. Use `created_at` and `updated_at` timestamps

### `/media/` - Uploaded Content

**Purpose:** Store user-uploaded content (images, etc.)

**Organization:**

```
media/
└── menu_photos/      # Menu item images
    ├── item_1.jpg
    ├── item_2.png
    └── ...
```

**Rules:**

1. Organize by content type
2. Use descriptive filenames
3. Optimize images (max 500KB for menu photos)
4. Don't commit to version control

---

## 🎨 Template Structure (Standard Pattern)

All templates should follow this structure:

```html
{% extends 'base.html' %} {% block title %}Page Title{% endblock %} {% block
navbar %}
<!-- Navbar content -->
<nav class="navbar navbar-modern navbar-expand-lg">
  <!-- Standard navbar structure -->
</nav>
{% endblock %} {% block content %}
<div class="container-modern">
  <div class="page-container">
    <!-- Page content -->
  </div>
</div>
{% endblock %}
```

**Bootstrap Classes Used:**

- `navbar navbar-modern` - Navigation bar
- `navbar-expand-lg` - Responsive breakpoint
- `container-modern` - Outer wrapper with padding
- `page-container` - Inner max-width container
- `card-modern` - Content cards
- `btn-*-custom` - Buttons
- `form-group` - Form elements

---

## 📋 Template Consistency Checklist

When creating or modifying templates:

### Structure

- [ ] Extends `base.html`
- [ ] Has `{% block title %}`
- [ ] Has `{% block navbar %}`
- [ ] Has `{% block content %}`

### Navbar

- [ ] Uses `navbar navbar-modern`
- [ ] Includes branding/logo section
- [ ] Includes navigation links
- [ ] Uses Font Awesome icons for links
- [ ] Has responsive toggle button

### Content

- [ ] Wrapped in `container-modern` and `page-container`
- [ ] Uses semantic HTML (not divs for everything)
- [ ] Has clear heading hierarchy (h1 → h2 → h3)
- [ ] Uses `.card-modern` for content sections
- [ ] Uses `.menu-container` for grids
- [ ] Uses `.table-modern` for tabular data

### Forms

- [ ] Uses `.form-group` for each field
- [ ] Has labels with Font Awesome icons
- [ ] Uses `.form-group input` or `textarea` classes
- [ ] Has submit button with `.btn-primary-custom`
- [ ] Includes `{% csrf_token %}`

### Buttons

- [ ] Primary actions: `.btn-primary-custom`
- [ ] Secondary actions: `.btn-secondary-custom`
- [ ] Destructive actions: `.btn-danger-custom`
- [ ] All buttons have Font Awesome icons
- [ ] Button text is clear and action-oriented

### Icons

- [ ] All buttons have icons
- [ ] All navigation links have icons
- [ ] Icons use Font Awesome 6.4.0
- [ ] Icons paired with descriptive text

### Colors

- [ ] Uses CSS variables (not hardcoded hex)
- [ ] Primary: `var(--primary)` for user flows
- [ ] Secondary: `var(--secondary)` for headings
- [ ] Status colors semantic: success/danger/warning/info

### Responsive

- [ ] Mobile-friendly layout
- [ ] Touch targets minimum 44px
- [ ] Images responsive: `max-width: 100%`
- [ ] Tested on 480px, 768px, 1200px breakpoints

### Accessibility

- [ ] Clear heading hierarchy
- [ ] Images have alt text
- [ ] Links have visible focus states
- [ ] Color not only indicator
- [ ] Contrast ratio 4.5:1 minimum

### Performance

- [ ] No console errors
- [ ] Images optimized
- [ ] No unused CSS classes
- [ ] Proper caching headers

---

## 🎨 CSS Organization Rules

### CSS File Structure (`styles.css`)

1. **Variables Section** - CSS custom properties
2. **Global Styles** - Base element styling
3. **Layout Components** - Navbar, containers, grids
4. **UI Components** - Buttons, forms, cards, badges
5. **Animation Keyframes** - Transitions and animations
6. **Responsive Breakpoints** - Media queries

### CSS Naming Convention

```css
/* Component-based naming (BEM-inspired) */
.card-modern { }                    /* Base component */
.card-modern__header { }            /* Component child */
.card-modern__header--active { }    /* Component state */

/* Utility classes (limited use) */
.text-center { text-align: center; }
.mt-20 { margin-top: 20px; }

/* State classes */
.is-active { }
.is-disabled { }
.is-loading { }

/* DO NOT USE */
❌ .style1, .s1, .blue-box
❌ .left, .right, .float-left (semantic outdated)
❌ Random IDs for styling: #user-input-box
```

### Common Component Classes

| Component   | Class Name            | Usage              |
| ----------- | --------------------- | ------------------ |
| Button      | `.btn-*-custom`       | All buttons        |
| Form Group  | `.form-group`         | Form field wrapper |
| Card        | `.card-modern`        | Content container  |
| Card Header | `.card-header-modern` | Card title area    |
| Card Body   | `.card-body-modern`   | Card content area  |
| Navbar      | `.navbar-modern`      | Navigation bar     |
| Table       | `.table-modern`       | Data tables        |
| Menu Grid   | `.menu-container`     | Product/item grid  |
| Container   | `.container-modern`   | Page wrapper       |
| Badge       | `.badge`              | Status/label       |

---

## 🔄 Version Control & Git

### Commit Message Format

```
[type]: Brief description

Detailed explanation if needed.

Files: list of modified files
```

**Types:**

- `feat` - New feature
- `fix` - Bug fix
- `style` - CSS/styling changes
- `refactor` - Code restructuring
- `docs` - Documentation
- `chore` - Maintenance

### Files to Ignore (in `.gitignore`)

```
myenv/                  # Virtual environment
db.sqlite3             # Database
*.pyc                  # Python cache
__pycache__/           # Python cache
.env                   # Environment variables
media/                 # Uploaded files (usually)
.DS_Store              # macOS files
*.log                  # Log files
```

### Protected Files

⚠️ **Be very careful modifying:**

- `base.html` - Changes affect all templates
- `styles.css` - Changes affect entire site
- `settings.py` - Database/app configuration
- Migration files - Database schema history

---

## 📚 Best Practices

### Template Development

1. ✅ Always extend `base.html`
2. ✅ Use Django template tags properly
3. ✅ Keep templates focused (one view = one template)
4. ✅ Use template inheritance for repeated sections
5. ✅ Use `{% url %}` tag for links (not hardcoded paths)
6. ✅ Use `{% static %}` tag for static files

### CSS Development

1. ✅ Use CSS variables for all colors
2. ✅ Follow component-based naming
3. ✅ Use Flexbox/Grid for layouts
4. ✅ Mobile-first approach
5. ✅ Test across breakpoints
6. ✅ Document complex patterns

### Code Quality

1. ✅ Keep files well-organized
2. ✅ Use meaningful names
3. ✅ Document complex logic
4. ✅ Remove commented code before committing
5. ✅ Test changes locally first
6. ✅ Maintain design consistency

### Performance

1. ✅ Minimize CSS/JS files
2. ✅ Optimize images (< 500KB)
3. ✅ Use CDN for libraries
4. ✅ Cache static files
5. ✅ Lazy-load images
6. ✅ Profile before optimizing

---

## 🚨 Common Mistakes to Avoid

| ❌ Mistake                    | ✅ Correct Approach                |
| ----------------------------- | ---------------------------------- |
| Hardcoded colors in templates | Use CSS variables via `styles.css` |
| Inline styles in HTML         | Use CSS classes from `styles.css`  |
| Creating new CSS files        | Add to `styles.css` only           |
| Inconsistent naming           | Follow naming conventions          |
| Template without `base.html`  | Always extend `base.html`          |
| Missing responsive design     | Test at 480px, 768px, 1200px       |
| No icon with button text      | Always pair icons with text        |
| Broken focus states           | Ensure keyboard accessibility      |
| Hardcoded URLs                | Use `{% url %}` template tag       |
| Unused CSS classes            | Remove before committing           |

---

## 📞 Contact & Updates

For questions about organization or guidelines:

1. Check this document first
2. Review `DESIGN_SYSTEM.md` for design details
3. Check existing templates for patterns
4. Update documentation if clarification needed

**Last Updated:** March 24, 2026
**Maintained By:** Development Team

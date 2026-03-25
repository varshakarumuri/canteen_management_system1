# E-Canteen Design System

**Version 1.0 | Last Updated: March 24, 2026**

---

## 📋 Table of Contents

1. [Design Tokens](#design-tokens)
2. [Color Palette](#color-palette)
3. [Typography System](#typography-system)
4. [Components & Patterns](#components--patterns)
5. [Layout Guidelines](#layout-guidelines)
6. [Animation & Transitions](#animation--transitions)
7. [Responsive Design](#responsive-design)
8. [Accessibility](#accessibility)

---

## 🎨 Design Tokens

### CSS Variables (Root)

All design tokens are defined in `:root` in `static/css/styles.css`:

```css
:root {
  /* Colors */
  --primary: #ff6b35; /* Warm Orange */
  --primary-light: #ff9a56; /* Light Orange */
  --primary-dark: #e55a1f; /* Dark Orange */
  --secondary: #004e89; /* Deep Blue */
  --secondary-light: #00618a; /* Light Blue */
  --secondary-dark: #003f5c; /* Dark Blue */
  --success: #27ae60; /* Green */
  --danger: #e74c3c; /* Red */
  --warning: #f39c12; /* Yellow */
  --info: #3498db; /* Cyan */
  --dark: #1a1a1a; /* Almost Black */
  --light: #f8f9fa; /* Off White */
  --gray: #6c757d; /* Medium Gray */

  /* Spacing & Sizing */
  --border-radius: 12px;
  --border-radius-lg: 16px;

  /* Transitions */
  --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-fast: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);

  /* Shadows */
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.06);
  --shadow-md: 0 5px 20px rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 10px 30px rgba(0, 0, 0, 0.12);
  --shadow-xl: 0 20px 60px rgba(0, 0, 0, 0.15);
}
```

---

## 🎨 Color Palette

### Primary Colors

| Color             | Hex       | Usage                                  |
| ----------------- | --------- | -------------------------------------- |
| **Primary**       | `#ff6b35` | CTAs, buttons, highlights (user flows) |
| **Primary Light** | `#ff9a56` | Button hover states, gradients         |
| **Primary Dark**  | `#e55a1f` | Links, text links, active states       |

### Secondary Colors

| Color               | Hex       | Usage                                     |
| ------------------- | --------- | ----------------------------------------- |
| **Secondary**       | `#004e89` | Headings, subheadings, text (staff flows) |
| **Secondary Light** | `#00618a` | Navbar backgrounds, accents               |
| **Secondary Dark**  | `#003f5c` | Dark overlays                             |

### Semantic Colors

| Color       | Hex       | Usage                               |
| ----------- | --------- | ----------------------------------- |
| **Success** | `#27ae60` | Success messages, checkmarks        |
| **Danger**  | `#e74c3c` | Error messages, destructive actions |
| **Warning** | `#f39c12` | Warning messages, caution content   |
| **Info**    | `#3498db` | Info messages, system updates       |

### Neutral Colors

| Color     | Hex       | Usage                          |
| --------- | --------- | ------------------------------ |
| **Dark**  | `#1a1a1a` | Body text, deep content        |
| **Light** | `#f8f9fa` | Backgrounds, light surfaces    |
| **Gray**  | `#6c757d` | Secondary text, disabled state |

### Gradients

**Primary Gradient:**

```css
background: linear-gradient(135deg, #ff6b35 0%, #ff9a56 100%);
```

Used for: CTA buttons, headings, links

**Secondary Gradient:**

```css
background: linear-gradient(135deg, #004e89 0%, #00618a 100%);
```

Used for: Navbar, staff-specific elements

**Bi-color Gradient:**

```css
background: linear-gradient(135deg, #004e89 0%, #ff6b35 100%);
```

Used for: Section headings, important text

---

## 📝 Typography System

### Font Stack

```css
font-family:
  -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen", "Ubuntu",
  "Helvetica Neue", sans-serif;
```

**Reasoning:** System fonts provide optimal performance and native look on all platforms

### Font Sizes (Scale)

| Size     | Value     | Usage                |
| -------- | --------- | -------------------- |
| **xs**   | `0.8rem`  | Small labels, badges |
| **sm**   | `0.9rem`  | Secondary text       |
| **base** | `1rem`    | Body text, default   |
| **md**   | `1.05rem` | Subheadings          |
| **lg**   | `1.2rem`  | Small headings       |
| **xl**   | `1.5rem`  | Medium headings      |
| **2xl**  | `1.8rem`  | Page titles          |
| **3xl**  | `2.2rem`  | Section headings     |
| **4xl**  | `2.8rem`  | Hero titles          |
| **5xl**  | `3.5rem`  | Large hero titles    |

### Font Weights

| Weight         | Value | Usage                       |
| -------------- | ----- | --------------------------- |
| **Regular**    | `400` | Body text, paragraphs       |
| **Medium**     | `600` | Labels, smaller headings    |
| **Bold**       | `700` | Headings, strong emphasis   |
| **Extra Bold** | `800` | Hero titles, major headings |

### Line Height

```css
line-height: 1.6; /* Default body */
line-height: 1.2; /* Headings (tighter) */
line-height: 1.8; /* Long-form text */
```

### Letter Spacing

| Usage          | Value     |
| -------------- | --------- |
| Headings       | `1-2px`   |
| Buttons        | `0.5-1px` |
| Uppercase text | `1-1.5px` |
| Labels         | `0.5px`   |

---

## 🧩 Components & Patterns

### Buttons

**Primary Button (CTA)**

```css
.btn-primary-custom {
  background: linear-gradient(135deg, #ff6b35 0%, #ff9a56 100%);
  color: white;
  padding: 14px 20px;
  border-radius: 10px;
  font-weight: 700;
  letter-spacing: 0.5px;
  box-shadow: 0 8px 20px rgba(255, 107, 53, 0.3);
  transition: var(--transition);
}

.btn-primary-custom:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 30px rgba(255, 107, 53, 0.4);
}
```

**Secondary Button**

```css
.btn-secondary-custom {
  background: linear-gradient(135deg, #004e89 0%, #00618a 100%);
  color: white;
  /* Same styling as primary */
}
```

**Outline Button**

```css
.btn-outline-custom {
  background: transparent;
  color: var(--primary);
  border: 2px solid var(--primary);
  /* Hover: background becomes primary */
}
```

### Forms

**Form Group**

```css
.form-group {
  margin-bottom: 24px;
}

.form-group label {
  font-weight: 700;
  color: var(--secondary);
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.95rem;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 14px 16px;
  border: 2px solid #e0e0e0;
  border-radius: 10px;
  font-size: 0.95rem;
  transition: var(--transition);
  font-weight: 500;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 5px rgba(255, 107, 53, 0.12);
}
```

### Cards

**Modern Card**

```css
.card-modern {
  background: white;
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-lg);
  overflow: hidden;
  transition: var(--transition);
}

.card-modern:hover {
  box-shadow: var(--shadow-xl);
  transform: translateY(-4px);
}

.card-header-modern {
  background: linear-gradient(
    135deg,
    var(--secondary) 0%,
    var(--secondary-light) 100%
  );
  color: white;
  padding: 24px;
  font-weight: 700;
}

.card-body-modern {
  padding: 24px;
}
```

### Tables

**Modern Table**

```css
.table-modern {
  width: 100%;
  background: white;
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-md);
  overflow: hidden;
  border-collapse: collapse;
}

.table-modern thead {
  background: linear-gradient(
    135deg,
    var(--secondary) 0%,
    var(--secondary-light) 100%
  );
  color: white;
  font-weight: 700;
}

.table-modern th,
.table-modern td {
  padding: 16px 20px;
  border-bottom: 1px solid #e0e0e0;
}

.table-modern tbody tr:hover {
  background: #f8f9fa;
  transition: var(--transition);
}
```

### Badges & Status Indicators

**Badge**

```css
.badge {
  padding: 6px 12px;
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.85rem;
}

.badge-primary {
  background: linear-gradient(
    135deg,
    var(--primary) 0%,
    var(--primary-light) 100%
  );
  color: white;
}
.badge-success {
  background: var(--success);
  color: white;
}
.badge-danger {
  background: var(--danger);
  color: white;
}
.badge-info {
  background: var(--info);
  color: white;
}
```

### Navbar

**Modern Navbar**

```css
.navbar-modern {
  background: linear-gradient(
    90deg,
    var(--secondary) 0%,
    var(--secondary-light) 100%
  );
  box-shadow: var(--shadow-lg);
  padding: 1rem 2rem;
  position: sticky;
  top: 0;
  z-index: 1000;
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.nav-link {
  color: rgba(255, 255, 255, 0.85) !important;
  font-weight: 600;
  transition: var(--transition);
  position: relative;
}

.nav-link:hover {
  color: var(--primary) !important;
  transform: translateY(-2px);
}
```

---

## 📐 Layout Guidelines

### Container Sizes

| Breakpoint  | Max Width | Padding |
| ----------- | --------- | ------- |
| **Desktop** | `1200px`  | `20px`  |
| **Tablet**  | `968px`   | `20px`  |
| **Mobile**  | `100%`    | `15px`  |

### Container Classes

```css
.container-modern {
  width: 100%;
  padding: 40px 20px;
  margin: 0 auto;
}

.page-container {
  max-width: 1200px;
  margin: 0 auto;
}
```

### Common Layout Patterns

**Two-Column Layout (Login/Register)**

```css
.login-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 50px;
  align-items: center;
  max-width: 1200px;
}

@media (max-width: 968px) {
  .login-container {
    grid-template-columns: 1fr;
    gap: 30px;
  }
}
```

**CSS Grid Menu**

```css
.menu-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 25px;
  animation: fadeIn 0.6s ease;
}
```

**Full-Screen Hero**

```css
.hero-section {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  padding: 40px 20px;
}
```

---

## ✨ Animation & Transitions

### Timing Functions

```css
--transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); /* Standard */
--transition-fast: all 0.2s cubic-bezier(0.4, 0, 0.2, 1); /* Quick */
```

### Common Animations

**Slide Up**

```css
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.element {
  animation: slideUp 0.6s ease;
}
```

**Fade In**

```css
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.element {
  animation: fadeIn 0.4s ease;
}
```

**Hover Elevation**

```css
.element:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-xl);
  transition: var(--transition);
}
```

---

## 📱 Responsive Design

### Breakpoints

```css
/* Desktop: 1200px+ */
Default styles apply

/* Tablet: 968px - 1199px */
@media (max-width: 968px) {
}

/* Mobile: Below 768px */
@media (max-width: 480px) {
}
```

### Responsive Strategy

1. **Mobile-First:** Code for mobile, then add desktop enhancements
2. **Flexible Layouts:** Use CSS Grid and Flexbox over floats
3. **Responsive Images:** `max-width: 100%` for all images
4. **Touch-Friendly:** Minimum 44px tap targets
5. **Readable Text:** Min 16px on mobile

### Common Responsive Patterns

**Grid Adaptation**

```css
/** Desktop: 3 columns **/
grid-template-columns: repeat(3, 1fr);

/** Tablet: 2 columns **/
@media (max-width: 968px) {
  grid-template-columns: repeat(2, 1fr);
}

/** Mobile: 1 column **/
@media (max-width: 480px) {
  grid-template-columns: 1fr;
}
```

**Font Size Scaling**

```css
h1 {
  font-size: 2.8rem;
} /** Desktop **/

@media (max-width: 968px) {
  h1 {
    font-size: 2.2rem;
  }
}

@media (max-width: 480px) {
  h1 {
    font-size: 1.8rem;
  }
}
```

---

## ♿ Accessibility

### Color Contrast

- **AA Standard:** 4.5:1 for text, 3:1 for graphics
- **Test with:** WebAIM Contrast Checker

### Semantic HTML

- Use `<button>` for buttons (not `<a>` or `<div>`)
- Use `<label>` for form inputs
- Use heading hierarchy: `<h1>` → `<h2>` → `<h3>`

### ARIA Labels

```html
<i class="fas fa-search" aria-label="Search icon"></i>
<button aria-label="Close menu">×</button>
```

### Keyboard Navigation

- All interactive elements must be keyboard accessible
- Tab order: `tabindex` only when necessary
- Focus visible: `:focus` states must be clear

### Icon Usage

- Always pair icons with text labels
- Icons alone: provide `aria-label`
- Example: `<i class="fas fa-user"></i> Profile`

---

## 📋 Implementation Checklist

When creating or modifying pages, ensure:

- [ ] Uses `base.html` for template inheritance
- [ ] Includes navbar with `.navbar-modern` class
- [ ] Uses CSS variables from `:root` (no hardcoded colors)
- [ ] Forms follow `.form-group` pattern
- [ ] Buttons use `.btn-*-custom` classes
- [ ] Cards use `.card-modern` wrapper
- [ ] Uses Font Awesome icons consistently
- [ ] Responsive breakpoints at 968px and 480px
- [ ] Proper heading hierarchy (h1 → h2 → h3)
- [ ] Accessible color contrast (4.5:1 ratio)
- [ ] Touch targets minimum 44px
- [ ] Images have alt text
- [ ] Links have visible focus states
- [ ] Interactive elements have hover states
- [ ] Loading states where applicable
- [ ] Error/success messages follow semantic colors
- [ ] Mobile viewport meta tag present
- [ ] Bootstrap 5 CDN included
- [ ] Font Awesome 6.4.0 CDN included
- [ ] Custom styles.css linked

---

## 📞 Questions or Updates

For design system updates or clarifications:

1. Update this document
2. Increment version number
3. Document the change in changelog
4. Inform team of updates

**Current Version:** 1.0 (March 24, 2026)

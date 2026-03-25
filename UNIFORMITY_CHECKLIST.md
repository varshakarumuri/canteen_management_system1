# Uniformity Verification Checklist

**Quick Reference for Ensuring Design Consistency**

---

## 📋 Page Uniformity Audit

### Navigation & Branding

All pages should have:

- [ ] Navigation bar with `.navbar-modern` class
- [ ] Branding: `<i class="fas fa-utensils"></i>E-Canteen` or similar
- [ ] Sticky positioning (`position: sticky; top: 0;`)
- [ ] All nav links with Font Awesome icons
- [ ] Blue gradient background: `#004e89` → `#00618a`
- [ ] Active/hover states on links

**Quick Check:**

```html
✅
<nav class="navbar navbar-modern navbar-expand-lg">
  ✅ <i class="fas fa-utensils"></i>E-Canteen ✅ All links have icons and text
</nav>
```

### Page Structure

All pages should have:

- [ ] `{% extends 'base.html' %}`
- [ ] `{% block navbar %}` with nav content
- [ ] `{% block content %}` with main content
- [ ] `.container-modern` wrapper
- [ ] `.page-container` inner wrapper
- [ ] Proper heading hierarchy (h1 first)

**Quick Check:**

```html
✅ {% extends 'base.html' %} ✅
<div class="container-modern">
  ✅
  <div class="page-container">
    ✅
    <h1>Page Title</h1>
  </div>
</div>
```

### Color Usage

All pages should use:

- [ ] **Primary Color** (`#ff6b35`) - User flow buttons, highlights
- [ ] **Secondary Color** (`#004e89`) - Headings, navbar, staff flow
- [ ] **Semantic Colors** - Success (#27ae60), Danger (#e74c3c), Warning (#f39c12), Info (#3498db)
- [ ] NO hardcoded hex colors - use `var(--*)`
- [ ] Consistent gradient direction: `135deg`

**Quick Check:**

```css
✅ background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
✅ color: var(--secondary);
❌ color: #ff6b35; (WRONG - use CSS variable)
```

### Buttons

All buttons should have:

- [ ] Font Awesome icon inside
- [ ] Proper button class (`.btn-primary-custom`, `.btn-secondary-custom`, etc.)
- [ ] Padding: `14px 20px`
- [ ] Border radius: `10px`
- [ ] Font weight: `700`
- [ ] Box shadow: `0 8px 20px rgba(...)`
- [ ] Hover effect: `transform: translateY(-3px)`

**Quick Check:**

```html
✅
<button class="btn-primary-custom">
  ✅ <i class="fas fa-check"></i> Submit ✅ 14px 20px padding (matches pattern)
  ✅ 10px border radius (matches pattern)
</button>
```

### Forms

All forms should have:

- [ ] `.form-group` wrapper for each field
- [ ] Label with icon: `<i class="fas fa-*"></i>Label`
- [ ] Input with proper classes and styling
- [ ] Focus state: border color change + glow effect
- [ ] 2px border, rounded 10px
- [ ] Consistent padding: `14px 16px`

**Quick Check:**

```html
✅
<div class="form-group">
  ✅ <label><i class="fas fa-user"></i>Full Name</label> ✅
  <input class="form-group input" ... /> ✅ Focus: border color changes to
  #ff6b35
</div>
```

### Cards & Content

All cards should have:

- [ ] `.card-modern` wrapper
- [ ] `.card-header-modern` for title (if needed)
- [ ] `.card-body-modern` for content
- [ ] White background
- [ ] Border radius: `16px`
- [ ] Shadow: `var(--shadow-lg)`
- [ ] Hover lift effect: `translateY(-4px)`

**Quick Check:**

```html
✅
<div class="card-modern">
  ✅
  <div class="card-header-modern">
    ✅
    <div class="card-body-modern">
      ✅ Box-shadow: 0 10px 30px rgba(0,0,0,0.12)
    </div>
  </div>
</div>
```

### Typography

All pages should have:

- [ ] Page title in h1 (font-size: 2.8rem)
- [ ] Section headers in h2 (font-size: 2.2rem)
- [ ] Subsections in h3
- [ ] Proper line-height: `1.6`
- [ ] Color: Headings use `var(--secondary)`, body text uses `#2c3e50`
- [ ] Font weight hierarchy: 400 (body) → 600 (labels) → 700 (headings) → 800 (hero)

**Quick Check:**

```html
✅
<h1>Main Title</h1>
/* font-size: 2.8rem */ ✅
<h2>Section Title</h2>
/* font-size: 2.2rem */ ✅
<p>Body text</p>
/* font-size: 1rem, line-height: 1.6 */
```

### Icons

All elements should have:

- [ ] All buttons have icons
- [ ] All nav links have icons
- [ ] All headings/labels have icons
- [ ] Icons use Font Awesome 6.4.0
- [ ] Icon + text paired (not icon alone)
- [ ] Consistent icon sizing

**Quick Check:**

```html
✅ <button><i class="fas fa-save"></i> Save</button> ✅
<a href="..."><i class="fas fa-user"></i> Profile</a> ✅
<h2><i class="fas fa-list"></i> Items</h2>
```

### Responsive Design

All pages should work at:

- [ ] Desktop (1200px+) - Full two-column layouts where applicable
- [ ] Tablet (968px) - Single column, stacked layouts
- [ ] Mobile (480px) - Single column, optimized padding/font

**Media Queries Used:**

```css
@media (max-width: 968px) {
  /* Tablet adjustments */
}
@media (max-width: 480px) {
  /* Mobile adjustments */
}
```

**Quick Check:**

- [ ] Desktop: Two-column layouts render properly
- [ ] Tablet: Layouts stack to single column
- [ ] Mobile: Content is readable, buttons are 44px+ tall

### Accessibility

All pages should have:

- [ ] Color contrast 4.5:1 on all text
- [ ] Proper heading hierarchy (h1, h2, h3, not skipped)
- [ ] Alt text on all images
- [ ] Visible focus states (`:focus` should be clear)
- [ ] Labels associated with form inputs
- [ ] ARIA labels where needed

**Quick Check:**

```html
✅ <img alt="Menu item photo" ... /> ✅ <label for="name">Full Name</label> ✅
<input id="name" ... /> ✅ :focus { outline with 4px solid color; }
```

---

## 🚨 Red Flags (Things to Fix)

| Red Flag                            | Fix                                         |
| ----------------------------------- | ------------------------------------------- |
| Hardcoded colors (`#ff6b35`)        | Replace with `var(--primary)`               |
| Inline styles (`style=""`)          | Move to CSS classes in `styles.css`         |
| Random CSS file created             | Move all styles to `styles.css`             |
| Missing navbar                      | Add navbar from template                    |
| Template doesn't extend `base.html` | Add `{% extends 'base.html' %}`             |
| Button without icon                 | Add Font Awesome icon                       |
| Text without heading hierarchy      | Organize with h1, h2, h3                    |
| Not responsive at 480px             | Add media query for mobile                  |
| 30px border radius                  | Use `10px` or `16px` (standard)             |
| Green buttons for everything        | Use semantic colors: success/danger/warning |
| Buttons with purple/pink            | Use primary orange or secondary blue        |
| Image > 500KB                       | Optimize or reduce dimensions               |
| Text color hard to read             | Check contrast, use proper colors           |

---

## 📊 Design System Compliance Matrix

### User Pages

| Page            | Structure | Color | Responsive | Icons | Status      |
| --------------- | --------- | ----- | ---------- | ----- | ----------- |
| Login           | ✅        | ✅    | ✅         | ✅    | ✅ COMPLETE |
| Register        | ✅        | ✅    | ✅         | ✅    | ✅ COMPLETE |
| Menu            | ✅        | ✅    | ✅         | ✅    | ✅ COMPLETE |
| Cart            | ✅        | ✅    | ✅         | ✅    | ✅ COMPLETE |
| Active Orders   | ✅        | ✅    | ✅         | ✅    | ✅ COMPLETE |
| Profile         | ✅        | ✅    | ✅         | ✅    | ✅ COMPLETE |
| Change Password | ✅        | ✅    | ✅         | ✅    | ✅ COMPLETE |
| Verify Email    | ✅        | ✅    | ✅         | ✅    | ✅ COMPLETE |
| Forgot Password | ✅        | ✅    | ✅         | ✅    | ✅ COMPLETE |
| Reset Password  | ✅        | ✅    | ✅         | ✅    | ✅ COMPLETE |
| Receipt         | ✅        | ✅    | ✅         | ✅    | ✅ COMPLETE |

### Staff Pages

| Page             | Structure | Color | Responsive | Icons | Status      |
| ---------------- | --------- | ----- | ---------- | ----- | ----------- |
| Login            | ✅        | ✅    | ✅         | ✅    | ✅ COMPLETE |
| Orders           | ✅        | ✅    | ✅         | ✅    | ✅ COMPLETE |
| Profile          | ✅        | ✅    | ✅         | ✅    | ✅ COMPLETE |
| Completed Orders | ✅        | ✅    | ✅         | ✅    | ✅ COMPLETE |

### Public Pages

| Page | Structure | Color | Responsive | Icons | Status      |
| ---- | --------- | ----- | ---------- | ----- | ----------- |
| Home | ✅        | ✅    | ✅         | ✅    | ✅ COMPLETE |

---

## ✨ Uniformity Score Card

Check pages using this scoring system:

**Perfect Score: 100 points**

| Category      | Max Points | Criteria                                    |
| ------------- | ---------- | ------------------------------------------- |
| Structure     | 20         | Extends base, has blocks, proper containers |
| Colors        | 15         | Uses CSS variables, consistent gradients    |
| Buttons       | 15         | Has icons, proper styling, hover effects    |
| Forms         | 15         | Groups, labels with icons, focus states     |
| Icons         | 10         | All interactive elements have icons         |
| Typography    | 10         | Proper hierarchy, consistent sizing         |
| Responsive    | 10         | Works at 480px, 768px, 1200px               |
| Accessibility | 5          | Contrast, alt text, focus states            |

**Scoring:**

- **100 points** = Perfect! Release to production
- **90-99 points** = Excellent! Minor tweaks only
- **80-89 points** = Good! Document known issues
- **70-79 points** = Needs work. Create tickets
- **<70 points** = Do not use. Requires redesign

---

## 🔍 Quick Audit Script

Use this to rapidly check page consistency:

```python
# Check list (for developers):
1. Open page in browser at Developer Tools
2. Check Console for errors (should be 0)
3. Resize window to 480px, 768px, 1200px
4. Click all buttons/links to verify functionality
5. Tab through page with keyboard (accessibility)
6. Inspect element colors (should use CSS variables)
7. Verify all images have alt text
8. Check heading hierarchy (h1 first, no skips)
```

---

## 📝 Template Audit Report

**Use this template to document issues:**

```
Page: _______________
Date: _______________
Auditor: _____________

Issues Found:
1. [ ] Issue description → Fix needed
2. [ ] Issue description → Fix needed
3. [ ] Issue description → Fix needed

Score: ___/100

Priority:  [ ] Critical  [ ] High  [ ] Medium  [ ] Low

Notes:
_________________________________

Action Items:
- [ ] Fix issue #1
- [ ] Fix issue #2
- [ ] Re-audit after fixes
```

---

## 🎯 Maintenance Checklist (Monthly)

- [ ] Review all template files for consistency
- [ ] Check CSS file for unused/duplicate rules
- [ ] Update documentation if changes made
- [ ] Test responsive design at all breakpoints
- [ ] Verify all links work correctly
- [ ] Check accessibility with screen reader
- [ ] Profile performance using DevTools
- [ ] Review git commit messages
- [ ] Update this checklist if needed

---

**Last Updated:** March 24, 2026  
**Next Review:** April 24, 2026

---
name: accessibility-code
description: Review frontend CODE for accessibility — semantic HTML, ARIA, keyboard operability, focus management, and WCAG conformance at the implementation level. Use when auditing components/markup for a11y, fixing keyboard or screen-reader problems in code, meeting WCAG in a build, or when the user says "make this accessible", "a11y review of this component", "keyboard navigation", "ARIA", "screen reader support", or "WCAG in code". This is the code-level complement to the design-level accessibility skills in designer-skills (WCAG design review) and awesome-design-skills.
---

# Accessibility (code level)

Role: make the implementation operable by everyone — keyboard, screen reader, zoom,
reduced motion. This is the **code** pass; design-level WCAG/contrast review lives in
`designer-skills` (`accessibility-audit`, `critique-color`) and `awesome-design-skills`.

## Checklist (WCAG 2.2 AA, implementation)
- **Semantic HTML first**: real `<button>`, `<a href>`, `<nav>`, `<main>`, `<label>`,
  headings in order. A `<div onclick>` is not a button — it loses focus, Enter/Space, and
  role for free. Reach for ARIA only when HTML can't express it.
- **Keyboard**: every interactive element reachable and operable by keyboard; logical tab
  order; visible focus indicator (don't `outline:none` without a replacement); no keyboard
  traps; custom widgets implement expected keys (Esc closes, arrows in menus).
- **Focus management**: move focus into an opened modal, trap it there, return it on close;
  manage focus on route change and after async content loads.
- **Forms**: every input has a programmatic `<label>`/`aria-label`; errors tied via
  `aria-describedby`; required/invalid state conveyed, not by color alone.
- **Images/media**: meaningful `alt`; decorative images `alt=""`; captions for media.
- **ARIA correctly**: correct roles/states (`aria-expanded`, `aria-selected`,
  `aria-live` for async updates); never ARIA that contradicts the element; no `aria-hidden`
  on focusable content.
- **Contrast & zoom**: text contrast ≥ 4.5:1 (3:1 large); usable at 200% zoom / 400%
  reflow; not conveying meaning by color alone.
- **Motion**: honor `prefers-reduced-motion` (see `motion-dev-animations-skill`,
  `animation-principles/12-by-problem-type/motion-sickness`).

## Red flags
- `<div>`/`<span>` with `onClick` and no role/tabindex/keyboard handler.
- `outline: none` with no visible focus replacement.
- Modal that doesn't trap or restore focus.
- Inputs with placeholder-as-label only.
- Icon-only buttons with no accessible name.

Grounding: WCAG; OWASP is not relevant here. Related: [[ux-review]], [[frontend-code-review]].

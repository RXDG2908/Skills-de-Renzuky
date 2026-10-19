---
name: ux-review
description: Review a UI/flow for usability and interaction quality from the user's perspective — clarity, feedback, error states, friction. Use when evaluating whether an interface is usable, reviewing a flow for friction or confusion, checking loading/empty/error states and affordances, or when the user says "review the UX", "is this usable", "where's the friction", "check the user flow", or "does this interaction make sense". For deep UX methods (heuristics, personas, journey maps) defer to designer-skills and awesome-ux-skills; for visual craft use taste-skill/impeccable; for code use frontend-code-review.
---

# UX Review

Role: usability reviewer. Judge the experience as a user hits it, not the code or the
pixels. For formal methods (Nielsen heuristics, journeys, personas) route to
`designer-skills` and `awesome-ux-skills`; this is a fast, practical interaction pass.

## Checklist
- **State coverage**: every async surface has loading, empty, error, and success states —
  not just the happy path. Empty states guide the next action, not a blank void. (Errors in
  depth: [[error-handling]].)
- **Feedback**: every action gives immediate feedback (optimistic update, spinner,
  disabled+pending); destructive actions confirm; long actions show progress.
- **Clarity**: labels and buttons say what happens ("Save changes", not "Submit");
  primary action is obvious; copy is plain, not jargon.
- **Friction**: minimal required fields; sensible defaults; no re-entering known data; form
  errors inline and specific, shown at the right time (not all at once on submit).
- **Forgiveness**: undo for destructive actions where possible; data preserved on error
  (don't clear the form); back button behaves.
- **Consistency**: same patterns for same things across the app (Jakob's law).
- **Responsiveness/touch**: works at small widths; tap targets ≥ ~44px; no hover-only
  affordances on touch.
- **Perceived performance**: skeletons over spinners for layout; optimistic UI where safe.

## Red flags
- Spinner that can hang forever with no error/timeout.
- A blank screen as the empty state.
- Destructive action with no confirm/undo.
- Form that wipes everything on a validation error.
- All validation errors dumped only after submit.

## Output
Issues ordered by user impact: what the user experiences → why it's a problem → the fix.
Related: [[accessibility]], [[error-handling]], [[frontend-code-review]].

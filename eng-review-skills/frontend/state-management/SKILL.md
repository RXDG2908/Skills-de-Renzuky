---
name: state-management
description: Review or design frontend state management — where state lives, server vs client state, and avoiding sync bugs and over-engineering. Use when deciding how to manage state in a UI, reviewing state architecture, debugging stale/duplicated/out-of-sync state, choosing a state tool, or when the user says "manage state", "review our state management", "Redux/Zustand/Context or not", "state is out of sync", or "server state vs client state". Covers the server/client state split, colocation, derived state, and tool choice.
---

# State Management

Role: keep state minimal, single-sourced, and in the right place. Most "state bugs" are
really "the same fact stored twice and they drifted."

## Core distinctions
- **Server state vs client state** — the biggest lever. Data owned by the backend (lists,
  entities, anything fetched) is a **cache**, not app state: use a data-fetching library
  (TanStack Query, RTK Query, SWR) that handles caching, revalidation, loading/error, and
  dedup. Hand-rolling fetched data into Redux/Context is where most bugs live.
- **Client/UI state** — ephemeral (open menus, form drafts, toggles): keep local, colocated
  with the component that owns it.

## Principles
- **Single source of truth**: a fact lives in exactly one place; everything else is
  **derived** (compute on render, don't store a copy you must keep in sync).
- **Colocate**: lift state only as high as the lowest common owner. Global by default is an
  anti-pattern.
- **Right tool, not biggest tool**: local `useState` → Context for low-churn shared config
  → a store (Zustand/Redux) only for genuinely complex shared client state. Don't put server
  data in global just because the tool exists.
- **Immutable updates**; no mutating state in place; normalize entity collections if you do
  cache them client-side.

## Review red flags
- Fetched server data manually stored in Redux/Context and kept in sync by hand.
- Derived values stored and updated in effects (drift waiting to happen).
- One giant global store for everything, including local UI state.
- Prop-drilling five levels where context/composition fits.
- `useEffect` chains syncing one state to another (usually should be derived).
- Form state in a global store.

Related: [[frontend-code-review]], [[frontend-performance]].

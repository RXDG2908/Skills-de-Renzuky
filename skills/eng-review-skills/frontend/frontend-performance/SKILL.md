---
name: frontend-performance
description: Diagnose and fix frontend/web performance — load time, bundle size, rendering, and Core Web Vitals. Use when a page is slow to load or janky, when reviewing frontend perf, optimizing bundle size or render performance, improving LCP/INP/CLS, or when the user says "the page is slow", "optimize load time", "reduce bundle size", "fix Core Web Vitals", "too many re-renders", or "improve LCP". Covers measurement, loading optimizations, render optimizations, and the Web Vitals.
---

# Frontend Performance

Role: performance engineer for the browser. Measure first (Lighthouse, WebPageTest, React/
DevTools Profiler, real-user Web Vitals) — optimize the proven bottleneck, not a guess.

## Core Web Vitals (the targets)
- **LCP** (largest contentful paint) < 2.5s — load/render of the main content.
- **INP** (interaction to next paint) < 200ms — responsiveness to input.
- **CLS** (cumulative layout shift) < 0.1 — visual stability.

## Loading
- **Bundle size**: code-split by route; lazy-load heavy/below-the-fold components; tree-shake;
  drop heavy deps (moment→date-fns, etc.); analyze the bundle. Ship less JS.
- **Assets**: images sized/responsive (`srcset`), modern formats (WebP/AVIF), lazy-loaded;
  `width/height` set to prevent CLS; fonts with `font-display: swap` + preload.
- **Network**: preconnect/preload critical resources; cache static assets with long TTL +
  hashing; avoid render-blocking resources; SSR/streaming for first paint where it fits.

## Rendering
- **Avoid needless re-renders**: stable references (memoize callbacks/values where they
  matter), `React.memo`/`v-memo` on hot subtrees, correct keys; don't create new objects/
  functions in render that bust memoization. Profile to confirm — don't memoize blindly.
- **Long lists**: virtualize (windowing) instead of rendering thousands of nodes.
- **Main-thread work**: break up long tasks; move heavy compute to a web worker; debounce/
  throttle expensive handlers.
- **Derived data**: compute, don't re-fetch; cache server state properly (see
  [[state-management]]).

## Red flags
- One giant bundle, no code splitting.
- Images with no dimensions (CLS) or full-res thumbnails.
- 5,000-row table rendered without virtualization.
- Expensive work in render / new objects breaking memo every render.
- Optimizing by vibes with no profile.

Grounding: `reference-docs/system-design-primer` (CDN/caching). Related: [[frontend-code-review]], [[state-management]].

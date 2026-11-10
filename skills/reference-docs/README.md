# reference-docs — NOT skills

Authoritative engineering/security reference material cloned for grounding, **not**
agent skills (no `SKILL.md`). The `eng-review-skills/` skills cite these. `use-skills`
should read from here when it needs source-of-truth detail, but never invoke these as
skills. Each keeps its own upstream LICENSE.

| Folder | Source | License | Use for |
|---|---|---|---|
| `CheatSheetSeries/` | OWASP/CheatSheetSeries (sparse: `cheatsheets/` only, 137 md) | CC-BY-SA 4.0 | Security controls: input validation, authn/z, crypto, API, SQLi, XSS, etc. |
| `ASVS/` | OWASP/ASVS (sparse: `5.0/en`) | CC-BY-SA | Application Security Verification Standard — requirement checklists by level |
| `wstg/` | OWASP/wstg | CC-BY-SA | Web Security Testing Guide — how to test each vuln class |
| `API-Security/` | OWASP/API-Security (2023 edition kept; 2019 translations dropped) | CC-BY-SA | API Security Top 10 (BOLA, broken auth, etc.) |
| `eng-practices/` | google/eng-practices | CC-BY 3.0 | Google's code-review guide (reviewer + author sides) |
| `system-design-primer/` | donnemartin/system-design-primer | CC-BY 4.0 | Scalability, caching, sharding, consistency, rate limiting, idempotency |
| `clean-code-javascript/` | ryanmcdermott/clean-code-javascript | MIT | Clean Code adapted to JS |
| `redis-doc/` | redis/redis-doc | historical docs | Redis commands/patterns — distributed locks (Redlock), rate limiting |

## Not cloned (on purpose)

- `refactoring.guru` and `martinfowler.com` — **websites with copyrighted content**
  (refactoring.guru sells its material). Not git repos; not scraped or redistributed.
  Use them in a browser as a human reference.
- `dotnet-architecture/eShopOnWeb` — a full sample .NET application, not reference docs
  or a skill. Skipped.

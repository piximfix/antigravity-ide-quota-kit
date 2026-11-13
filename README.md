# Antigravity IDE Quota Kit (`.antigravityignore` Presets & 5-Hour Context Optimizer)

A lightweight, open-source developer toolkit to prevent **"Rate Limit Exceeded"** interruptions in Google Antigravity IDE by excluding heavy dependency trees, build artifacts, lockfiles, and binary directories before agent context indexing runs.

> Complete 5-hour quota documentation: [How to Fix Google Antigravity Rate Limit Exceeded Error](https://piximplanet.com/how-to-fix-google-antigravity-rate-limit-exceeded/)

## Why Context Pruning Matters in Google Antigravity

Google Antigravity agent loops (`Orchestrator`, `Gemini 4 Carbon`, `Gemini 4 Argon`, `Gemini 4 Hydrogen`, `Gemini 3.8 Flash`, `Claude Opus 5.5`, `Claude Sonnet 5.5`, and `GPT-OSS 120B`) evaluate repository context inside rolling **5-hour quota windows**. Scanning unignored directories such as `node_modules/`, `.next/`, `vendor/`, `dist/`, `.git/`, or large binary assets consumes token headroom rapidly without improving code accuracy.

Dropping a tuned `.antigravityignore` at your project root and auditing large directories keeps agent prompts focused so coding capacity lasts across multi-hour builds.

## Files Included

- [`.antigravityignore`](./.antigravityignore) — Universal baseline ignore rules for JS, Python, PHP, and static assets.
- [`nextjs.antigravityignore`](./nextjs.antigravityignore) — Ignore preset tailored for Next.js, React, TypeScript, Turbo, and Vercel builds.
- [`wordpress.antigravityignore`](./wordpress.antigravityignore) — Ignore preset tailored for WordPress themes, plugins, Composer `vendor/`, `wp-content/uploads/`, and WooCommerce asset caches.
- [`python.antigravityignore`](./python.antigravityignore) — Ignore preset tailored for Python (`venv/`, `.venv/`, `__pycache__/`, `.pytest_cache/`, checkpoints, datasets).
- [`audit_context_size.py`](./audit_context_size.py) — Zero-dependency Python script to scan your local repo and flag oversized folders/files before starting an Antigravity agent session.
- [`index.html`](./index.html) — Live reference portal & 20x solo plan comparison table (GitHub Pages: [piximfix.github.io/antigravity-ide-quota-kit](https://piximfix.github.io/antigravity-ide-quota-kit/)).

## Quick Start

1. Copy the matching template to your project root as `.antigravityignore`:
   ```bash
   cp nextjs.antigravityignore /path/to/your-project/.antigravityignore
   ```
2. Audit oversized folders before running long autonomous coding tasks:
   ```bash
   python audit_context_size.py /path/to/your-project
   ```
3. Read the complete rolling-window optimization walkthrough: [Google Antigravity 5-Hour Quota Rules & .antigravityignore Guide](https://piximplanet.com/how-to-fix-google-antigravity-rate-limit-exceeded/).

## Verified 20x Solo Coding Plan Reference Matrix

When standard limits are not enough for sustained full-day agentic engineering, compare all verified solo 20x workspace plans on the [PiximPlanet Google Antigravity Hub](https://piximplanet.com/antigravity/):

| Plan | Primary Focus | Key Allowances & Highlights | Rate (INR) | Reference Page |
| :--- | :--- | :--- | :--- | :--- |
| **Essential Plan** | Solo Coding + Entry Video | 20x solo coding quota + 5,000 Flow credits + Nano Banana Ultra + 30 TB cloud | ₹7,039 / 1M | [Google AI Ultra 20x Essential Plan](https://piximplanet.com/product/google-ai-ultra-20x/) |
| **Pro Dedicated Plan** | Pure Dedicated Coding | Pure 20x solo coding quota (0 Flow) + 30 TB cloud + 30-day warranty | ₹8,517 / 1M | [Antigravity Ultra 20x Pro Plan](https://piximplanet.com/product/antigravity-ultra-20x-pro-dedicated-quota/) |
| **Solo Flex Plan** | 1M / 3M Flexible Coding | Pure 20x solo coding (0 Flow) + Claude Opus 5.5 + 30 TB cloud + 1M or 3M term | ₹9,432 / 1M · ₹23,932 / 3M | [Antigravity Ultra 20x Solo Flex Plan](https://piximplanet.com/product/antigravity-ultra-20x-solo-flex-plan/) |
| **Full Quota Plan** | Sustained Pure Coding | Full solo 20x coding quota + Orchestrator + GPT-OSS 120B + 30 TB cloud (1M & 3M) | ₹11,037 / 1M · ₹24,622 / 3M | [Antigravity Ultra 20x Full Quota Plan](https://piximplanet.com/product/antigravity-ultra-20x-full-quota/) |
| **Private Limit + Image** | Coding + Image Generation | Full private 20x coding quota + Nano Banana Image AI (No-Flow-Video rule) | ₹11,192 / 1M | [Antigravity 20x Private Limit Plan](https://piximplanet.com/product/antigravity-20x-private-limit-image/) |
| **Coding Agents Plan** | Terminal & Agentic Loops | Full private 20x coding limit + terminal CLI dev workflows (0 Flow) | ₹11,262 / 1M | [Antigravity 20x Coding Agents Plan](https://piximplanet.com/product/antigravity-20x-coding-agents-plan/) |
| **25K Flow Suite** | Complete Coding + Veo 3.1 | Personal X20 coding + 25,000 Veo 3.1 Flow credits + Nano Banana Pro + 30 TB | ₹12,669 / 1M | [Google AI Ultra 20x 25K Flow Suite](https://piximplanet.com/product/google-ai-ultra-20x-25k-flow-plan/) |

## License & Attribution

MIT License. Independent open-source workflow presets and nominative compatibility reference documentation. All third-party trademarks belong to their respective owners.

# .ai/PROJECT.md Template

Generated at the root of every scaffolded project. Adapt based on actual project type and choices.

---

# {ProjectName}

## Tech Stack

- **Framework**: {React 18 / Vue 3 / Next.js 14 / Nuxt 3}
- **Language**: TypeScript
- **Build**: Vite 5
- **CSS**: Sass (SCSS) + {Tailwind CSS / Ant Design / MUI}
- **State**: {Zustand / Pinia / Redux Toolkit}
- **Router**: {React Router v6 / Vue Router 4 / Next.js App Router}
- **Package Manager**: pnpm
- **Node**: 18+

## Commands

```bash
pnpm dev          # Start dev server (development mode)
pnpm dev:test     # Start dev server (test mode)
pnpm build:test   # Build for test env (Vite handles TS transpilation)
pnpm build:prod   # Build for production (Vite handles TS transpilation)
pnpm preview      # Preview production build
pnpm lint         # Check code style
pnpm lint:fix     # Auto-fix code style
pnpm typecheck    # TypeScript type check
```

## Directory Structure

```
{project-name}/
│
├── .ai/
│   └── PROJECT.md              # This file — AI reference doc
│
├── public/
│   └── favicon.ico             # Site favicon
│
├── src/
│   ├── assets/                 # Static assets (images, fonts, etc.)
│   │
│   ├── components/             # Shared/reusable UI components
│   │
│   ├── hooks/                  # Custom React/Vue hooks
│   │
│   ├── layouts/                # Page layout components (header, sidebar, etc.)
│   │
│   ├── pages/                  # Page-level components (one per route)
│   │
│   ├── router/                 # Route configuration
│   │   └── index.{tsx|ts}      # Route definitions
│   │
│   ├── services/               # API layer
│   │   ├── request.ts          # fetch wrapper — interceptors, error handling, auth header
│   │   ├── logger.ts           # Structured logger — levels, rotation, file persistence
│   │   ├── log-export.ts        # Log export (download) + submit (endpoint TBD)
│   │   └── api/
│   │       └── index.ts        # API endpoint functions
│   │
│   ├── stores/                 # State management (Zustand/Pinia/Redux stores)
│   │
│   ├── styles/                 # Global styles
│   │   ├── global.scss         # CSS custom properties + body/html defaults
│   │   ├── reset.scss          # CSS reset / normalize
│   │   └── variables.scss      # Design tokens (colors, spacing, breakpoints, font-sizes)
│   │
│   ├── types/                  # TypeScript type declarations
│   │   └── global.d.ts         # Global types, module declarations
│   │
│   ├── utils/                  # Pure utility functions
│   │   ├── index.ts            # Common helpers (debounce, throttle, deepClone, etc.)
│   │   ├── storage.ts          # Typed localStorage/sessionStorage wrapper
│   │   ├── format.ts           # Date, number, currency formatters
│   │   └── validate.ts         # Form validation rules
│   │
│   ├── App.{tsx|vue}           # Root component — layout + router outlet
│   ├── main.{tsx|ts}           # App entry — mount, global providers, styles
│   └── vite-env.d.ts           # Vite client type reference
│
├── .env                         # Common env (loaded in all modes)
├── .env.development             # Dev env overrides
├── .env.test                    # Test env overrides
├── .env.production              # Prod env overrides
│
├── index.html                   # Vite HTML entry point
├── package.json                 # Dependencies + scripts
├── pnpm-lock.yaml               # Locked dependency versions
├── tsconfig.json                # TypeScript config (paths: @/ → src/)
├── tsconfig.node.json           # TypeScript config for Vite config file
├── vite.config.ts               # Vite config (aliases, plugins, env prefix)
├── .eslintrc.cjs                # ESLint config
└── .prettierrc                  # Prettier config
```

## Conventions

- **Path alias**: `@/` maps to `src/`
- **Import order**: React/Vue → third-party libs → `@/` aliases → relative imports
- **Component naming**: PascalCase for components, camelCase for utilities
- **CSS modules**: Enabled by default (`.module.scss`)
- **Responsive breakpoints**: Mobile (< 768px) → Tablet (768-1023px) → Desktop (≥ 1024px)
- **API calls**: Use `src/services/request.ts` wrapper; never call `fetch()` directly
- **Logging**: Use `logger.child("Module")` from `services/logger.ts`; never use raw `console.log` in production
- **State**: Server state in API layer; UI state in stores; form state local to component

## Environment Variables

| Variable | Dev | Test | Prod | Description |
|---|---|---|---|---|
| `VITE_API_BASE_URL` | `http://localhost:3000` | `https://test-api.example.com` | `https://api.example.com` | API base URL |
| `VITE_APP_TITLE` | `{ProjectName} (Dev)` | `{ProjectName} (Test)` | `{ProjectName}` | App title |
| `VITE_APP_ENV` | `development` | `test` | `production` | Current environment |
| `VITE_LOG_LEVEL` | `info` | `info` | `warn` | Min log level (debug/info/warn/error) |
| `VITE_LOG_SUBMIT_URL` | — | — | — | Log submit endpoint (TBD) |

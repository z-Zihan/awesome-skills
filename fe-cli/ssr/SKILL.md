---
name: fe-cli-ssr
description: >
  Scaffold an SSR (Server-Side Rendering) frontend project using Next.js or Nuxt.
  Features SSR/SSG/ISR, SEO optimization, API routes, middleware, and image optimization.
  Triggered as a sub-skill of fe-cli when user wants SSR/Next.js/Nuxt/服务端渲染 project.
---

# fe-cli-ssr — SSR Project Scaffolding

## Workflow

### Step 1: Gather Options

1. **Framework**: Next.js (React) / Nuxt (Vue)
2. **Styling**: Tailwind CSS / Ant Design / MUI / 纯 SCSS
3. **CSS Preprocessor**: Sass / Less
4. **State Management**: Zustand / Redux Toolkit / Pinia (Nuxt) / None
5. **i18n**: next-intl (Next.js) / @nuxtjs/i18n (Nuxt) / None
6. **Database/ORM**: Prisma / Drizzle / None
7. **Auth**: NextAuth.js / Lucia / None
8. **Testing**: Vitest / Playwright / None
9. **Pre-commit**: husky + lint-staged? (default: No)
10. **Project name**: string

### Step 2: Scaffold

**Next.js:**
```
pnpm create next-app <project-name> --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
```
Note: `--tailwind` flag may not exist in all Next.js versions. If not, manually install tailwind.

**Nuxt:**
```
pnpm dlx nuxi init <project-name> --packageManager pnpm
```

### Step 3: Install Dependencies

| Selection | Packages |
|---|---|
| Sass | `sass` |
| Less | `less` |
| Zustand | `zustand` |
| Redux Toolkit | `@reduxjs/toolkit react-redux` |
| Ant Design | `antd @ant-design/icons @ant-design/v5-patch-for-react-19` |
| Next.js i18n | `next-intl` |
| Nuxt i18n | `@nuxtjs/i18n` |
| Prisma | `prisma @prisma/client` → `pnpm prisma init` |
| NextAuth | `next-auth@beta` |
| Playwright | `@playwright/test` |

### Step 4: Next.js-Specific Structure

```
src/
├── app/
│   ├── layout.tsx            # Root layout with metadata
│   ├── page.tsx              # Home page (SSG by default)
│   ├── loading.tsx           # Loading UI
│   ├── error.tsx             # Error boundary
│   ├── not-found.tsx         # 404 page
│   ├── globals.scss          # Global styles
│   └── (routes)/             # Route groups
├── components/
│   ├── ErrorBoundary.tsx     # Client-side error boundary
│   ├── PageLoading.tsx
│   ├── EmptyState.tsx
│   └── ErrorState.tsx
├── lib/
│   ├── request.ts            # Server-side fetch + client-side fetch
│   └── utils.ts              # Shared utils
├── services/
│   └── api.ts                # API calls (works on server & client)
├── hooks/
│   └── useRequest.ts         # Client-side data fetching
├── stores/                   # State management (client)
├── types/
│   └── global.d.ts
└── middleware.ts             # Next.js middleware (auth, redirects, i18n)
```

### Step 5: Key Templates

**`app/layout.tsx`:**
```tsx
import type { Metadata } from 'next';
import './globals.scss';

export const metadata: Metadata = {
  title: { template: '%s | My App', default: 'My App' },
  description: 'Your app description',
  openGraph: {
    title: 'My App',
    description: 'Your app description',
    url: 'https://example.com',
    siteName: 'My App',
    locale: 'zh_CN',
    type: 'website',
  },
  robots: { index: true, follow: true },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="zh-CN">
      <body>{children}</body>
    </html>
  );
}
```

**`lib/request.ts`** — Universal fetch (works server + client):
```typescript
type RequestOptions = {
  method?: string;
  headers?: Record<string, string>;
  body?: unknown;
  cache?: RequestCache;
  next?: { revalidate?: number; tags?: string[] };
};

class RequestError extends Error {
  constructor(public status: number, message: string, public data?: unknown) {
    super(message);
    this.name = 'RequestError';
  }
}

const BASE_URL = process.env.NEXT_PUBLIC_API_URL || process.env.API_URL || '';

export async function request<T = unknown>(url: string, options: RequestOptions = {}): Promise<T> {
  const { body, headers: customHeaders, ...rest } = options;
  const isServer = typeof window === 'undefined';

  const headers: Record<string, string> = {
    ...(body && !(body instanceof FormData) ? { 'Content-Type': 'application/json' } : {}),
    ...(isServer ? {} : {}),  // Client-side token injection
    ...customHeaders,
  };

  const res = await fetch(`${BASE_URL}${url}`, {
    ...rest,
    headers,
    body: body instanceof FormData ? body : body ? JSON.stringify(body) : undefined,
  });

  if (!res.ok) {
    const errData = await res.json().catch(() => null);
    throw new RequestError(res.status, errData?.message || `HTTP ${res.status}`, errData);
  }

  return res.json();
}
```

**`app/page.tsx`** — Home with SSG:
```tsx
export default async function Home() {
  // Server-side data fetch (SSG by default)
  // const data = await request('/api/some-endpoint', { next: { revalidate: 60 } });

  return (
    <main style={{ maxWidth: 1200, margin: '0 auto', padding: '2rem' }}>
      <h1>Welcome</h1>
    </main>
  );
}
```

**`app/loading.tsx`:**
```tsx
export default function Loading() {
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh' }}>
      Loading...
    </div>
  );
}
```

**`app/error.tsx`:**
```tsx
'use client';
export default function Error({ error, reset }: { error: Error; reset: () => void }) {
  return (
    <div style={{ textAlign: 'center', padding: '4rem' }}>
      <h2>Something went wrong!</h2>
      <p>{error.message}</p>
      <button onClick={reset}>Try again</button>
    </div>
  );
}
```

**`app/not-found.tsx`:**
```tsx
import Link from 'next/link';
export default function NotFound() {
  return (
    <div style={{ textAlign: 'center', padding: '4rem' }}>
      <h2>404 - Page Not Found</h2>
      <Link href="/">Go Home</Link>
    </div>
  );
}
```

**`middleware.ts`** (if auth/i18n selected):
```typescript
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  // Example: redirect unauthenticated users
  // const token = request.cookies.get('token');
  // if (!token && !request.nextUrl.pathname.startsWith('/login')) {
  //   return NextResponse.redirect(new URL('/login', request.url));
  // }
  return NextResponse.next();
}

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
};
```

**`env files`:**
```
.env.local            # Local overrides (gitignored)
.env.development      # NEXT_PUBLIC_API_URL=http://localhost:3000
.env.production       # NEXT_PUBLIC_API_URL=https://api.example.com
```

### Step 6: Nuxt-Specific

For Nuxt, use Nuxt modules and composables instead of Next.js patterns. Key files:
- `nuxt.config.ts` — Module registration, runtime config
- `app.vue` — Root app component
- `pages/` — File-based routing
- `server/api/` — API routes
- `composables/` — Shared composables (useFetch wrapper, useAuth, etc.)
- `middleware/` — Route middleware

### Step 7: Shared Layer + Final

For Next.js projects, adapt shared-base.md files:
- Use `lib/` instead of `src/services/` for universal code
- Use `components/` instead of `src/components/`
- `hooks/` become client-only (add `'use client'` directive)
- Skip `vite.config.ts` and `tsconfig.node.json` (Next.js has its own build system)

Only generate files that make sense for SSR context.

```bash
cd <project-name>
pnpm install
pnpm dev
```

Announce: SSR project with Next.js/Nuxt, URLs, and key features enabled.

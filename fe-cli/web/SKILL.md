---
name: fe-cli-web
description: >
  Scaffold a Web SPA frontend project. For websites, landing pages, and standard single-page apps.
  Triggered as a sub-skill of fe-cli when user wants a web/SPA project type.
---

# fe-cli-web — Web SPA Scaffolding

Handles project scaffolding for standard Web Single Page Applications.

## Workflow

### Step 1: Gather Options

Ask these questions. Skip questions whose answer is implied by the user's initial request.

**Quick mode:** If user provides all options in one message (e.g. "React + Tailwind + Zustand + i18n，叫 my-site"),
skip ALL questions and proceed directly to Step 2.

1. **Framework**: React 19 / Vue 3
2. **Styling**: Tailwind CSS / Ant Design / MUI / 纯 CSS (SCSS)
3. **CSS Preprocessor**: Sass / Less / None (default: Sass if using SCSS approach)
4. **State Management**: Zustand / Redux Toolkit / Pinia (for Vue) / None
5. **Router**: React Router / Vue Router / None
6. **i18n**: react-i18next / vue-i18n / None
7. **Testing**: Vitest / None
8. **Pre-commit hooks**: husky + lint-staged + commitlint? (default: No)
9. **Project name**: string (required)

### Step 2: Scaffold Project

Use `pnpm create vite` as the base:

```
pnpm create vite <project-name> --template react-ts   (for React)
pnpm create vite <project-name> --template vue-ts     (for Vue)
```

Then `cd <project-name>` and install additional dependencies based on selections.

### Step 3: Install Dependencies

| Selection | Packages |
|---|---|
| Tailwind CSS | `tailwindcss @tailwindcss/vite` |
| Ant Design | `antd @ant-design/icons @ant-design/v5-patch-for-react-19` |
| MUI | `@mui/material @emotion/react @emotion/styled @mui/icons-material` |
| Zustand | `zustand` |
| Redux Toolkit | `@reduxjs/toolkit react-redux` |
| React Router | `react-router-dom` |
| Vue Router | `vue-router` |
| i18n (React) | `react-i18next i18next i18next-browser-languagedetector` |
| i18n (Vue) | `vue-i18n` |
| Vitest | `vitest @testing-library/react @testing-library/jest-dom jsdom` (React) |
| Sass | `sass` (built-in Vite support) |
| Less | `less` |
| pre-commit | `husky lint-staged @commitlint/cli @commitlint/config-conventional` |

### Step 4: Configure Vite

Generate `vite.config.ts` based on selections. Use the template from `../references/shared-config.md`.
Add Tailwind plugin if selected: `import tailwindcss from '@tailwindcss/vite'` → `plugins: [react(), tailwindcss()]`

### Step 5: Generate Type-Specific Files

**React projects:**

```
src/
├── components/
│   ├── ErrorBoundary.tsx     # React error boundary with fallback UI
│   ├── PageLoading.tsx       # Full-page loading spinner
│   ├── EmptyState.tsx        # Empty state placeholder
│   └── ErrorState.tsx        # Error state with retry button
├── pages/
│   ├── Home/
│   │   └── index.tsx         # Home page
│   └── NotFound.tsx          # 404 page
├── hooks/
│   └── useRequest.ts         # Data fetching hook (useState + useEffect + request)
├── App.tsx                   # App with router setup + layout
└── main.tsx                  # Entry point
```

`App.tsx` template:
```tsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from '@/pages/Home';
import NotFound from '@/pages/NotFound';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}
```

`components/ErrorBoundary.tsx`:
```tsx
import { Component, type ReactNode } from 'react';
import ErrorState from './ErrorState';

interface Props { children: ReactNode; }
interface State { hasError: boolean; error?: Error; }

export default class ErrorBoundary extends Component<Props, State> {
  state: State = { hasError: false };
  static getDerivedStateFromError(error: Error) { return { hasError: true, error }; }
  render() {
    if (this.state.hasError) return <ErrorState error={this.state.error} />;
    return this.props.children;
  }
}
```

`components/PageLoading.tsx`:
```tsx
import { Spin } from 'antd'; // or custom spinner if no Ant Design
export default function PageLoading() {
  return <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}><Spin size="large" /></div>;
}
```

`components/EmptyState.tsx`:
```tsx
interface Props { description?: string; }
export default function EmptyState({ description = '暂无数据' }: Props) {
  return <div style={{ textAlign: 'center', padding: '48px 0', color: '#999' }}>{description}</div>;
}
```

`components/ErrorState.tsx`:
```tsx
interface Props { error?: Error; onRetry?: () => void; }
export default function ErrorState({ error, onRetry }: Props) {
  return (
    <div style={{ textAlign: 'center', padding: '48px 0' }}>
      <p style={{ color: '#ff4d4f', marginBottom: 16 }}>{error?.message || '页面出错了'}</p>
      {onRetry && <button onClick={onRetry}>重试</button>}
    </div>
  );
}
```

`hooks/useRequest.ts`:
```tsx
import { useState, useEffect, useCallback, useRef } from 'react';

interface UseRequestOptions<T> {
  manual?: boolean;
  onSuccess?: (data: T) => void;
  onError?: (error: Error) => void;
}

export function useRequest<T>(
  fetcher: () => Promise<T>,
  options: UseRequestOptions<T> = {}
) {
  const { manual = false, onSuccess, onError } = options;
  const [data, setData] = useState<T>();
  const [loading, setLoading] = useState(!manual);
  const [error, setError] = useState<Error>();
  const fetcherRef = useRef(fetcher);

  const run = useCallback(async () => {
    setLoading(true);
    setError(undefined);
    try {
      const result = await fetcherRef.current();
      setData(result);
      onSuccess?.(result);
    } catch (e) {
      setError(e as Error);
      onError?.(e as Error);
    } finally {
      setLoading(false);
    }
  }, [onSuccess, onError]);

  useEffect(() => { if (!manual) run(); }, [manual, run]);

  return { data, loading, error, run, refresh: run };
}
```

**Vue projects:** Adapt same patterns to Vue 3 Composition API (defineComponent, ref, reactive, etc.)

### Step 6: Generate Shared Layer

After type-specific files, read `../references/shared-base.md` and `../references/shared-config.md`
and generate all shared files (services, utils, styles, configs, env).

### Step 7: Final Setup

```bash
cd <project-name>
pnpm install
pnpm dev
```

Announce completion: project name, framework, key dependencies, dev server URL (http://localhost:5173).

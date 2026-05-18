---
name: fe-cli-admin
description: >
  Scaffold an Admin Dashboard frontend project. For data management backends, CRUD systems,
  and internal tools. Features permission-based routing, login page, Ant Design Pro layout.
  Triggered as a sub-skill of fe-cli when user wants an admin/后台管理 project type.
---

# fe-cli-admin — Admin Dashboard Scaffolding

## Workflow

### Step 1: Gather Options

Skip questions already answered in user's request.

1. **Framework**: React 19 / Vue 3 (React recommended for admin, Ant Design is React-only; Vue admin 推荐 Element Plus)
2. **Styling**: Ant Design (default for React) / Element Plus (default for Vue) / Tailwind CSS
3. **CSS Preprocessor**: Sass / Less (default: Sass)
4. **State Management**: Zustand / Redux Toolkit / None
5. **i18n**: react-i18next / vue-i18n / None
6. **Testing**: Vitest / None
7. **Pre-commit hooks**: husky + lint-staged + commitlint? (default: No)
8. **Project name**: string (required)

### Step 2: Scaffold Project

```
pnpm create vite <project-name> --template react-ts
```

For Vue: `pnpm create vite <project-name> --template vue-ts`

### Step 3: Install Dependencies

**React (Ant Design):**
```
pnpm add antd @ant-design/icons @ant-design/v5-patch-for-react-19 react-router-dom dayjs
```

**Vue (Element Plus):**
```
pnpm add element-plus @element-plus/icons-vue vue-router dayjs
```

Plus extras based on selections (zustand, pinia, i18n, etc.)

For date handling: `pnpm add dayjs` (recommended; moment is deprecated and not recommended).

### Step 4: Generate Admin-Specific Files

```
src/
├── components/
│   ├── ErrorBoundary.tsx
│   ├── PageLoading.tsx
│   ├── EmptyState.tsx
│   └── ErrorState.tsx          # (same templates as fe-cli-web)
├── layouts/
│   └── AdminLayout.tsx         # Sidebar + Header + Content layout
├── pages/
│   ├── Login/
│   │   └── index.tsx           # Login page with form
│   ├── Dashboard/
│   │   └── index.tsx           # Dashboard with stats cards
│   ├── List/
│   │   └── index.tsx           # Table list page template
│   ├── Form/
│   │   └── index.tsx           # Form page template
│   └── NotFound.tsx
├── hooks/
│   └── useRequest.ts           # (same as fe-cli-web)
├── stores/
│   └── authStore.ts            # Auth state (token, user info, login/logout)
├── routes/
│   └── index.tsx               # Route config with permission guard
├── App.tsx                     # Router + AuthProvider
└── main.tsx
```

### Step 5: Key Templates

**`layouts/AdminLayout.tsx`** — Classic admin layout:
> **Note:** Inline styles below are for quick scaffolding. **Production environments should replace them with SCSS modules** (e.g., `import styles from './AdminLayout.module.scss'`).
```tsx
import { useState } from 'react';
import { Outlet, useNavigate, useLocation } from 'react-router-dom';
import { Layout, Menu, Button, Dropdown, Avatar, theme } from 'antd';
import {
  DashboardOutlined, FileTextOutlined, FormOutlined,
  MenuFoldOutlined, MenuUnfoldOutlined, UserOutlined, LogoutOutlined,
} from '@ant-design/icons';

const { Header, Sider, Content } = Layout;

// Menu items - extend based on project needs
const menuItems = [
  { key: '/dashboard', icon: <DashboardOutlined />, label: '仪表盘' },
  { key: '/list', icon: <FileTextOutlined />, label: '列表页' },
  { key: '/form', icon: <FormOutlined />, label: '表单页' },
];

export default function AdminLayout() {
  const [collapsed, setCollapsed] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();
  const { token: { colorBgContainer, borderRadiusLG } } = theme.useToken();

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider trigger={null} collapsible collapsed={collapsed}>
        <div style={{ height: 32, margin: 16, background: 'rgba(255,255,255,0.2)', borderRadius: 6 }} />
        <Menu
          theme="dark"
          mode="inline"
          selectedKeys={[location.pathname]}
          items={menuItems}
          onClick={({ key }) => navigate(key)}
        />
      </Sider>
      <Layout>
        <Header style={{ padding: '0 24px', background: colorBgContainer, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <Button type="text" icon={collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />} onClick={() => setCollapsed(!collapsed)} />
          <Dropdown menu={{ items: [{ key: 'logout', icon: <LogoutOutlined />, label: '退出登录' }] }}>
            <Avatar icon={<UserOutlined />} style={{ cursor: 'pointer' }} />
          </Dropdown>
        </Header>
        <Content style={{ margin: 24, padding: 24, background: colorBgContainer, borderRadius: borderRadiusLG, minHeight: 280 }}>
          <Outlet />
        </Content>
      </Layout>
    </Layout>
  );
}
```

**`pages/Login/index.tsx`** — Login page:
> **Note:** Inline styles below are for quick scaffolding. **Production environments should replace them with SCSS modules**.
```tsx
import { useState, type FormEvent } from 'react';
import { useNavigate } from 'react-router-dom';
import { Form, Input, Button, Card, message } from 'antd';
import { UserOutlined, LockOutlined } from '@ant-design/icons';

export default function Login() {
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const onFinish = async (values: { username: string; password: string }) => {
    setLoading(true);
    try {
      // Replace with actual API call
      // const { token } = await userApi.login(values);
      // authStore.login(token);
      message.success('登录成功');
      navigate('/dashboard', { replace: true });
    } catch {
      message.error('登录失败');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh', background: '#f0f2f5' }}>
      <Card title="系统登录" style={{ width: 400 }}>
        <Form onFinish={onFinish} size="large">
          <Form.Item name="username" rules={[{ required: true, message: '请输入用户名' }]}>
            <Input prefix={<UserOutlined />} placeholder="用户名" />
          </Form.Item>
          <Form.Item name="password" rules={[{ required: true, message: '请输入密码' }]}>
            <Input.Password prefix={<LockOutlined />} placeholder="密码" />
          </Form.Item>
          <Form.Item>
            <Button type="primary" htmlType="submit" loading={loading} block>登录</Button>
          </Form.Item>
        </Form>
      </Card>
    </div>
  );
}
```

**`pages/Dashboard/index.tsx`** — Dashboard with stats:
```tsx
import { Row, Col, Card, Statistic } from 'antd';
import { UserOutlined, ShoppingCartOutlined, RiseOutlined, FileTextOutlined } from '@ant-design/icons';

export default function Dashboard() {
  return (
    <div>
      <Row gutter={[16, 16]}>
        <Col xs={24} sm={12} lg={6}>
          <Card><Statistic title="用户数" value={1893} prefix={<UserOutlined />} /></Card>
        </Col>
        <Col xs={24} sm={12} lg={6}>
          <Card><Statistic title="订单数" value={568} prefix={<ShoppingCartOutlined />} /></Card>
        </Col>
        <Col xs={24} sm={12} lg={6}>
          <Card><Statistic title="销售额" value={93456} prefix={<RiseOutlined />} suffix="元" /></Card>
        </Col>
        <Col xs={24} sm={12} lg={6}>
          <Card><Statistic title="文章数" value={128} prefix={<FileTextOutlined />} /></Card>
        </Col>
      </Row>
    </div>
  );
}
```

**`pages/List/index.tsx`** — Table list template:
> **Note:** Inline styles below are for quick scaffolding. **Production environments should replace them with SCSS modules**.
```tsx
import { useState } from 'react';
import { Table, Button, Input, Space, Tag, type TableColumnsType } from 'antd';
import { PlusOutlined, SearchOutlined } from '@ant-design/icons';

interface DataItem { id: number; name: string; status: 'active' | 'inactive'; createdAt: string; }

export default function List() {
  const [data] = useState<DataItem[]>([]);
  const columns: TableColumnsType<DataItem> = [
    { title: 'ID', dataIndex: 'id', key: 'id', width: 80 },
    { title: '名称', dataIndex: 'name', key: 'name' },
    { title: '状态', dataIndex: 'status', key: 'status', render: (s) => <Tag color={s === 'active' ? 'green' : 'red'}>{s}</Tag> },
    { title: '创建时间', dataIndex: 'createdAt', key: 'createdAt' },
    { title: '操作', key: 'action', render: () => <Space><Button type="link" size="small">编辑</Button><Button type="link" size="small" danger>删除</Button></Space> },
  ];
  return (
    <div>
      <div style={{ marginBottom: 16, display: 'flex', justifyContent: 'space-between' }}>
        <Space><Input placeholder="搜索" prefix={<SearchOutlined />} /><Button type="primary">搜索</Button></Space>
        <Button type="primary" icon={<PlusOutlined />}>新建</Button>
      </div>
      <Table rowKey="id" columns={columns} dataSource={data} pagination={{ pageSize: 10 }} />
    </div>
  );
}
```

**`pages/Form/index.tsx`** — Form page template:
```tsx
import { Form, Input, Button, Select, DatePicker, Card, message } from 'antd';

export default function FormPage() {
  const [form] = Form.useForm();
  const onFinish = (values: unknown) => { console.log(values); message.success('提交成功'); };
  return (
    <Card title="表单页">
      <Form form={form} layout="vertical" onFinish={onFinish} style={{ maxWidth: 600 }}>
        <Form.Item label="名称" name="name" rules={[{ required: true }]}><Input /></Form.Item>
        <Form.Item label="类型" name="type" rules={[{ required: true }]}><Select options={[{ label: '类型A', value: 'a' }, { label: '类型B', value: 'b' }]} /></Form.Item>
        <Form.Item label="日期" name="date"><DatePicker style={{ width: '100%' }} /></Form.Item>
        <Form.Item><Button type="primary" htmlType="submit">提交</Button></Form.Item>
      </Form>
    </Card>
  );
}
```

**`stores/authStore.ts`** (Zustand):
```tsx
import { create } from 'zustand';
import { storage } from '@/utils/storage';

interface AuthState {
  token: string | null;
  user: { id: string; name: string; avatar?: string } | null;
  login: (token: string, user: AuthState['user']) => void;
  logout: () => void;
  isLoggedIn: () => boolean;
}

export const useAuthStore = create<AuthState>((set, get) => ({
  token: storage.get('token'),
  user: storage.get('user'),
  login: (token, user) => { storage.set('token', token); storage.set('user', user); set({ token, user }); },
  logout: () => { storage.remove('token'); storage.remove('user'); set({ token: null, user: null }); },
  isLoggedIn: () => !!get().token,
}));
```

**`routes/index.tsx`** — Permission route config:
```tsx
import { Navigate, type RouteObject } from 'react-router-dom';
import AdminLayout from '@/layouts/AdminLayout';
import Login from '@/pages/Login';
import Dashboard from '@/pages/Dashboard';
import List from '@/pages/List';
import FormPage from '@/pages/Form';
import NotFound from '@/pages/NotFound';

// Auth guard component
import { useAuthStore } from '@/stores/authStore';

function AuthGuard({ children }: { children: React.ReactNode }) {
  const token = useAuthStore((s) => s.token);
  if (!token) return <Navigate to="/login" replace />;
  return <>{children}</>;
}

export const routes: RouteObject[] = [
  { path: '/login', element: <Login /> },
  {
    path: '/',
    element: <AuthGuard><AdminLayout /></AuthGuard>,
    children: [
      { index: true, element: <Navigate to="/dashboard" replace /> },
      { path: 'dashboard', element: <Dashboard /> },
      { path: 'list', element: <List /> },
      { path: 'form', element: <FormPage /> },
    ],
  },
  { path: '*', element: <NotFound /> },
];
```

**`App.tsx`:**
```tsx
import { useRoutes } from 'react-router-dom';
import { BrowserRouter } from 'react-router-dom';
import { ConfigProvider } from 'antd';
import zhCN from 'antd/locale/zh_CN';
import { routes } from '@/routes';

function AppRoutes() { return useRoutes(routes); }

export default function App() {
  return (
    <ConfigProvider locale={zhCN}>
      <BrowserRouter>
        <AppRoutes />
      </BrowserRouter>
    </ConfigProvider>
  );
}
```

### Step 6: Vue Admin Templates (if Vue + Element Plus selected)

**Vue file structure:**
```
src/
├── components/
│   ├── ErrorBoundary.vue
│   ├── PageLoading.vue
│   ├── EmptyState.vue
│   └── ErrorState.vue
├── layouts/
│   └── AdminLayout.vue        # Element Plus sidebar layout
├── pages/
│   ├── Login.vue              # Login page
│   ├── Dashboard.vue          # Dashboard with stats
│   ├── List.vue               # Table list page
│   ├── Form.vue               # Form page
│   └── NotFound.vue
├── stores/
│   └── authStore.ts           # Pinia auth store
├── router/
│   └── index.ts               # Vue Router with permission guard
├── App.vue
└── main.ts
```

**`main.ts`:**
```typescript
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import ElementPlus from 'element-plus';
import zhCn from 'element-plus/es/locale/lang/zh-cn';
import 'element-plus/dist/index.css';
import App from './App.vue';
import router from './router';

const app = createApp(App);
app.use(createPinia());
app.use(router);
app.use(ElementPlus, { locale: zhCn });
app.mount('#app');
```

**`router/index.ts`:**
```typescript
import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@/stores/authStore';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/login', component: () => import('@/pages/Login.vue') },
    {
      path: '/',
      component: () => import('@/layouts/AdminLayout.vue'),
      meta: { requiresAuth: true },
      children: [
        { path: '', redirect: '/dashboard' },
        { path: 'dashboard', component: () => import('@/pages/Dashboard.vue') },
        { path: 'list', component: () => import('@/pages/List.vue') },
        { path: 'form', component: () => import('@/pages/Form.vue') },
      ],
    },
    { path: '/:pathMatch(.*)*', component: () => import('@/pages/NotFound.vue') },
  ],
});

router.beforeEach((to) => {
  const authStore = useAuthStore();
  if (to.meta.requiresAuth && !authStore.token) return '/login';
});

export default router;
```

**`stores/authStore.ts` (Pinia):**
```typescript
import { defineStore } from 'pinia';
import { storage } from '@/utils/storage';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: storage.get<string>('token') || null,
    user: storage.get<{ id: string; name: string; avatar?: string }>('user') || null,
  }),
  actions: {
    login(token: string, user: this['user']) {
      this.token = token;
      this.user = user;
      storage.set('token', token);
      storage.set('user', user);
    },
    logout() {
      this.token = null;
      this.user = null;
      storage.remove('token');
      storage.remove('user');
    },
  },
  getters: {
    isLoggedIn: (state) => !!state.token,
  },
});
```

**`layouts/AdminLayout.vue`:**
```vue
<template>
  <el-container style="min-height: 100vh">
    <el-aside :width="isCollapsed ? '64px' : '220px'">
      <div class="logo-placeholder" />
      <el-menu
        :default-active="route.path"
        :collapse="isCollapsed"
        background-color="#001529"
        text-color="#ffffffa6"
        active-text-color="#fff"
        @select="(key: string) => router.push(key)"
      >
        <el-menu-item index="/dashboard"><el-icon><Odometer /></el-icon><span>仪表盘</span></el-menu-item>
        <el-menu-item index="/list"><el-icon><Document /></el-icon><span>列表页</span></el-menu-item>
        <el-menu-item index="/form"><el-icon><EditPen /></el-icon><span>表单页</span></el-menu-item>
      </el-menu>
    </el-aside>
    <el-container>
      <el-header class="admin-header">
        <el-icon class="collapse-btn" @click="isCollapsed = !isCollapsed">
          <component :is="isCollapsed ? 'Expand' : 'Fold'" />
        </el-icon>
        <el-dropdown @command="handleCommand">
          <el-avatar :size="32"><el-icon><User /></el-icon></el-avatar>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item command="logout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </el-header>
      <el-main><router-view /></el-main>
    </el-container>
  </el-container>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { Odometer, Document, EditPen, User, Expand, Fold } from '@element-plus/icons-vue';
import { useAuthStore } from '@/stores/authStore';

const route = useRoute();
const router = useRouter();
const authStore = useAuthStore();
const isCollapsed = ref(false);

function handleCommand(command: string) {
  if (command === 'logout') {
    authStore.logout();
    router.push('/login');
  }
}
</script>

<style scoped lang="scss">
/* Production: replace with SCSS module */
.logo-placeholder {
  height: 32px;
  margin: 16px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 6px;
}
.admin-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
}
.collapse-btn {
  font-size: 20px;
  cursor: pointer;
}
</style>
```

### Step 7: Generate Shared Layer

Read `../references/shared-base.md` and `../references/shared-config.md`.
Generate all shared files: services, utils, styles, configs, env.

### Step 8: Final Setup

```bash
cd <project-name>
pnpm install
pnpm dev
```

Announce completion with admin-specific info: login page at /login, dashboard at /dashboard, etc.

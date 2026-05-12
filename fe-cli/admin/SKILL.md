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

1. **Framework**: React 19 / Vue 3 (React recommended for admin, Ant Design is React-only)
2. **Styling**: Ant Design (default, strongly recommended) / Tailwind CSS
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

### Step 3: Install Dependencies

```
pnpm add antd @ant-design/icons @ant-design/v5-patch-for-react-19 react-router-dom dayjs
```

Plus extras based on selections (zustand, redux, i18n, etc.)

Also: `pnpm add moment` or `dayjs` for date handling.

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
import { Navigate } from 'react-router-dom';

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

### Step 6: Generate Shared Layer

Read `../references/shared-base.md` and `../references/shared-config.md`.
Generate all shared files: services, utils, styles, configs, env.

### Step 7: Final Setup

```bash
cd <project-name>
pnpm install
pnpm dev
```

Announce completion with admin-specific info: login page at /login, dashboard at /dashboard, etc.

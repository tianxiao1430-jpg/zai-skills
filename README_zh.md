# ZAI-Skills

[English](./README.md) | [简体中文](./README_zh.md) | [日本語](./README_ja.md)

一套专门为 **Z.AI (Z Code)** 平台及其核心 MCP 生态系统（Vision, Search 和 Zread）设计的高性能 [Agent Skills](https://github.com/skillcreatorai/Ai-Agent-Skills) 集合。

## 🌟 为什么选择 ZAI-Skills？

这些技能经过优化，增强了 Z.AI 智能套件的三大支柱，为高保真技术输出提供高级指令。

## 🚀 可用技能

| 技能 | 描述 | 触发词 |
|------|------|--------|
| **`zai-orchestrator`** | "大脑"技能。协调 Vision, Search 和 Zread 来解决复杂的、多步骤的工程任务。 | 复杂任务，多步骤，协同，orchestrator |
| **`vision-expert`** | 针对 Z.AI Vision 的高级 UI 转代码、技术图表分析和视觉错误诊断。 | 分析图片，UI 转代码，截图诊断，vision |
| **`search-expert`** | 使用 Z.AI Web Search Prime 进行高精度技术研究和结构化信息综合。 | 搜索，调研，查找资料，search |
| **`zread-expert`** | 通过 Zread 进行资深架构师级别的代码库分析、结构审计和语义搜索。 | 分析仓库，代码审计，zread, 架构分析 |

## 📖 使用场景

### Vision Expert

| 场景 | 示例输入 | 预期输出 |
|------|----------|----------|
| **UI 还原** | "帮我把这个设计稿转成 React 组件" + [截图] | 可运行的 React + Tailwind 代码 |
| **错误诊断** | "这个报错怎么修？" + [终端错误截图] | 错误原因分析 + 具体修复代码 |
| **架构图理解** | "帮我解释这个系统架构" + [架构图] | 架构说明 + 服务/模块定义 |
| **OCR 提取** | "提取这张图片里的文字" + [文档截图] | 结构化文本内容 |

**示例对话：**
```
用户：[上传 UI 截图] 帮我实现这个登录页面

助手：我来帮你将这张截图转换为 React + Tailwind 代码。
      [调用 ui_to_artifact]
      ✅ 已生成登录组件，包含：
      - 邮箱/密码输入框
      - 带加载状态的登录按钮
      - 表单验证逻辑
      - 响应式设计
```

---

### Search Expert

| 场景 | 示例输入 | 预期输出 |
|------|----------|----------|
| **技术调研** | "对比 Next.js 和 Remix 的优缺点" | 结构化对比表 + 选型建议 |
| **最佳实践** | "React 性能优化的最佳实践" | 分类整理的优化方案 |
| **版本差异** | "React 18 相比 React 17 有什么新特性" | 新特性列表 + 迁移指南 |
| **错误排查** | "TypeError: Cannot read property of undefined 常见原因" | 常见原因 + 解决方案汇总 |

**示例对话：**
```
用户：帮我调研一下 2026 年前端状态管理的趋势

助手：我正在搜索最新的前端状态管理方案...
      [调用 zai-web-search]
      
📊 2026 前端状态管理趋势总结：

## 主流方案
1. **Zustand** - 轻量级，适合中小型项目
2. **Jotai** - 原子化状态，适合细粒度更新
3. **Redux Toolkit** - 企业级，完整生态

## 新兴趋势
- 服务端组件减少客户端状态需求
- Signals 方案兴起（SolidJS, Preact Signals）

## 选型建议
- 小型项目：Zustand
- 大型项目：Redux Toolkit + 服务端组件
```

---

### Zread Expert

| 场景 | 示例输入 | 预期输出 |
|------|----------|----------|
| **新库学习** | "帮我分析 facebook/react 的目录结构" | 项目结构说明 + 核心模块介绍 |
| **源码理解** | "React 的 useEffect 是怎么实现的" | 源码路径 + 实现逻辑解析 |
| **Issue 调研** | "这个库有哪些未解决的严重 Bug" | Issue 列表 + 影响分析 |
| **贡献准备** | "我想给这个库提 PR，需要注意什么" | 贡献指南 + 代码规范 |

**示例对话：**
```
用户：分析一下 vercel/next.js 的中间件系统是怎么实现的

助手：我来分析 Next.js 中间件系统的实现...
      [调用 zread.structure]
      [调用 zread.search 搜索"middleware"]
      [调用 zread.read 读取核心文件]
      
📦 Next.js 中间件系统架构：

## 核心文件
- `packages/next/src/server/web/sandbox.ts` - 沙箱环境
- `packages/next/src/server/web/spec-extension/` - Edge API
- `packages/next/middleware.ts` - 用户入口

## 实现原理
1. 基于 Edge Runtime 运行
2. 使用 V8 Isolate 隔离用户代码
3. 通过 spec-extension 提供 Next.js API
```

---

### ZAI Orchestrator

| 场景 | 示例输入 | 使用技能 | 预期输出 |
|------|----------|----------|----------|
| **全栈功能开发** | "帮我实现一个带登录的博客系统" | Orchestrator + 全部 expert | 完整架构 + 核心代码 |
| **复杂 Bug 排查** | "这个功能本地正常，部署后报错" | Orchestrator + Search + Zread | 根因分析 + 修复方案 |
| **技术选型** | "我要做一个实时协作编辑器，用什么技术栈" | Orchestrator + Search | 技术方案对比 + 推荐 |
| **代码迁移** | "帮我把这个 jQuery 项目迁移到 React" | Orchestrator + Vision + Zread | 迁移计划 + 示例代码 |

**示例对话：**
```
用户：我想做一个类似 Notion 的在线文档编辑器，应该怎么设计？

助手：<internal>
这是一个复杂任务，需要协调多个技能：
1. Search - 调研现有方案和最佳实践
2. Zread - 分析开源类似项目（如 AppFlowy）
3. Vision - 如果有 UI 参考图，分析界面布局

开始执行 Triple-A 工作流...
</internal>

我来帮你设计这个在线文档编辑器。

## 📊 市场调研 (Search)
[调研结果：主流方案有 ProseMirror, TipTap, Slate.js...]

## 📦 架构分析 (Zread)
[分析 AppFlowy 等项目：前端用 React + TipTap，后端用 Rust...]

## 🏗️ 推荐技术方案

### 前端
- 编辑器核心：TipTap (基于 ProseMirror)
- 框架：Next.js 14 (App Router)
- 实时协作：Yjs + WebSocket

### 后端
- API：Next.js API Routes
- 数据库：PostgreSQL + pgvector
- 实时同步：PartyKit 或自研 WebSocket 服务

### 部署
- Vercel (前端) + Railway (后端服务)

需要我详细实现某个模块吗？
```

---

## 🛠️ 安装方法

### 推荐：安装全部技能
```bash
# 一次性安装所有 4 个技能
npx skills add https://github.com/tianxiao1430-jpg/zai-skills --all
```

### 单独安装
```bash
# 安装特定技能
npx skills add https://github.com/tianxiao1430-jpg/zai-skills --skill vision-expert
npx skills add https://github.com/tianxiao1430-jpg/zai-skills --skill search-expert
npx skills add https://github.com/tianxiao1430-jpg/zai-skills --skill zread-expert
npx skills add https://github.com/tianxiao1430-jpg/zai-skills --skill zai-orchestrator
```

### 技能依赖关系

```
┌─────────────────────────────────────────┐
│         zai-orchestrator (大脑)          │
│  协调 Vision + Search + Zread 解决复杂任务  │
└─────────────┬───────────────────────────┘
              │ 依赖
              ▼
    ┌─────────────────────────┐
    │                         │
    ▼                         ▼
┌──────────┐          ┌──────────────┐
│ vision   │          │ search       │
│ expert   │          │ expert       │
└──────────┘          └──────────────┘
       │                     │
       └──────────┬──────────┘
                  │
                  ▼
          ┌──────────────┐
          │ zread        │
          │ expert       │
          └──────────────┘
```

**注意：** `zai-orchestrator` 需要安装全部三个 expert 技能才能正常工作。

---

## 🔧 配置指南

### 自定义技能

可以通过编辑 `SKILL.md` 文件自定义每个技能。常见的自定义包括：

1. **添加领域特定知识** - 为你的行业修改提示词
2. **调整输出格式** - 更改响应模板
3. **添加示例** - 加入你自己的使用案例

### 技能组合建议

| 任务类型 | 推荐技能组合 |
|----------|-------------|
| UI 转代码 | vision-expert |
| 技术调研 | search-expert |
| 代码分析 | zread-expert |
| 复杂项目 | **全部 4 个技能** |
| 全栈开发 | orchestrator + 全部 expert |

---

## 📊 技能对比

| 特性 | vision-expert | search-expert | zread-expert | orchestrator |
|------|---------------|---------------|--------------|--------------|
| **输入** | 图片/截图 | 文本查询 | GitHub 仓库 | 任何复杂任务 |
| **输出** | 代码/诊断 | 调研报告 | 代码分析 | 综合解决方案 |
| **适用** | UI 还原、OCR | 技术研究 | 学习代码库 | 多步骤项目 |
| **依赖** | 无 | 无 | 无 | 全部 3 个 expert |

---

## 🤝 参与贡献

这是一个社区驱动的项目！我们欢迎所有人：

1. **提交新技能**（针对 Z.AI 工具）
2. **改进现有指令**以提高 AI 可靠性
3. **分享案例** - 这些技能帮你解决问题的实际案例
4. **添加使用场景** - 从你的经验中添加用例

欢迎提交 PR 或 Issue。让我们一起构建最好的 Z.AI 工具箱！

### 开发流程

```bash
# 1. Fork 仓库
git clone https://github.com/your-username/zai-skills

# 2. 创建新技能
cd zai-skills/skills
mkdir my-new-skill
# 添加 skill.json 和 SKILL.md

# 3. 本地测试
# 在你的 AI agent 中使用

# 4. 提交 PR
git add .
git commit -m "feat: add my-new-skill"
git push origin main
```

---

## ❓ 常见问题

### Q: 我需要安装全部 4 个技能吗？

**A:** 不一定。根据你的需求选择：
- **只做 UI 工作？** → vision-expert 就够了
- **只做调研？** → search-expert 就够了
- **复杂项目？** → 建议安装全部 4 个

### Q: 没有 Z.AI 可以使用这些技能吗？

**A:** 这些技能是专门为 Z.AI MCP 工具（Vision, Search, Zread）设计的。没有这些工具无法使用。

### Q: 如何更新技能？

**A:** 重新运行安装命令：
```bash
npx skills update zai-skills
```

### Q: 可以自定义提示词吗？

**A:** 可以！编辑 `SKILL.md` 文件添加你自己的示例和领域知识。

---

## 📄 许可证

本项目采用 MIT 许可证。

## 🔗 相关链接

- [Z.AI MCP 工具](https://github.com/z-ai/mcp) - 核心 MCP 工具
- [Agent Skills 标准](https://github.com/skillcreatorai/Ai-Agent-Skills) - Skills 规范
- [OpenClaw](https://github.com/openclaw/openclaw) - AI 代理框架

---

**版本：** 1.0.0  
**最后更新：** 2026-03-21  
**维护者：** [@tianxiao1430-jpg](https://github.com/tianxiao1430-jpg)

# ZAI-Skills

[English](./README.md) | [简体中文](./README_zh.md) | [日本語](./README_ja.md)

A collection of high-performance [Agent Skills](https://github.com/skillcreatorai/Ai-Agent-Skills) designed to supercharge AI agents (OpenClaw, Claude Code, Cursor, Z Code, etc.) with the **Z.AI (Z Code)** core MCP ecosystem (Vision, Search, and Zread).

## 🌟 Why ZAI-Skills?

These skills are optimized to enhance the three fundamental pillars of the Z.AI intelligence suite, providing advanced instructions for high-fidelity technical output.

## 🚀 Available Skills

| Skill | Description | Triggers |
|-------|-------------|----------|
| **`zai-orchestrator`** | The "Brain" skill. Coordinates Vision, Search, and Zread to solve complex, multi-step engineering tasks. | 复杂任务，多步骤，协同，orchestrator |
| **`vision-expert`** | Advanced UI-to-Code, technical diagram analysis, and visual error diagnosis for Z.AI Vision. | 分析图片，UI 转代码，截图诊断，vision |
| **`search-expert`** | High-precision technical research and structured information synthesis using Z.AI Web Search Prime. | 搜索，调研，查找资料，search |
| **`zread-expert`** | Senior architect-level codebase analysis, structural audits, and semantic search via Zread. | 分析仓库，代码审计，zread, 架构分析 |

## 📖 Use Cases

### Vision Expert

| Scenario | Example Input | Expected Output |
|----------|---------------|-----------------|
| **UI Recreation** | "Convert this design to React components" + [screenshot] | Runnable React + Tailwind code |
| **Error Diagnosis** | "How to fix this error?" + [terminal screenshot] | Root cause analysis + specific fix |
| **Diagram Analysis** | "Explain this system architecture" + [architecture diagram] | Architecture breakdown + service definitions |
| **OCR Extraction** | "Extract text from this image" + [document screenshot] | Structured text content |

**Example Dialogue:**
```
User: [uploads UI screenshot] Help me implement this login page

Assistant: I'll convert this screenshot to React + Tailwind code.
           [calls ui_to_artifact]
           ✅ Generated login component with:
           - Email/password input fields
           - Login button with loading state
           - Form validation logic
           - Responsive design
```

---

### Search Expert

| Scenario | Example Input | Expected Output |
|----------|---------------|-----------------|
| **Technical Research** | "Compare Next.js vs Remix pros and cons" | Structured comparison + recommendation |
| **Best Practices** | "React performance optimization best practices" | Categorized optimization strategies |
| **Version Differences** | "What's new in React 18 vs React 17" | New features list + migration guide |
| **Error Research** | "Common causes of TypeError: Cannot read property of undefined" | Common causes + solutions summary |

**Example Dialogue:**
```
User: Research 2026 frontend state management trends

Assistant: I'm searching for the latest frontend state management solutions...
           [calls zai-web-search]
           
📊 2026 Frontend State Management Trends:

## Main Solutions
1. **Zustand** - Lightweight, great for small-medium projects
2. **Jotai** - Atomic state, perfect for fine-grained updates
3. **Redux Toolkit** - Enterprise-grade, complete ecosystem

## Emerging Trends
- Server Components reducing client state needs
- Signals approach rising (SolidJS, Preact Signals)

## Recommendation
- Small projects: Zustand
- Large projects: Redux Toolkit + Server Components
```

---

### Zread Expert

| Scenario | Example Input | Expected Output |
|----------|---------------|-----------------|
| **New Library Learning** | "Analyze facebook/react directory structure" | Project structure + core modules intro |
| **Source Code Understanding** | "How is React's useEffect implemented?" | Source path + implementation logic |
| **Issue Research** | "What are the unresolved critical bugs in this repo?" | Issue list + impact analysis |
| **Contribution Prep** | "I want to contribute to this repo, what should I know?" | Contribution guide + code standards |

**Example Dialogue:**
```
User: Analyze how vercel/next.js middleware system works

Assistant: I'll analyze the Next.js middleware implementation...
           [calls zread.structure]
           [calls zread.search for "middleware"]
           [calls zread.read on core files]
           
📦 Next.js Middleware Architecture:

## Core Files
- `packages/next/src/server/web/sandbox.ts` - Sandbox environment
- `packages/next/src/server/web/spec-extension/` - Edge API
- `packages/next/middleware.ts` - User entry point

## How It Works
1. Runs on Edge Runtime
2. Uses V8 Isolate for user code isolation
3. Provides Next.js API via spec-extension

## Key Code Snippet
[code example...]
```

---

### ZAI Orchestrator

| Scenario | Example Input | Skills Used | Expected Output |
|----------|---------------|-------------|-----------------|
| **Full-Stack Dev** | "Build a blog system with authentication" | All 4 skills | Complete architecture + core code |
| **Complex Bug** | "This works locally but fails in production" | Orchestrator + Search + Zread | Root cause + fix plan |
| **Tech Selection** | "What stack for a real-time collaborative editor?" | Orchestrator + Search | Tech comparison + recommendation |
| **Code Migration** | "Migrate this jQuery project to React" | Orchestrator + Vision + Zread | Migration plan + sample code |

**Example Dialogue:**
```
User: I want to build an online document editor like Notion. How should I design it?

Assistant: <internal>
This is a complex task requiring multiple skills:
1. Search - Research existing solutions
2. Zread - Analyze open-source alternatives (e.g., AppFlowy)
3. Vision - Analyze UI if reference images provided

Starting Triple-A Workflow...
</internal>

I'll help you design this online document editor.

## 📊 Market Research (Search)
[Research results: Mainstream solutions include ProseMirror, TipTap, Slate.js...]

## 📦 Architecture Analysis (Zread)
[Analyzing AppFlowy and similar projects: Frontend uses React + TipTap, backend in Rust...]

## 🏗️ Recommended Tech Stack

### Frontend
- Editor Core: TipTap (based on ProseMirror)
- Framework: Next.js 14 (App Router)
- Real-time Collaboration: Yjs + WebSocket

### Backend
- API: Next.js API Routes
- Database: PostgreSQL + pgvector
- Sync Service: PartyKit or custom WebSocket

### Deployment
- Vercel (Frontend) + Railway (Backend)

Need me to implement any specific module?
```

---

## 🛠️ Installation

### Recommended: Install All Skills
```bash
# Install all 4 skills at once
npx skills add https://github.com/tianxiao1430-jpg/zai-skills --all
```

### Individual Installation
```bash
# Install specific skills
npx skills add https://github.com/tianxiao1430-jpg/zai-skills --skill vision-expert
npx skills add https://github.com/tianxiao1430-jpg/zai-skills --skill search-expert
npx skills add https://github.com/tianxiao1430-jpg/zai-skills --skill zread-expert
npx skills add https://github.com/tianxiao1430-jpg/zai-skills --skill zai-orchestrator
```

### Skill Dependencies

```
┌─────────────────────────────────────────┐
│         zai-orchestrator (Brain)         │
│  Coordinates Vision + Search + Zread     │
└─────────────┬───────────────────────────┘
              │ depends on
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

**Note:** `zai-orchestrator` requires all three expert skills to function properly.

---

## 🔧 Configuration

### Customizing Skills

Each skill can be customized by editing its `SKILL.md` file. Common customizations:

1. **Add domain-specific knowledge** - Modify prompts for your industry
2. **Adjust output format** - Change response templates
3. **Add examples** - Include your own use cases

### Combining Skills

| Task Type | Recommended Combination |
|-----------|------------------------|
| UI to Code | vision-expert |
| Technical Research | search-expert |
| Code Analysis | zread-expert |
| Complex Projects | **All 4 skills** |
| Full-Stack Development | orchestrator + all experts |

---

## 📊 Skill Comparison

| Feature | vision-expert | search-expert | zread-expert | orchestrator |
|---------|---------------|---------------|--------------|--------------|
| **Input** | Images/Screenshots | Text queries | GitHub repos | Any complex task |
| **Output** | Code/Diagnosis | Research reports | Code analysis | Comprehensive solutions |
| **Best For** | UI conversion, OCR | Technical research | Learning codebases | Multi-step projects |
| **Dependencies** | None | None | None | All 3 experts |

---

## 🤝 Contributing

This is a community-driven project! We welcome everyone to:

1. **Submit new skills** for Z.AI tools
2. **Refine existing instructions** to improve AI reliability
3. **Share edge cases** where these skills saved your day
4. **Add use cases** from your experience

Feel free to open a PR or Issue. Let's build the best Z.AI toolbox together!

### Development Workflow

```bash
# 1. Fork the repo
git clone https://github.com/your-username/zai-skills

# 2. Create new skill
cd zai-skills/skills
mkdir my-new-skill
# Add skill.json and SKILL.md

# 3. Test locally
# Use with your AI agent

# 4. Submit PR
git add .
git commit -m "feat: add my-new-skill"
git push origin main
```

---

## ❓ FAQ

### Q: Do I need all 4 skills?

**A:** Not necessarily. Choose based on your needs:
- **Only UI work?** → vision-expert is enough
- **Only research?** → search-expert is enough
- **Complex projects?** → Get all 4 skills

### Q: Can I use these skills without Z.AI?

**A:** These skills are specifically designed for Z.AI MCP tools (Vision, Search, Zread). They won't work without access to these tools.

### Q: How do I update skills?

**A:** Re-run the install command:
```bash
npx skills update zai-skills
```

### Q: Can I customize the prompts?

**A:** Yes! Edit the `SKILL.md` files to add your own examples and domain knowledge.

---

## 📄 License

This project is licensed under the MIT License.

## 🔗 Related Projects

- [Z.AI MCP Tools](https://github.com/z-ai/mcp) - Core MCP tools
- [Agent Skills Standard](https://github.com/skillcreatorai/Ai-Agent-Skills) - Skills specification
- [OpenClaw](https://github.com/openclaw/openclaw) - AI agent framework

---

**Version:** 1.0.0  
**Last Updated:** 2026-03-21  
**Maintainer:** [@tianxiao1430-jpg](https://github.com/tianxiao1430-jpg)

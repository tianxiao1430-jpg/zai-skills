# ZAI-Skills 测试指南

## 快速开始

### 运行所有测试

```bash
cd zai-skills
python tests/run_tests.py
```

### 运行特定技能测试

```bash
# 只测试 vision-expert
python tests/run_tests.py --skill vision-expert

# 只测试 search-expert
python tests/run_tests.py --skill search-expert
```

### 生成详细报告

```bash
python tests/run_tests.py --report
```

报告将保存到 `tests/TEST_REPORT.md`

---

## 测试结构

```
tests/
├── run_tests.py              # 测试运行器
├── test_cases.json           # 测试用例定义
├── README.md                 # 测试文档
└── examples/                 # 示例对话测试集
    ├── vision-expert.md
    ├── search-expert.md
    ├── zread-expert.md
    └── orchestrator.md
```

---

## 添加新测试

### 1. 在 test_cases.json 中添加测试用例

```json
{
  "vision-expert": [
    {
      "id": "vision-004",
      "name": "新测试名称",
      "input": {
        "type": "image",
        "description": "测试输入描述",
        "prompt": "用户提示词"
      },
      "expected": {
        "tool_called": "工具名称",
        "output_contains": ["期望包含的内容"],
        "quality": {
          "检查项": true
        }
      }
    }
  ]
}
```

### 2. 在 examples/ 中添加示例对话

在对应的技能文件中添加新的测试场景：

```markdown
## Test XXX: 测试名称

**输入：**
```
用户：[输入内容]
```

**期望输出要点：**
- [ ] 检查项 1
- [ ] 检查项 2
- [ ] 检查项 3

**实际输出：**
```
[运行测试后填写]
```

**评分：** ⭐⭐⭐⭐⭐

**备注：**
```
[任何额外评论]
```
```

### 3. 运行测试验证

```bash
python tests/run_tests.py --skill your-skill-name
```

---

## 测试用例格式

### 输入类型

| 类型 | 说明 | 示例 |
|------|------|------|
| `image` | 图片输入 | UI 截图、错误截图、架构图 |
| `text` | 文本输入 | 技术问题、调研请求 |

### 期望输出字段

| 字段 | 说明 | 类型 |
|------|------|------|
| `tool_called` | 期望调用的工具 | string |
| `tools_called` | 期望调用的多个工具 | string[] |
| `output_contains` | 输出应包含的内容 | string[] |
| `quality` | 质量检查项 | object |

---

## 持续集成

### GitHub Actions 配置

```yaml
# .github/workflows/test-skills.yml
name: Test Skills

on:
  push:
    paths:
      - 'skills/**/*.md'
      - 'tests/**/*'
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Run skill tests
        run: |
          python tests/run_tests.py
      
      - name: Upload test report
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: test-report
          path: tests/TEST_REPORT.md
```

---

## 测试覆盖率目标

| 技能 | 最少测试数 | 当前状态 |
|------|-----------|----------|
| vision-expert | 5 | ✅ 5 |
| search-expert | 5 | ✅ 5 |
| zread-expert | 5 | ✅ 5 |
| zai-orchestrator | 5 | ✅ 5 |

---

## 手动测试清单

在提交 PR 前，建议手动测试以下场景：

### Vision Expert
- [ ] UI 截图转代码
- [ ] 错误截图诊断
- [ ] 架构图分析
- [ ] OCR 文本提取
- [ ] 多张图片关联分析

### Search Expert
- [ ] 技术对比调研
- [ ] 最佳实践搜索
- [ ] 版本差异调研
- [ ] 错误解决方案
- [ ] 趋势分析

### Zread Expert
- [ ] 项目结构分析
- [ ] 源码实现理解
- [ ] Issue 调研
- [ ] 贡献指南查询
- [ ] 架构决策分析

### ZAI Orchestrator
- [ ] 全栈功能开发
- [ ] 复杂 Bug 排查
- [ ] 技术选型
- [ ] 代码迁移
- [ ] 系统设计

---

## 故障排除

### 测试运行失败

```bash
# 检查 Python 版本
python --version  # 需要 3.8+

# 检查测试文件是否存在
ls tests/test_cases.json

# 查看详细错误
python tests/run_tests.py -v
```

### 测试用例格式错误

确保 JSON 格式正确：

```bash
python -m json.tool tests/test_cases.json > /dev/null && echo "JSON 格式正确"
```

---

## 贡献测试

欢迎贡献新的测试用例！

1. Fork 仓库
2. 添加测试用例到 `test_cases.json`
3. 添加示例对话到 `examples/`
4. 运行测试验证
5. 提交 PR

---

**测试框架版本：** 1.0.0  
**最后更新：** 2026-03-21

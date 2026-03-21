#!/bin/bash
# ZAI-Skills 测试运行脚本

set -e

echo "🦞 ZAI-Skills 测试运行器"
echo "========================"
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误：需要 Python 3"
    exit 1
fi

echo "✅ Python 版本：$(python3 --version)"
echo ""

# 运行测试
echo "🚀 运行测试..."
python3 tests/run_tests.py "$@"

# 检查退出码
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 所有测试通过！"
else
    echo ""
    echo "❌ 部分测试失败"
    exit 1
fi

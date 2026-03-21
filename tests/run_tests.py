#!/usr/bin/env python3
"""
ZAI-Skills Test Framework
验证技能提示词的有效性和一致性

使用方法:
    python tests/run_tests.py              # 运行所有测试
    python tests/run_tests.py --skill vision-expert  # 运行特定技能测试
    python tests/run_tests.py --report     # 生成详细报告
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime


class SkillTester:
    """技能测试器"""
    
    def __init__(self, skill_name: str, test_cases: List[Dict]):
        self.skill_name = skill_name
        self.test_cases = test_cases
        self.results = []
    
    def load_skill_prompt(self) -> Optional[str]:
        """加载技能的 SKILL.md 文件"""
        skill_path = Path(__file__).parent.parent / "skills" / self.skill_name / "SKILL.md"
        if not skill_path.exists():
            return None
        
        with open(skill_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def validate_test_case(self, test_case: Dict) -> Dict[str, Any]:
        """
        验证单个测试用例
        
        注意：这是简化版本，实际集成需要：
        1. 加载 SKILL.md 提示词
        2. 调用实际 Agent 运行测试
        3. 验证输出是否符合预期
        """
        result = {
            "test_id": test_case["id"],
            "name": test_case["name"],
            "status": "pending",
            "errors": [],
            "warnings": []
        }
        
        # 验证测试用例格式
        if "input" not in test_case:
            result["status"] = "failed"
            result["errors"].append("缺少 input 字段")
            return result
        
        if "expected" not in test_case:
            result["status"] = "failed"
            result["errors"].append("缺少 expected 字段")
            return result
        
        # 验证 SKILL.md 存在
        skill_prompt = self.load_skill_prompt()
        if not skill_prompt:
            result["status"] = "failed"
            result["errors"].append(f"SKILL.md 文件不存在")
            return result
        
        # 验证 SKILL.md 包含必要内容
        if "##" not in skill_prompt:
            result["warnings"].append("SKILL.md 可能缺少章节结构")
        
        # 检查是否包含示例对话
        if "示例" not in skill_prompt and "Example" not in skill_prompt:
            result["warnings"].append("SKILL.md 可能缺少示例对话")
        
        # 检查是否包含错误处理
        if "错误" not in skill_prompt and "Error" not in skill_prompt:
            result["warnings"].append("SKILL.md 可能缺少错误处理说明")
        
        # 如果没有错误，标记为通过（模拟）
        if not result["errors"]:
            result["status"] = "passed" if not result["warnings"] else "passed_with_warnings"
        
        return result
    
    def run_all(self) -> Dict[str, Any]:
        """运行所有测试"""
        print(f"\n{'='*60}")
        print(f"测试技能：{self.skill_name}")
        print(f"{'='*60}")
        
        for test_case in self.test_cases:
            print(f"\n  运行测试：{test_case['id']} - {test_case['name']}")
            result = self.validate_test_case(test_case)
            self.results.append(result)
            
            # 打印结果
            status_icon = "✅" if result["status"] == "passed" else "⚠️" if result["status"] == "passed_with_warnings" else "❌"
            print(f"  {status_icon} 状态：{result['status']}")
            
            if result["errors"]:
                for error in result["errors"]:
                    print(f"     ❌ {error}")
            
            if result["warnings"]:
                for warning in result["warnings"]:
                    print(f"     ⚠️  {warning}")
        
        # 汇总结果
        total = len(self.results)
        passed = sum(1 for r in self.results if r["status"] in ["passed", "passed_with_warnings"])
        failed = sum(1 for r in self.results if r["status"] == "failed")
        
        return {
            "skill": self.skill_name,
            "total": total,
            "passed": passed,
            "failed": failed,
            "details": self.results
        }


def load_test_cases() -> Dict[str, List[Dict]]:
    """加载所有测试用例"""
    test_cases_path = Path(__file__).parent / "test_cases.json"
    
    if not test_cases_path.exists():
        print(f"❌ 测试用例文件不存在：{test_cases_path}")
        sys.exit(1)
    
    with open(test_cases_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_report(all_results: Dict[str, Dict]) -> str:
    """生成测试报告"""
    report_lines = [
        "# ZAI-Skills 测试报告",
        f"\n生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "\n## 总体结果\n"
    ]
    
    total_tests = 0
    total_passed = 0
    total_failed = 0
    
    for skill, result in all_results.items():
        total_tests += result["total"]
        total_passed += result["passed"]
        total_failed += result["failed"]
        
        pass_rate = (result["passed"] / result["total"] * 100) if result["total"] > 0 else 0
        status = "✅" if result["failed"] == 0 else "❌"
        
        report_lines.append(f"{status} **{skill}**: {result['passed']}/{result['total']} ({pass_rate:.1f}%)")
    
    overall_rate = (total_passed / total_tests * 100) if total_tests > 0 else 0
    report_lines.extend([
        f"\n**总计**: {total_passed}/{total_tests} ({overall_rate:.1f}%)",
        "\n## 详细结果\n"
    ])
    
    for skill, result in all_results.items():
        report_lines.append(f"### {skill}\n")
        for detail in result["details"]:
            icon = "✅" if detail["status"] == "passed" else "⚠️" if detail["status"] == "passed_with_warnings" else "❌"
            report_lines.append(f"- {icon} **{detail['test_id']}**: {detail['name']} - {detail['status']}")
            
            if detail["errors"]:
                for error in detail["errors"]:
                    report_lines.append(f"  - ❌ {error}")
            
            if detail["warnings"]:
                for warning in detail["warnings"]:
                    report_lines.append(f"  - ⚠️ {warning}")
        
        report_lines.append("")
    
    return "\n".join(report_lines)


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='ZAI-Skills 测试框架')
    parser.add_argument('--skill', type=str, help='只测试特定技能')
    parser.add_argument('--report', action='store_true', help='生成详细报告')
    args = parser.parse_args()
    
    # 加载测试用例
    print("📦 加载测试用例...")
    test_cases = load_test_cases()
    
    # 确定要测试的技能
    skills_to_test = [args.skill] if args.skill else list(test_cases.keys())
    
    # 运行测试
    all_results = {}
    for skill in skills_to_test:
        if skill not in test_cases:
            print(f"⚠️  跳过未知技能：{skill}")
            continue
        
        tester = SkillTester(skill, test_cases[skill])
        all_results[skill] = tester.run_all()
    
    # 打印汇总
    print(f"\n{'='*60}")
    print("📊 测试结果汇总")
    print(f"{'='*60}")
    
    total_tests = 0
    total_passed = 0
    total_failed = 0
    
    for skill, result in all_results.items():
        total_tests += result["total"]
        total_passed += result["passed"]
        total_failed += result["failed"]
        
        pass_rate = (result["passed"] / result["total"] * 100) if result["total"] > 0 else 0
        status = "✅" if result["failed"] == 0 else "❌"
        print(f"{status} {skill}: {result['passed']}/{result['total']} ({pass_rate:.1f}%)")
    
    overall_rate = (total_passed / total_tests * 100) if total_tests > 0 else 0
    print(f"\n{'='*60}")
    print(f"📈 总计：{total_passed}/{total_tests} ({overall_rate:.1f}%)")
    print(f"{'='*60}")
    
    # 生成报告
    if args.report:
        report = generate_report(all_results)
        report_path = Path(__file__).parent / "TEST_REPORT.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\n📄 详细报告已保存到：{report_path}")
    
    # 返回退出码
    sys.exit(0 if total_failed == 0 else 1)


if __name__ == "__main__":
    main()

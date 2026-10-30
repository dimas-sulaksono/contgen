#!/usr/bin/env python3
"""
System Integrity & Quality Gate Validator
Skill: content-gen
Persona: @LeadArchitect & @SkillEngineer
Verifies that all schemas, memory stores, configs, and multi-agent personas
are intact and valid across any host environment.
"""
import json
import os
import sys

# Find root of repo dynamically
current_dir = os.path.dirname(os.path.abspath(__file__))
if os.path.basename(current_dir) == "scripts":
    parent = os.path.dirname(current_dir)
    if os.path.basename(parent) == "content-gen":
        BASE_DIR = os.path.dirname(parent)
    else:
        BASE_DIR = parent
else:
    BASE_DIR = current_dir

SKILL_DIR = os.path.join(BASE_DIR, "content-gen")


def check_file(path, desc):
    if not os.path.exists(path):
        print(f"❌ Missing: {desc} ({os.path.relpath(path, BASE_DIR)})")
        return False
    print(f"✅ Found: {desc} ({os.path.relpath(path, BASE_DIR)})")
    return True


def check_json(path, desc, required_keys=None):
    if not os.path.exists(path):
        print(f"❌ Missing JSON file: {desc}")
        return False
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if required_keys:
            if isinstance(data, dict):
                for k in required_keys:
                    if k not in data:
                        print(f"❌ Missing key '{k}' in {desc}")
                        return False
        print(f"✅ Valid JSON: {desc}")
        return True
    except Exception as e:
        print(f"❌ Invalid JSON in {desc}: {e}")
        return False


def check_jsonl(path, desc):
    if not os.path.exists(path):
        print(f"❌ Missing JSONL file: {desc}")
        return False
    try:
        count = 0
        with open(path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                for req in ["timestamp", "error_type", "bad_pattern", "correction_rule", "scope", "status"]:
                    if req not in obj:
                        print(f"❌ Line {line_no} missing '{req}' in {desc}")
                        return False
                count += 1
        print(f"✅ Valid JSONL ({count} entries): {desc}")
        return True
    except Exception as e:
        print(f"❌ Invalid JSONL in {desc}: {e}")
        return False


def main():
    print("=" * 60)
    print("🔍 RUNNING CONTENT ENGINE PRE-FLIGHT VALIDATION")
    print(f"   Root Directory: {BASE_DIR}")
    print("=" * 60)

    success = True

    # 1. Check Personas
    personas = ["lead-architect", "competitive-analyst", "creative-director", "qa-critic", "skill-engineer"]
    for p in personas:
        p_path = os.path.join(BASE_DIR, ".agents", "personas", f"{p}.md")
        success &= check_file(p_path, f"Persona @{p}")

    # 2. Check Core Meta Prompt & Agent Rules
    success &= check_file(os.path.join(BASE_DIR, "META_PROMPT.md"), "Universal Meta-Prompt")
    success &= check_file(os.path.join(BASE_DIR, "AGENTS.md"), "Agents Configuration")

    # 3. Check Prompts
    prompts = [
        "01_scraper_analyzer.md",
        "02_image_prompt_builder.md",
        "03_caption_copywriter.md",
        "04_critic_evaluator.md",
    ]
    for pr in prompts:
        pr_path = os.path.join(SKILL_DIR, "prompts", pr)
        success &= check_file(pr_path, f"Prompt {pr}")

    # 4. Check Configs & OpenSpec
    success &= check_file(os.path.join(SKILL_DIR, "openspec.yaml"), "OpenSpec Contract")
    success &= check_file(os.path.join(SKILL_DIR, "config", "target_brand.yaml"), "Target Brand Config")
    success &= check_file(os.path.join(SKILL_DIR, "config", "competitors.yaml"), "Competitors Config")
    success &= check_file(os.path.join(SKILL_DIR, "workflows", "ruflo_pipeline.yaml"), "Workflow Pipeline")

    # 5. Check Memory
    success &= check_json(os.path.join(SKILL_DIR, "memory", "brand_matrix.json"), "Brand Matrix Data")
    success &= check_json(os.path.join(SKILL_DIR, "memory", "graphify_nodes.json"), "Knowledge Graph Nodes")
    success &= check_file(os.path.join(SKILL_DIR, "memory", "competitor_patterns.md"), "Competitor Patterns Doc")
    success &= check_file(os.path.join(SKILL_DIR, "memory", "winning_patterns.md"), "Winning Patterns Doc")
    success &= check_jsonl(os.path.join(SKILL_DIR, "memory", "lessons_learned.jsonl"), "Reflexion Loop Memory")

    # 6. Check Assets & References
    ref_dir = os.path.join(SKILL_DIR, "assets", "references")
    if os.path.exists(ref_dir):
        files = [f for f in os.listdir(ref_dir) if not f.startswith(".")]
        print(f"✅ References assets directory: {len(files)} game character images ready")
    else:
        print("❌ References assets directory missing!")
        success = False

    print("=" * 60)
    if success:
        print("🎉 ALL QUALITY GATES PASSED! The repository is ready for production use.")
        return 0
    else:
        print("⚠️ SOME CHECKS FAILED. Please review the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

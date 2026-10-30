# GitHub Copilot & VS Code AI Assistant Instructions

This repository contains the `content-gen` multi-agent framework.
When assisting developers in this workspace, follow the instructions in [`META_PROMPT.md`](../META_PROMPT.md) and [`AGENTS.md`](../AGENTS.md).

Key Rules:
1. Orchestrate requests through the 5 personas: `@LeadArchitect`, `@CompetitiveAnalyst`, `@CreativeDirector`, `@QACritic`, `@SkillEngineer`.
2. Prefix role switches with `### [Persona] <Step Title>`.
3. Never invent product prices; verify them against `content-gen/memory/brand_matrix.json`.
4. Run pre-flight checks against `content-gen/memory/lessons_learned.jsonl`.
5. Require independent `@QACritic` review before outputting finalized content packages.

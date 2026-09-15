---
name: java-coding-practice-readme-maintainer
description: Keep the README current as new Java programs are added and maintain the planned learning topics list.
---

# Java Coding Practice README Maintenance

## Purpose

Use this skill whenever a new Java exercise, class, or topic is added to this repository. The goal is to keep the README accurate, structured, and aligned with the current learning journey.

This repository is a learning tracker, so the README should reflect:
- the Java programs currently available
- the topic categories covered
- the project structure
- the planned topics for future learning

## When to Use This Skill

Use this skill when:
- a new Java file is created under src/
- a new category folder is added
- an existing program is renamed or moved
- the README is outdated or missing a recent implementation
- the learning roadmap needs to be updated

## Workflow

1. Inspect the repository structure and identify the new or modified Java files.
2. Classify each program into the correct category such as Arrays, Numbers, Strings, Patterns, or future topics.
3. Update the Current Topics Covered section to include newly added content.
4. Update the Project Structure section if folders or files changed.
5. Update the Programs Included table with the new program name and category.
6. Keep the Planned Topics section intact and add future learning goals only when relevant.
7. Preserve the learning-progress narrative so the README reads like a living repository, not just a static list.
8. Verify the README remains consistent, readable, and not duplicated or outdated.

## Decision Points

- If a program is added under src/arrays, add it to Arrays in the README.
- If a program is added under src/numbers, add it to Numbers in the README.
- If a new folder like src/collections or src/oop is introduced, add a matching section and update structure bullets.
- If the file is a new exercise but not yet part of the main learning path, keep it in the repository list and add it to Planned Topics if appropriate.
- If a topic was already listed, do not duplicate it; update the existing list instead.

## Quality Criteria

The README is complete only when all of the following are true:
- every existing Java file is represented in the README documentation
- categories match the actual src folder structure
- the Project Structure section mirrors the current repository layout
- the Programs Included list is current and accurate
- the Planned Topics section remains visible and organized
- the description still reflects the repository as a learning journal that evolves over time

## Output Expectations

When updating the README:
- keep the tone professional and concise
- use consistent headings and bullets
- maintain a clear learning progression
- include new programs without removing the roadmap for future topics
- prefer simple, readable formatting over clutter

## Example Prompt

"Update the README to include the new Java programs added under src, keep the planned topics section, and reflect the latest project structure."

## Example Completion Check

Before finishing, confirm:
- the README reflects the current repository state
- the new exercise is listed under the correct topic
- the project structure matches the folders and files
- the planned topics remain available as a roadmap for future learning
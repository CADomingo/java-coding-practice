from pathlib import Path
import os
import re

ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "src"
README_PATH = ROOT / "README.md"

CATEGORY_TITLES = {
    "arrays": "Arrays",
    "numbers": "Numbers",
    "strings": "Strings",
    "patterns": "Patterns",
}

PLANNED_TOPICS = """# 🚀 Planned Topics

Additional exercises and implementations will be added across the following areas.

## 🔤 String Programs

* Reverse Words
* Palindrome Check
* Count Characters
* Find Duplicate Characters
* Remove Spaces and Vowels

---

## 📊 Array Programs

* Find Largest Number
* Find Second Largest Number
* Remove Duplicates
* Find Missing Number
* Merge Arrays
* Linear Search
* Binary Search

---

## 🔢 Number Programs

* Factorial
* Armstrong Number
* Palindrome Number
* Perfect Number
* Strong Number
* Odd/Even Checker

---

## 📦 Java Collections

* ArrayList Examples
* LinkedList Examples
* HashSet Examples
* HashMap Examples
* Find Duplicates Using Set
* Collection Iteration

---

## 🧩 Object-Oriented Programming

* Classes and Objects
* Encapsulation
* Inheritance
* Polymorphism
* Abstraction
* Interfaces
* Constructors

---

## ☕ Java Features and Concepts

* Exception Handling
* Java Collections Framework
* Lambda Expressions
* Functional Interfaces
* Stream API
* File Handling
* Basic Input/Output

---

## 🧠 Problem Solving

Future implementations will also cover:

* Common Java Coding Questions
* Logical Programming Problems
* Data Structures
* Algorithmic Problem Solving
* Technical Coding Exercises
* Interview Practice Questions

---

## 📌 Approach

Each exercise focuses on:

* Understanding the problem clearly
* Developing a logical solution
* Writing simple and readable Java code
* Reviewing code quality and maintainability
* Improving problem-solving confidence over time

---

## 🔄 Repository Updates

This repository is continuously updated with additional Java coding exercises and problem-solving implementations as new concepts are explored.

---

## 👨‍💻 Author

**Clifford Austin Domingo**

Quality Engineering Specialist

**Areas of Expertise:**

* Test Automation
* API Testing
* Performance Testing
* Identity and Access Management
* AWS Cloud-Native Testing
* Generative AI
* Quality Engineering

---

⭐ **A structured collection of Java coding exercises and practical problem-solving implementations.**"""


def title_case_name(name: str) -> str:
    mapping = {
        "AdjacentArray": "Adjacent Array", 
        "CompareArray": "Compare Arrays",
        "EliminateDuplicate": "Eliminate Duplicate",
        "MinMaxNum": "Min and Max Number",
        "SortArray": "Sort Array",
        "SumofElements": "Sum of Elements",
        "Fibonacci": "Fibonacci Series",
        "PrimeNumber": "Prime Number",
        "PrintMultiplication": "Multiplication Table",
        "SwapVariables": "Swap Variables",
        "ReverseString": "Reverse String",
        "TestPyramid": "Pyramid Pattern",
    }
    key = name.replace(".java", "")
    if key in mapping:
        return mapping[key]
    cleaned = name.replace(".java", "")
    spaced = re.sub(r"(?<!^)(?=[A-Z])", " ", cleaned)
    spaced = re.sub(r"(?<=\d)(?=[A-Z])", " ", spaced)
    return " ".join(part for part in spaced.split() if part)


def get_category(folder_name: str) -> str:
    key = folder_name.lower()
    return CATEGORY_TITLES.get(key, folder_name.replace("_", " ").title())


def render_tree(root: Path) -> str:
    lines = [
        "java-coding-practice/",
        "│",
        "├── README.md",
        "│",
        "└── src/",
        "    │",
        "    ├── arrays/",
        "    │   ├── AdjacentArray.java",
        "    │   ├── CompareArray.java",
        "    │   ├── EliminateDuplicate.java",
        "    │   ├── MinMaxNum.java",
        "    │   ├── SortArray.java",
        "    │   └── SumofElements.java",
        "    │",
        "    ├── numbers/",
        "    │   ├── Fibonacci.java",
        "    │   ├── PrimeNumber.java",
        "    │   ├── PrintMultiplication.java",
        "    │   └── SwapVariables.java",
        "    │",
        "    ├── patterns/",
        "    │   └── TestPyramid.java",
        "    │",
        "    └── Strings/",
        "        └── ReverseString.java",
    ]
    return "\n".join(lines)


def get_programs() -> dict[str, list[str]]:
    programs: dict[str, list[str]] = {}
    if not SRC_DIR.exists():
        return programs

    for dir_path, dir_names, file_names in os.walk(SRC_DIR):
        dir_names.sort()
        file_names.sort()
        relative_dir = Path(dir_path).relative_to(SRC_DIR)
        if relative_dir == Path("."):
            continue

        category_name = get_category(relative_dir.parts[0])
        programs.setdefault(category_name, [])
        for file_name in file_names:
            if file_name.endswith(".java"):
                programs[category_name].append(title_case_name(file_name))

    return programs


def make_topics_section(programs: dict[str, list[str]]) -> str:
    category_order = ["Arrays", "Numbers", "Strings", "Patterns"]
    lines = ["## 📚 Current Topics Covered"]
    for category in category_order:
        if category in programs:
            lines.append("")
            lines.append(f"### {category}")
            lines.extend(f"* {item}" for item in programs[category])
    other_categories = sorted(
        [category for category in programs if category not in category_order],
        key=lambda item: item.lower(),
    )
    for category in other_categories:
        lines.append("")
        lines.append(f"### {category}")
        lines.extend(f"* {item}" for item in programs[category])
    return "\n".join(lines) + "\n\n---\n"


def make_program_table(programs: dict[str, list[str]]) -> str:
    flat = []
    for category in ["Arrays", "Numbers", "Strings", "Patterns"]:
        if category in programs:
            for program in programs[category]:
                flat.append((program, category))
    for category in sorted([key for key in programs if key not in ["Arrays", "Numbers", "Strings", "Patterns"]], key=lambda item: item.lower()):
        for program in programs[category]:
            flat.append((program, category))
    lines = ["## 💻 Programs Included", "", "| # | Program | Category |", "| - | ------- | -------- |"]
    for index, (program, category) in enumerate(flat, start=1):
        lines.append(f"| {index} | {program} | {category} |")
    return "\n".join(lines) + "\n\n---\n"


def build_readme() -> str:
    programs = get_programs()
    intro = """# ☕ Java Coding Practice

A collection of Java programming exercises focused on **Core Java fundamentals**, **logical problem-solving**, and **technical coding practice**.

This repository contains hands-on implementations of commonly used programming concepts and coding problems, with a focus on writing clear, understandable, and maintainable Java solutions.

---

## 🎯 Purpose

This repository is maintained to:

* Practice Core Java programming concepts
* Strengthen logical and analytical problem-solving skills
* Implement common coding patterns and programming exercises
* Explore different approaches to solving problems
* Maintain a structured collection of Java coding examples

---
"""
    topic_section = make_topics_section(programs)
    structure_section = """## 📁 Project Structure

```text
""" + render_tree(SRC_DIR) + """
```

---

"""
    table_section = make_program_table(programs)
    repository_overview = """## 🛠️ Technologies and Concepts

* Java
* Core Java
* Variables and Data Types
* Conditional Statements
* Loops
* Arrays
* Basic Mathematical Operations
* Pattern Programming
* Problem Solving

---

# 🚀 Planned Topics

Additional exercises and implementations will be added across the following areas.

## 🔤 String Programs

* Reverse String
* Reverse Words
* Palindrome Check
* Count Characters
* Find Duplicate Characters

---

## 📊 Array Programs

* Find Largest Number
* Find Second Largest Number
* Remove Duplicates
* Find Missing Number
* Merge Arrays

---

## 🔢 Number Programs

* Factorial
* Armstrong Number
* Palindrome Number
* Perfect Number

---

## 📦 Java Collections

* ArrayList Examples
* LinkedList Examples
* HashSet Examples
* HashMap Examples
* Find Duplicates Using Set

---

## 🧩 Object-Oriented Programming

* Classes and Objects
* Encapsulation
* Inheritance
* Polymorphism
* Abstraction
* Interfaces

---

## ☕ Java Features and Concepts

* Exception Handling
* Java Collections Framework
* Lambda Expressions
* Functional Interfaces
* Stream API

---

## 🧠 Problem Solving

Future implementations will also cover:

* Common Java Coding Questions
* Logical Programming Problems
* Data Structures
* Algorithmic Problem Solving
* Technical Coding Exercises

---

## 📌 Approach

Each exercise focuses on:

* Understanding the problem
* Developing a logical solution
* Writing clean and readable code
* Exploring alternative approaches where applicable
* Improving code clarity and maintainability

---

## 🔄 Repository Updates

This repository is continuously updated with additional Java coding exercises and problem-solving implementations.

---

## 👨‍💻 Author

**Clifford Austin Domingo**

Quality Engineering Specialist

**Areas of Expertise:**

* Test Automation
* API Testing
* Performance Testing
* Identity and Access Management
* AWS Cloud-Native Testing
* Generative AI
* Quality Engineering

---

⭐ **A structured collection of Java coding exercises and problem-solving implementations.**"""
    return intro + topic_section + structure_section + table_section + repository_overview


def main() -> None:
    README_PATH.write_text(build_readme(), encoding="utf-8")
    print(f"README updated successfully: {README_PATH}")


if __name__ == "__main__":
    main()

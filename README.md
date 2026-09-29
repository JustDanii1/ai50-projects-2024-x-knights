# Knights

A solution to **Project 1 — Knights** from Harvard's **CS50's Introduction to Artificial Intelligence with Python**.

## About

This project solves a series of **Knights and Knaves** logic puzzles using **propositional logic** and an AI model-checking algorithm.

In these puzzles:

* A **Knight** always tells the truth.
* A **Knave** always lies.
* Each character must be either a Knight or a Knave.

The goal is to represent the information from each puzzle as logical statements and allow the model-checking algorithm to determine which characters are Knights and which are Knaves.

## How It Works

The project represents each character using propositional symbols such as:

```text
AKnight
AKnave
BKnight
BKnave
CKnight
CKnave
```

The knowledge bases describe both the rules of the puzzle and the statements made by the characters.

The program then uses `model_check()` to test possible models and determine which conclusions logically follow from the knowledge base.

## Logic

The project uses logical operators such as:

```text
And
Or
Not
Implication
Biconditional
```

These expressions can be combined to represent statements made by the characters.

For example, the program can represent a relationship such as:

```text
A is a Knight if and only if A's statement is true.
```

The model checker then evaluates the possible combinations of Knights and Knaves.

## Puzzles

The project contains four puzzles:

* **Puzzle 0** — One character, A
* **Puzzle 1** — Two characters, A and B
* **Puzzle 2** — Two characters with conflicting statements
* **Puzzle 3** — Three characters, A, B, and C

Each puzzle requires constructing a knowledge base that allows the AI to logically determine the identity of each character.

## Technologies

* Python
* Propositional Logic
* Model Checking
* Knowledge Representation
* Logical Inference
* Artificial Intelligence

## Running the Project

Run the program with:

```bash
python puzzle.py
```

The program evaluates all four puzzles and prints the conclusions that can be logically determined.

## Project Structure

```text
ai50-projects-2024-x-knights/
├── logic.py
├── puzzle.py
└── README.md
```

`logic.py` contains the logical sentence classes and model-checking algorithm provided by the course.

`puzzle.py` contains the knowledge bases used to solve the Knights and Knaves puzzles.

## Course

**CS50's Introduction to Artificial Intelligence with Python**

**Project 1 — Knights**

Course: [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/?utm_source=chatgpt.com)

Project: [Knights — Project Specification](https://cs50.harvard.edu/ai/projects/1/knights/?utm_source=chatgpt.com)

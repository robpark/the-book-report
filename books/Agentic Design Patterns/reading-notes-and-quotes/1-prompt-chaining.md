# Prompt Chaining

## What

"Complex tasks often overwhelm LLMs when handled within a single prompt, leading to significant performance issues."

## Why

"Prompt chaining provides a standardized solution by breaking down a complex problem into a sequence of smaller,
interconnected sub-tasks."

"This modular, divide-and-conquer strategy makes the process more manageable, easier to debug, and allows for the
integration of external tools or structured data formats between steps."

## Rule of Thumb

"Use this pattern when a task is too complex for a single prompt, involves multiple distinct processing stages, requires
interaction with external tools between steps, or when building Agentic systems that need to perform multi-step
reasoning and maintain state."

---

## Limitations of Single Prompts

"For multifaceted tasks, using a single, complex prompt for a n LLM can be inefficient, causing the model to struggle   
with constraints and instructions, potentially leading to instruction neglect where parts of the prompt are overlooked,
contextual drift where the model loses track of the initial context, error propagation where early errors amplify,
prompts which require a longer context window where the model gets insufficient information to respond back and
hallucination where the cognitive load increases the chance of incorrect information."

## Enhanced Reliability Through Sequential Decomposition

- Use Case: Code Generation and Refinement

## Code Example

A two-step _prompt chain_ that functions as a data processing pipeline.

- The initial stage is designed to parse unstructured text and extract specific information.
- The subsequent stage then receives this extracted output and transforms it into a structured data format.

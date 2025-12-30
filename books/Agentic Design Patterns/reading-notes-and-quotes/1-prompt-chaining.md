# Prompt Chaining

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

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(temperature=0)

# Prompt 1: Extract information
prompt_extract = ChatPromptTemplate.from_template(
    "Extract the technical specifications from the following text:\n\n(text_input)"
)

# Prompt 2: Transform to JSON
prompt_transform = ChatPromptTemplate.from_template(
    "Transform the following specifications into a JSON object with 'cpu', 'memory', "
    "and 'storage' as keys:\n\n(specifications)"
)

# Build the chain
extraction_chain = prompt_extract | llm | StrOutputParser()
full_chain = {"specifications": extraction_chain} | prompt_transform | llm | StrOutputParser()

# Run the chain
input_text = "The new laptop model feature a 3.5 GHz octa-core processor, 16GB of RAM, and a 1TB NVMe SSD."
final_result = full_chain.invoke({"text_input": input_text})

print("\n--- Final JSON Output ---")
print(final_result)

def main():
    print("Hello from 1-prompt-chaining!")


if __name__ == "__main__":
    main()

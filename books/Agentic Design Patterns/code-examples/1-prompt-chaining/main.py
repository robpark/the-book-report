from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def build_prompt_chain():
    llm = ChatOpenAI(temperature=0)

    prompt_extract = ChatPromptTemplate.from_template(
        'Extract the technical specifications from the following text:\n\n{text_input}'
    )

    prompt_transform = ChatPromptTemplate.from_template(
        'Transform the following specifications into a JSON object with "cpu", "memory", '
        'and "storage" as keys:\n\n{specifications}'
    )

    extraction_chain = prompt_extract | llm | StrOutputParser()
    full_chain = {'specifications': extraction_chain} | prompt_transform | llm | StrOutputParser()

    return full_chain


def main():
    print('Prompt Chaining Example\n')
    print('=' * 50)

    input_text = (
        'The new laptop model features a 3.5 GHz octa-core processor, '
        '16GB of RAM, and a 1TB NVMe SSD.'
    )

    print(f'\nInput Text:\n{input_text}\n')
    print('Processing through prompt chain...\n')

    chain = build_prompt_chain()
    result = chain.invoke({'text_input': input_text})

    print('=' * 50)
    print('\nFinal Output:\n')
    print(result)
    print()


if __name__ == '__main__':
    main()

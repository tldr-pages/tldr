# LLM

> A CLI utility and Python library for interacting with Large Language Models, both via remote APIs and models that can be installed and run on your own machine.
> More information: <https://llm.datasette.io/en/stable/>.

- Install LLM using pip:

`pip install llm`

- Install LLM using pipx:

`pipx install llm`

- Set up OpenAI API Key:

`llm keys set openai`

- Run a Prompt:
  
`llm "Ten fun names for a pet pelican"`

- Run a system prompt against a file

`cat myfile.py | llm -s "Explain this code"`

- Install Plugin and Local Models:

`llm install llm-gpt4all`

- Download and run a prompt against the Orca Mini 7B model

`llm -m orca-mini-3b-gguf2-q4_0 'What is the capital of France?'`
  
- Interactive Chat:

`llm chat -m chatgpt`

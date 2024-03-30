# llm

> Interact with Large Language Models (LLMs) via remote APIs and models that can be installed and run on your machine.
> More information: <https://llm.datasette.io/en/stable/help.html>.

- Set up an OpenAI API Key:

`llm keys set openai`

- Run a prompt:

`llm "{{Ten fun names for a pet pelican}}"`

- Run a [s]ystem prompt against a file:

`cat {{path/to/file.py}} | llm --system "{{Explain this code}}"`

- Install packages from PyPI into the same environment as LLM:

`llm install {{package1 package2 ...}}`

- Download and run a prompt against a [m]odel:

`llm --model {{orca-mini-3b-gguf2-q4_0}} "{{What is the capital of France?}}"`

- Have an interactive chat with a specific [m]odel:

`llm chat --model {{chatgpt}}`

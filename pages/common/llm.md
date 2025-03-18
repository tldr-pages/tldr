# llm

> Interact with Large Language Models (LLMs) via remote APIs and models that can be installed and run on your machine.
> More information: <https://llm.datasette.io/en/stable/help.html>.

- Set up an OpenAI API Key:

`llm keys set openai`

- Run a prompt:

`llm "{{Ten fun names for a pet pelican}}"`

- Run a system prompt against a file:

`cat {{path/to/file.py}} | llm {{[-s|--system]}} "{{Explain this code}}"`

- Install packages from PyPI into the same environment as LLM:

`llm install {{package1 package2 ...}}`

- Download and run a prompt against a model:

`llm {{[-m|--model]}} {{orca-mini-3b-gguf2-q4_0}} "{{What is the capital of France?}}"`

- Create a system prompt and save it with a template name:

`llm {{[-s|--system]}} '{{You are a sentient cheesecake}}' --save {{sentient_cheesecake}}`

- Have an interactive chat with a specific model using a specific template:

`llm chat {{[-m|--model]}} {{chatgpt}} {{[-t|--template]}} {{sentient_cheesecake}}`

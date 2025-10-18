# oneliner

> Turn plain English into shell commands using OpenAI, Claude, or local LLMs, designed to teach, not replace your knowledge.
> More information: <https://github.com/dorochadev/oneliner#-usage-flags>.

- Generate a shell command from plain English:

`oneliner "{{find all jpg files larger than 10MB}}"`

- Explain what a command does:

`oneliner {{[-e|--explain]}} "{{delete node_modules recursively}}"`

- Copy a generated command to the clipboard:

`oneliner {{[-c|--clipboard]}} "{{compress all pdfs}}"`

- Show a detailed, educational breakdown of a command:

`oneliner {{[-b|--breakdown]}} "{{list all active network connections}}"`

- Execute a generated command (use with caution):

`oneliner {{[-r|--run]}} "{{list files larger than 1GB}}"`

- Interactively confirm before executing a generated command:

`oneliner {{[-i|--interactive]}} "{{delete temporary files in /tmp}}"`

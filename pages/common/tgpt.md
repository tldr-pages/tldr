# tgpt

> Talk to an AI chatbot without the need for API keys.
> Available providers: `openai`, `opengpts`, `koboldai`, `phind`, `llama2`, `blackboxai`.
> More information: <https://github.com/aandrew-me/tgpt>.

- Chat with the default provider (GPT-3.5-turbo):

`tgpt "{{prompt}}"`

- Start multi-line interactive mode:

`tgpt {{[-m|--multiline]}}`

- Generate images and save them to the current directory:

`tgpt {{[-img|--image]}} "{{prompt}}"`

- Generate code with the default provider (GPT-3.5-turbo):

`tgpt {{[-c|--code]}} "{{prompt}}"`

- Chat with a specific provider quietly (without animations):

`tgpt --provider {{openai|opengpts|koboldai|phind|llama2|blackboxai}} {{[-q|--quiet]}} {{[-w|--whole]}} "{{prompt}}"`

- Generate and execute shell commands using a specific provider (with a confirmation prompt):

`tgpt --provider {{llama2}} {{[-s|--shell]}} "{{prompt}}"`

- Prompt with an API key, model, max response length, temperature, and `top_p` (required when using `openai` provider):

`tgpt --provider openai --key "{{api_key}}" --model "{{gpt-3.5-turbo}}" --max-length {{10}} --temperature {{0.7}} --top_p {{0.9}} "{{prompt}}"`

- Feed a file as additional pre-prompt input:

`tgpt --provider {{blackboxai}} "{{prompt}}" < {{path/to/file}}`

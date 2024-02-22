# tgpt

> Talk to an AI chatbot without the need for API keys.
> Available providers: `openai`, `opengpts`, `koboldai`, `phind`, `llama2`, `blackboxai`.
> More information: <https://github.com/aandrew-me/tgpt>.

- Chat with the default provider (GPT-3.5-turbo):

`tgpt "{{prompt}}"`

- Start [m]ulti-line interactive mode:

`tgpt --multiline`

- Generate [i]mages and save them to the current directory:

`tgpt --image "{{prompt}}"`

- Generate [c]ode with the default provider (GPT-3.5-turbo):

`tgpt --code "{{prompt}}"`

- Chat with a specific provider [q]uietly (without animations):

`tgpt --provider {{openai|opengpts|koboldai|phind|llama2|blackboxai}} --quiet --whole "{{prompt}}"`

- Generate and execute [s]hell commands using a specific provider (with a confirmation prompt):

`tgpt --provider {{llama2}} --shell "{{prompt}}"`

- Prompt with an API key, model, max response length, temperature, and `top_p` (required when using `openai` provider):

`tgpt --provider openai --key "{{api_key}}" --model "{{gpt-3.5-turbo}}" --max-length {{10}} --temperature {{0.7}} --top_p {{0.9}} "{{prompt}}"`

- Feed a file as additional pre-prompt input:

`tgpt --provider {{blackboxai}} "{{prompt}}" < {{path/to/file}}`

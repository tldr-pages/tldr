# llama-cli

> Command-line interface for LLM inference.
> More information: <https://github.com/ggml-org/llama.cpp#llama-cli>.

- Start up LLM [m]odel and interface:

`llama-cli {{[-m|--model]}} {{path/to/model}}`

- Start with setup prompt [c]ontext size:

`llama-cli {{[-m|--model]}} {{path/to/model}} {{[-c|--ctx-size]}} {{number}}`

- Start with set offload [n]umber of layer [g]pu [l]ayers:

`llama-cli {{[-m|--model]}} {{path/to/model}} {{[-ngl|--gpu-layers|--n-gpu-layers]}} {{auto|all|number}}`

- Start with sending content as [sys]tem prompt from a [f]ile:

`llama-cli {{[-m|--model]}} {{path/to/model}} {{[-sysf|--system-prompt-file]}} {{path/to/prompt}}`

- Start with sending content in [f]ile as first prompt:

`llama-cli {{[-m|--model]}} {{path/to/model}} {{[-f|--file]}} {{path/to/prompt}}`

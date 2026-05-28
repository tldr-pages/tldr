# Inference snaps

> Chat with generative AI Language Models that runs locally without internet.
> Here inference-snap is one of the supported models: `deepseek-r1`, `gemma3`, `gemma4`, `nemotron3-nano`, `qwen-vl` .
> More information: <https://documentation.ubuntu.com/inference-snaps/>.

- Start a chat in terminal (and a chat server in background on first start):

`{{inference-snap}} chat`

- Show current engine and status of chat server:

`{{inference-snap}} status`

- Select specific engine (eg. `cuda` for NVIDIA GPU). Download and use the appropriate model for the engine:

`sudo {{inference-snap}} use-engine {{engine}}`

- Show detailed device hardware information (RAM, architecture, etc.):

`sudo {{inference-snap}} show-machine`

- Get all configuration (`http.host`, `http.port`) of running chat server:

`{{inference-snap}} get`

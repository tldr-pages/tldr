# deepseek-r1

> Chat with deepseek-r1, a Language Model that runs locally without internet. A part of Ubuntu Inference Snaps.
> More information: https://documentation.ubuntu.com/inference-snaps/reference/models-cli/ .

- Start a chat in terminal (and a chat server in background on first start):

`deepseek-r1 chat`

- Show current engine and status of chat server:

`deepseek-r1 status`

- Select specific engine (eg. `cuda` for NVIDIA GPU). Download and use the appropriate model for the engine:

`sudo deepseek-r1 use-engine {{engine}}`

- Show detailed device hardware information (RAM, architecture, etc.):

`sudo deepseek-r1 show-machine`

- Get all configuration (`http.host`, `http.port`) of running chat server:

`deepseek-r1 get`

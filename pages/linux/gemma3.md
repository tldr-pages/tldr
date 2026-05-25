# gemma3

> Chat with gemma3, a Language Model that runs locally without internet.
> See more about Ubuntu Inference Snaps: https://documentation.ubuntu.com/inference-snaps/reference/models-cli/ .

- Start a chat in terminal (and a chat server in background on first start):

`gemma3 chat`

- Show current engine and status of chat server:

`gemma3 status`

- Select specific engine (eg. `cuda` for NVIDIA GPU). Download and use the appropriate model for the engine:

`sudo gemma3 use-engine {{engine}}`

- Show detailed device hardware information (RAM, architecture, etc.):

`sudo gemma3 show-machine`

- Get all configuration (`http.host`, `http.port`) of running chat server:

`gemma3 get`

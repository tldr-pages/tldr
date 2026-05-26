# nemotron3-nano

> Chat with nemotron3-nano, a Language Model that runs locally without internet. A part of Ubuntu Inference Snaps.
> More information: https://documentation.ubuntu.com/inference-snaps/reference/models-cli/ .

- Start a chat in terminal (and a chat server in background on first start):

`nemotron3-nano chat`

- Show current engine and status of chat server:

`nemotron3-nano status`

- Select specific engine (eg. `cuda` for NVIDIA GPU). Download and use the appropriate model for the engine:

`sudo nemotron3-nano use-engine {{engine}}`

- Show detailed device hardware information (RAM, architecture, etc.):

`sudo nemotron3-nano show-machine`

- Get all configuration (`http.host`, `http.port`) of running chat server:

`nemotron3-nano get`

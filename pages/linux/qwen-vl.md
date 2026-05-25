# qwen-vl

> Chat with qwen-vl, a Language Model that runs locally without internet.
> See more about Ubuntu Inference Snaps: https://documentation.ubuntu.com/inference-snaps/reference/models-cli/ .

- Start a chat in terminal (and a chat server in background on first start):

`qwen-vl chat`

- Show current engine and status of chat server:

`qwen-vl status`

- Select specific engine (eg. `cuda` for NVIDIA GPU). Download and use the appropriate model for the engine:

`sudo qwen-vl use-engine {{engine}}`

- Show detailed device hardware information (RAM, architecture, etc.):

`sudo qwen-vl show-machine`

- Get all configuration (`http.host`, `http.port`) of running chat server:

`qwen-vl get`

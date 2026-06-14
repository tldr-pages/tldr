# vllmd

> Run and orchestrate vLLM model containers, single-node or across a cluster.
> See also: `vllmd-session`, `vllmd-db`, `vllmd-task`.
> More information: <https://github.com/sroomberg/vllmd>.

- Serve a model on a port (foreground):

`vllmd run --model {{path/to/model}} --port {{port}}`

- Serve a model in the background and wait until the API is ready:

`vllmd run --model {{path/to/model}} --port {{port}} --detach`

- List all running vllmd containers:

`vllmd ps`

- Show container and API health:

`vllmd status`

- Stream container logs:

`vllmd logs --follow`

- Stop a container:

`vllmd stop --name {{container_name}}`

- Stop all vllmd containers:

`vllmd stop --all`

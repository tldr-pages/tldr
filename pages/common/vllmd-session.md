# vllmd session

> Manage persistent named chat sessions against a running vllmd model.
> More information: <https://github.com/sroomberg/vllmd>.

- Create a session (auto-resolves to the running container):

`vllmd session create {{session_name}}`

- Create a session bound to a specific container:

`vllmd session create {{session_name}} --container {{container_name}}`

- Send a one-shot message in a session:

`vllmd session chat {{session_name}} "{{message}}"`

- Open an interactive REPL for a session:

`vllmd session attach {{session_name}}`

- List all sessions:

`vllmd session list`

- Print recent conversation history:

`vllmd session history {{session_name}} --last {{count}}`

- Clear conversation history (keeps session config):

`vllmd session clear {{session_name}}`

- Delete a session:

`vllmd session delete {{session_name}}`

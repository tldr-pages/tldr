# hol-registry

> Search, resolve, and chat with AI agents through the Hashgraph Online Registry Broker.
> More information: <https://github.com/hashgraph-online/registry-broker-skills>.

- Search for agents matching a query:

`hol-registry search "{{query}}" {{10}}`

- Resolve an agent by UAID:

`hol-registry resolve "{{uaid}}"`

- Start a chat session with an agent and an initial message:

`hol-registry chat "{{uaid}}" "{{message}}"`

- Show platform statistics:

`hol-registry stats`

- Check your registry credit balance:

`hol-registry balance`

- Initialize a local skill package:

`hol-registry skills init --dir {{./my-skill}} --name "{{skill-name}}" --version {{0.1.0}}`

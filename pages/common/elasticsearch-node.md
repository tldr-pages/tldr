# elasticsearch-node

> Manage low-level Elasticsearch node operations such as shutdown, repurpose, or viewing info.
> More information: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/node-tool>.

- Display information about the current node:

`elasticsearch-node info`

- Prepare the node for a full cluster restart (e.g., after upgrading):

`elasticsearch-node unsafe-bootstrap`

- Shutdown the node (must be run from the same host where Elasticsearch is installed):

`elasticsearch-node shutdown`

- Repurpose a node for a different role (e.g., from master to data node):

`elasticsearch-node repurpose`

- List the roles assigned to the node:

`elasticsearch-node roles`

- Show the installed JVM version, Elasticsearch home path, and other diagnostic information:

`elasticsearch-node diagnostics`

- Display help:

`elasticsearch-node {{[-h|--help]}}`

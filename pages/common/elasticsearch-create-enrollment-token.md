# elasticsearch-create-enrollment-token

> Create enrollment tokens for Elasticsearch nodes and Kibana instances.
> More information: <https://www.elastic.co/guide/en/elasticsearch/reference/current/create-enrollment-token.html>.

- Create an enrollment token for adding a new Elasticsearch node:

`elasticsearch-create-enrollment-token {{[-s|--scope]}} node`

- Create an enrollment token for adding a new Kibana instance:

`elasticsearch-create-enrollment-token {{[-s|--scope]}} kibana`

- Create an enrollment token and display verbose output:

`elasticsearch-create-enrollment-token {{[-s|--scope]}} node --verbose`

- Create an enrollment token for a Kibana instance with a custom Elasticsearch URL:

`elasticsearch-create-enrollment-token {{[-s|--scope]}} kibana --url "{{IP}}"`

- Display help:

`elasticsearch-create-enrollment-token {{[-h|--help]}}`

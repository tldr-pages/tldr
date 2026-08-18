# llm embed

> Calculate and store embedding vectors for content using Large Language Models.
> More information: <https://llm.datasette.io>.

- Calculate embeddings for content using a specific model:

`llm embed {{[-c|--content]}} "{{text}}" {{[-m|--model]}} {{3-small}}`

- Store an embedding in a collection:

`llm embed {{collection_name}} {{id}} {{[-c|--content]}} "{{text}}"`

- Store an embedding with content and metadata:

`llm embed {{collection_name}} {{id}} {{[-c|--content]}} "{{text}}" --store --metadata '{{{"key": "value"}}}'`

- Calculate embeddings from a file:

`cat {{path/to/file}} | llm embed {{collection_name}} {{id}}`

- Output embeddings in a specific format:

`llm embed {{[-c|--content]}} "{{text}}" {{[-m|--model]}} {{3-small}} --format {{base64|hex|blob}}`

- Calculate embeddings for binary data (e.g., images):

`llm embed --binary {{[-m|--model]}} {{clip}} {{[-i|--input]}} {{path/to/image.jpg}}`

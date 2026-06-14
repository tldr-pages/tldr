# vllmd db

> Manage the vllmd local vector database for document and code context retrieval.
> More information: <https://github.com/sroomberg/vllmd>.

- Ingest a directory of documents into the vector database:

`vllmd db ingest {{path/to/docs}} --type documents --model {{model_name}}`

- Ingest a codebase:

`vllmd db ingest {{path/to/src}} --type code --model {{model_name}}`

- Search for relevant context:

`vllmd db search "{{query}}" --collection {{code|documents}} --model {{model_name}}`

- Sync the vector database to S3:

`vllmd db sync {{s3://bucket/path}} --direction push`

- Pull the vector database from S3:

`vllmd db sync {{s3://bucket/path}} --direction pull`

- Show collection sizes:

`vllmd db stats`

# mongod

> The MongoDB database server.
> More information: <https://docs.mongodb.com/manual/reference/program/mongod>.

- Specify a config file:

`mongod --config {{path/to/file}}`

- Specify the port to listen on:

`mongod --port {{port}}`

- Specify database profiling level. 0 is off, 1 is only slow operations, 2 is all:

`mongod --profile {{0|1|2}}`

# sqsc

> A command line AWS Simple Queue Service client.

- List all queues:

`sqsc lq [queue-prefix]`

- List all messages in a queue:

`sqsc ls <queue-name>`

- Copy all messages from one queue to another:

`sqsc cp <from-queue-name> <to-queue-name>`

- Move all messages from one queue to another:

`sqsc mv <from-queue-name> <to-queue-name>`

- Describe a queue:

`sqsc describe <queue-name>`

- Query a queue with SQL syntax:

`sqsc query "SELECT body FROM <queue-name> WHERE body LIKE '%user%'"`

- Pull all messages in a queue into a local sqlite database:

`sqsc pull <queue-name>`

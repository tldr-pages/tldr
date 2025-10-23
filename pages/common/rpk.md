# rpk

> Manage topics, clusters, groups, security and more via a single binary.
> More information: <https://docs.redpanda.com/current/reference/rpk/>.

- Display version:

`rpk version`

- Create a new topic:

`rpk topic create {{topic_name}}`

- Produce a message to a topic:

`rpk topic produce {{topic_name}}`

- Consume messages from a topic:

`rpk topic consume {{topic_name}}`

- List all topics:

`rpk topic list`

- Display cluster information:

`rpk cluster info`

- List all consumer groups:

`rpk group list`

- Describe a consumer group with lag information:

`rpk group describe {{group_name}}`

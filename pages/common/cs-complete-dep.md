# cs complete dep

> Allows the developer to search for libraries without searching directly on the web but from the command line.
> More information: <https://get-coursier.io/docs/cli-complete>.

- Print which artifacts are published under a specific Maven group identifier:

`cs complete-dep {{group_id}}`

- List published library versions under a specific Maven group identifier and an artifact one:

`cs complete-dep {{group_id}}:{{artifact_id}}`

- Print which artifacts are pubblished under a given Maven groupId searching in the ivy2local:

`cs complete-dep {{group_id}} --repository ivy2local`

- List published artifacts under a Maven group identifier searching in a specific repository and credentials:

`cs complete-dep {{group_id}}:{{artifact_id}} --repository {{repository_url}} --credentials {{user}}:{{password}}`

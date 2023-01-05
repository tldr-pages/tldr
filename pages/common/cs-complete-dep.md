# cs fetch

> Allows the developer to search for libraries without searching directly on the web but from the command line.
> More information: <https://get-coursier.io/docs/cli-fetch>.

- Print which artifacts are published under a given Maven groupId:

`cs complete-dep {{groupId}}`

- Print which versions of a library are published under a given Maven groupId and artifactId:

`cs complete-dep {{groupId}}:{{artifactId}}`

- Print which articats are pubblished under a given Maven groupId searching in the ivy2local:

`cs complete-dep {{groupId}} --repository ivy2local`

- Print which articats are pubblished under a given Maven groupId searching in a custom repo with specified credentials:

`cs complete-dep {{groupId}}:{{artifactId}} --repository {{repoUrl}} --credentials {{user}}:{{password}}`

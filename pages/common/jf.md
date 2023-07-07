# jf

> Use JF CLI for interfacing with JFrog products like Artifactory, Xray, Distribution, Pipelines and Mission Control
> More information: <https://jfrog.com/help/r/jfrog-cli/usage>

- Add new configuration:

`jf config add `

- Show current configuration:

`jf config show`

- Artifactory: Search artifacts within given repository and directory:

`jf rt search --recursive {{repostiory_name}}/{{path}}/`
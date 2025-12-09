# git request-pull

> Generate a request asking the upstream project to pull changes into its tree.
> More information: <https://git-scm.com/docs/git-request-pull>.

- Produce a request summarizing the changes between the v1.1 release and a specified branch:

`git request-pull {{v1.1}} {{https://example.com/project}} {{branch_name}}`

- Produce a request summarizing the changes between the v0.1 release on the `foo` branch and the local `bar` branch:

`git request-pull {{v0.1}} {{https://example.com/project}} {{foo:bar}}`

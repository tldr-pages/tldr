# git request-pull

> Generate a request asking the upstream project to pull changes into its tree.
> More information: <https://git-scm.com/docs/git-request-pull>.

- Produce a request summarizing the changes between the v1.1 release and main:

`git request-pull {{v1.1}} {{https://example.com/project}} {{main}}`

- Produce a request summarizing the changes between the v0.1 release on main branch and local foo branch:

`git request-pull {{v0.1}} {{https://example.com/project}} {{main:foo}}`

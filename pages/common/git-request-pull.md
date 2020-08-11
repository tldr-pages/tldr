# git request-pull

> Generate a request asking the upstream project to pull changes into its tree.
> More information: <https://git-scm.com/docs/git-request-pull>.

- Produce a request summarizing the changes between the v1.1 release and master:

`git request-pull {{v1.1}} {{https://example.com/project}} {{master}}`

- Produce a request summarizing the changes between the v0.1 release on master branch and local foo branch:

`git request-pull {{v0.1}} {{https://example.com/project}} {{master:foo}}`

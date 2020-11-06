# vela

> Command line tools for vela pipeline
> More information: <https://go-vela.github.io/docs/>.

- Trigger pipeline to run from git tagged version:

`vela add deployment --org {{git org}} --repo {{repo name}} --target {{dev/stage/prod/other}} --ref refs/tags/{{git tag}} --description "{{Deploy description}}"`

# hadolint

> A Haskell Dockerfile linter.
> Checks for optimizations and likely failures, resulting in cleaner code, no errors and possibly a smaller Docker image.
> More information: <https://github.com/hadolint/hadolint>.

- Install hadolint as a docker image:

`docker run --rm -i hadolint/hadolint`

- Configure hadolint to ignore all errors pointed out by hadolint in the Dockerfile:

`docker run --rm -i hadolint/hadolint hadolint --ignore {{error code}} -`

- Configure hadolint to ignore in entire Dockerfile by mounting configuration YAML file:

`docker run --rm -i -v ${PWD}/.hadolint.yml:/.hadolint.yaml hadolint/hadolint`

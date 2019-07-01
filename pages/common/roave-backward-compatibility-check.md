# roave-backward-compatibility-check

> A tool that can be used to verify backward compatibility breaks between two versions of a PHP library.
> More information: <https://github.com/Roave/BackwardCompatibilityCheck>.

- Check for breaking changes since the last tag:

`roave-backward-compatibility-check`

- Check for breaking changes since a specific tag:

`roave-backward-compatibility-check --from={{git_reference}}`

- Check for breaking changes between the last tag and a specific reference:

`roave-backward-compatibility-check --to={{git_reference}}`

- Check for breaking changes and output to markdown:

`roave-backward-compatibility-check --format=markdown > {{results.md}}`

# semver

> Semantic version string parser.
> More information: <https://github.com/npm/node-semver>.

- Check if a version string respects the semantic versioning format (prints an empty string if it does not match):

`semver {{1.2}}`

- Convert a version string to the semantic versioning format:

`semver --coerce {{1.2}}`

- Test if `1.2.3` matches the `^1.0` range (prints an empty string if it does not match):

`semver {{1.2.3}} --range "{{^1.0}}"`

- Test with multiple ranges:

`semver {{1.2.3}} --range {{">=1.0"}} {{"<2.0"}}`

- Test multiple version strings and return only the ones that match:

`semver {{1.2.3}} {{2.0.0}} --range "{{^1.0}}"`

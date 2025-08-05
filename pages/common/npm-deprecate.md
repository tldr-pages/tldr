# npm deprecate

> Mark a version or range of versions of an `npm` package as deprecated.
> More information: <https://docs.npmjs.com/cli/npm-deprecate/>.

- Deprecate a specific version of a package:

`npm deprecate {{package_name}}@{{version}} "{{deprecation_message}}"`

- Deprecate a range of versions of a package:

`npm deprecate {{package_name}}@"<{{version_range}}" "{{deprecation_message}}"`

- Un-deprecate a specific version of a package:

`npm deprecate {{package_name}}@{{version}} ""`

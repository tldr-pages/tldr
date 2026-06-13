# dart

> Manage Dart projects.
> More information: <https://dart.dev/tools/dart-tool>.

- Initialize a new Dart project in a directory of the same name:

`dart create {{project_name}}`

- Run a Dart file:

`dart run {{path/to/file.dart}}`

- Download dependencies for the current project:

`dart pub get`

- Run unit tests for the current project:

`dart test`

- Update an outdated project's dependencies to support null-safety:

`dart pub upgrade --null-safety`

- Compile a Dart file to a native binary:

`dart compile exe {{path/to/file.dart}}`

- Apply automated fixes to the current project:

`dart fix --apply`

# gradle init

> Initialize a new Gradle project interactively.
> More information: <https://docs.gradle.org/current/userguide/build_init_plugin.html>.

- Initialize a new Gradle project interactively:

`gradle init`

- Initialize a project of a specific type:

`gradle init --type {{basic|java-application|java-library|...}}`

- Initialize a project with a specific DSL:

`gradle init --dsl {{groovy|kotlin}}`

- Initialize a project with a specific test framework:

`gradle init --test-framework {{junit-jupiter|testng|spock}}`

- Initialize a project without interactive prompts:

`gradle init --type {{java-application}} --dsl {{kotlin}} --test-framework {{junit-jupiter}}`

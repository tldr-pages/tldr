# mvn generate-sources

> Generate source code for a Maven project before the main compilation phase.
> This phase runs after `initialize` and before `process-sources`.
> More information: <https://manned.org/mvn>.

- Run all lifecycle phases up to `generate-sources`:

`mvn generate-sources`

- Run the next phase to generate resources:

`mvn generate-resources`

- Clean and regenerate sources:

`mvn clean generate-sources`

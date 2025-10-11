# mvn archetype

> Generate a new Maven project from a predefined template (archetype).
> More information: <https://maven.apache.org/archetype/maven-archetype-plugin/usage.html>.

- Generate a new project interactively:

`mvn archetype:generate`

- Generate a project non-interactively with specific archetype and project parameters:

`mvn archetype:generate --define archetypeGroupId={{group_id}} --define archetypeArtifactId={{artifact_id}} --define archetypeVersion={{version}} --define groupId={{project_group_id}} --define artifactId={{project_name}} --define interactiveMode=false`

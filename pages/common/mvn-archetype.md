# mvn archetype

> Generate a new Maven project from a predefined template (archetype).
> More information: <https://maven.apache.org/archetype/maven-archetype-plugin/usage.html>.

- Generate a new project interactively:

`mvn archetype:generate`

- Generate a project non-interactively with specific archetype and project parameters:

`mvn archetype:generate \
  {{[-D|--define]}} archetypeGroupId={{group_id}} \
  {{[-D|--define]}} archetypeArtifactId={{artifact_id}} \
  {{[-D|--define]}} archetypeVersion={{version}} \
  {{[-D|--define]}} groupId={{project_group_id}} \
  {{[-D|--define]}} artifactId={{project_name}} \
  {{[-D|--define]}} interactiveMode=false`

# unity

> A tool for installing and managing Unity Editors, projects and modules.
> More information: <https://docs.unity.com/en-us/unity-cli/unity-cli-reference>.

- Install a specific version of the Unity Editor:

`unity install "{{unity_version}}"`

- Log in to your Unity account:

`unity auth login`

- Install modules interactively:

`unity install-modules`

- Create a new Universal Render Pipeline 2D project:

`unity projects new "{{project_name}}" --template com.unity.template.universal-2d --path "{{/path/to/project_parent_dir}}"`

- Open an existing project:

`unity open "{{/path/to/project}}"`

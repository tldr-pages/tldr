# unity

> A tool for installing and managing Unity Editors, projects, and modules.
> More information: <https://docs.unity.com/en-us/unity-cli/unity-cli-reference>.

- Install a specific version of the Unity Editor:

`unity {{[i|install]}} "{{unity_version}}"`

- Log in to your Unity account:

`unity {{[a|auth]}} login`

- Install modules interactively:

`unity {{[im|install-modules]}}`

- Create a new Universal Render Pipeline 2D project:

`unity {{[p|projects]}} new "{{project_name}}" --template com.unity.template.universal-2d --path "{{path/to/parent_directory}}"`

- Open an existing project:

`unity open "{{path/to/project_directory}}"`

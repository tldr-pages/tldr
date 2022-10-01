# projucer

> A project manager for JUCE framework applications.
> More information: <https://juce.com/discover/stories/projucer-manual#10.4-command-line-tools>.

- Display the help manual:

`projucer --help`

- Display information about the project:

`projucer --status`

- Resave all files and resources in a project:

`projucer --resave {{project_file}}`

- Update the version number in a project:

`projucer --set-version {{version_number}} {{project_file}}`

- Generate a JUCE project from a PIP file:

`projucer --create-project-from-pip {{path/to/PIP}} {{path/to/output}}`

- Remove all JUCE-style comments (`//=====` or `//-----` or `///////`):

`projucer --tidy-divider-comments {{target_folder}}`

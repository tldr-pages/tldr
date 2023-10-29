# xcodes runtimes

> Manage Xcode Simulator runtimes.
> More information: <https://github.com/xcodesorg/xcodes>.

- Display all available Simulator runtimes:

`xcodes runtimes --include-betas`

- Download a Simulator runtime:

`xcodes runtimes download {{runtime_name}}`

- Download and install a Simulator runtime:

`xcodes runtimes install {{runtime_name}}`

- Download/install a Simulator runtime for specific iOS/watchOS/tvOS/visionOS version (must be written as case-sensitive):

`xcodes runtimes {{download|install}} "{{iOS|watchOS|tvOS|visionOS}} {{runtime_version}}"`

- Set a specific location where the runtime archive will be first downloaded (defaults to `~/Downloads`):

`xcodes runtimes {{download|install}} {{runtime_name}} --directory {{path/to/directory}}`

- Do not delete the downloaded archive when the Simulator is successfully installed:

`xcodes runtimes install {{runtime_name}} --keep-archive`

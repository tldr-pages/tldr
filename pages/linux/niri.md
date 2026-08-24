# niri

> A scrollable-tiling Wayland compositor.
> More information: <https://github.com/YaLTeR/niri>.

- List all outputs and their properties:

`niri msg outputs`

- Turn off an output (monitor):

`niri msg output {{output_name}} off`

- Focus the workspace below the current one:

`niri msg action focus-workspace-down`

- Focus the workspace above the current one:

`niri msg action focus-workspace-up`

- Move the current workspace down:

`niri msg action move-workspace-down`

- Close the currently focused window:

`niri msg action close-window`

- Focus a specific workspace by index:

`niri msg action focus-workspace {{workspace_index}}`

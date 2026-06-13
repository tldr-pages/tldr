# quickemu

> Build and manage highly optimised desktop virtual machines quickly.
> Note: Virtual machine must be in stopped state when working with snapshots.
> See also: `quickget`.
> More information: <https://github.com/quickemu-project/quickemu>.

- Create and run a virtual machine from a configuration file:

`quickemu --vm {{path/to/file.conf}}`

- Do not commit any changes to disk/snapshot but write any changes to temporary files:

`quickemu --status-quo --vm {{path/to/file.conf}}`

- Start the virtual machine in full-screen mode (`<Ctrl Alt f>` to exit) and select the display backend (`sdl` by default):

`quickemu --fullscreen --display {{sdl|gtk|spice|spice-app|none}} --vm {{path/to/file.conf}}`

- Select a virtual audio device to emulate and create a desktop shortcut:

`quickemu --sound-card {{intel-hda|ac97|es1370|sb16|none}} --shortcut --vm {{path/to/file.conf}}`

- Create/restore/delete a snapshot:

`quickemu --snapshot {{create|apply|delete}} {{tag}} --vm {{path/to/file.conf}}`

- List available snapshots:

`quickemu --snapshot info --vm {{path/to/file.conf}}`

- Delete the entire virtual machine and its configuration:

`quickemu --delete-vm --vm {{path/to/file.conf}}`

- Delete the virtual machine's disk image and EFI variables:

`quickemu --delete-disk --vm {{path/to/file.conf}}`

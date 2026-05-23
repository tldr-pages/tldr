# pdisk

> Apple partition table editor.
> Does not support Intel/DOS partition tables; see also: `fdisk`, `gpt`.
> More information: <https://keith.github.io/xcode-man-pages/pdisk.8.html>.

- List Apple partition tables for all available devices:

`sudo pdisk {{[-l|--list]}}`

- Open a device in read-only mode to inspect its Apple partition table:

`sudo pdisk {{[-r|--readonly]}} {{/dev/sdX}}`

- Start the interactive editor for a device (changes are only saved after writing):

`sudo pdisk {{/dev/sdX}}`

- Print the partition table from the interactive editor:

`<p>`

- Quit the interactive editor without saving changes:

`<q>`

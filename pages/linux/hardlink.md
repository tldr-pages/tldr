# hardlink

> Consolidate duplicate files by replacing them with hard links.
> Part of `util-linux`, useful for saving disk space when identical files exist across directories.
> More information: <https://manned.org/hardlink>.

- Perform a dry run without modifying files:

`hardlink {{[-n|--dry-run]}} {{path/to/directory}}`

- Hardlink duplicate files in a directory:

`hardlink {{path/to/directory}}`

- Hardlink duplicate files in multiple directories:

`hardlink {{path/to/directory1 path/to/directory2 ...}}`

- Display verbose output while hardlinking:

`hardlink {{[-v|--verbose]}} {{path/to/directory}}`

- Only consider files with a minimum size:

`hardlink {{[-s|--minimum-size]}} {{size}} {{path/to/directory}}`

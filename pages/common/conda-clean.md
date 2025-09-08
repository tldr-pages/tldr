# conda clean

> Delete temporary or unused files: index cache, lock files, unused cache packages, tarballs, and log files.
> More information: <https://docs.conda.io/projects/conda/en/stable/commands/clean.html>.

- Delete [a]ll temporary or unused files [v]erbosely. Say [y]es to all confirmations:

`conda clean {{[-avy|--all --verbose --yes]}}`

- Delete only [i]ndex cache, [t]arballs, and [l]og files:

`conda clean {{[-itl|--index-cache --tarballs --logfiles]}}`

- Delete only temporary [c]ache files that could not be deleted earlier due to being in-use:

`conda clean {{[-c|--tempfiles]}} {{/path/to/tempfiles}}`

- Delete only unused [p]ackages. Might delete packages installed with softlinks:

`conda clean {{[-p|--packages]}}`

- [f]orce delete all writable packages. More broad than the `[-a|--all]` option. Will delete packages installed with softlinks:

`conda clean {{[-f|--force-pkgs-dirs]}}`

- Display detailed [h]elp message:

`conda clean {{[-h|--help]}}`

# alr

> Ada package manager.
> Manage Ada toolchains, dependencies, tools and libraries.
> More information: <https://alire.ada.dev/docs/#first-steps>.

- Create a binary or library project:

`alr init {{--bin|--lib}} {{project_name}}`

- Add a dependency to the project:

`alr add {{crate}}`

- Run the compiled binary (no need to do `build` before):

`alr run`

- Compile the project:

`alr build {{--release|--development|--validation}}`

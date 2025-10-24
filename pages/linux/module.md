# module

> Modify a users' environment.
> More information: <https://lmod.readthedocs.io/en/latest/010_user.html>.

- Display available modules:

`module avail`

- Search for a module by name:

`module avail {{module_name}}`

- Load a module:

`module load {{module_name}}`

- Display loaded modules:

`module list`

- Unload a specific loaded module:

`module unload {{module_name}}`

- Unload all loaded modules:

`module purge`

- Specify user-created modules:

`module use {{path/to/module_file1 path/to/module_file2 ...}}`

- Save the current set of loaded modules:

`module save {{collection_name}}`

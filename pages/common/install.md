# install

> Copy files and set attributes.
> Similar to "cp", but allows you to control the attributes of destination files.

- Copy files to destination:

`install {{path/to/source}} {{path/to/destination}}`

- Copy and set ownership to destination:

`install -o {{user}} {{path/to/source}} {{path/to/destination}}`

- Copy and set group ownership to destination:

`install -g {{user}} {{path/to/source}} {{path/to/destination}}`

- Copy and set permissions to destination:

`install -m {{mode}} {{path/to/source}} {{path/to/destination}}`

- Copy and apply access/modification times of source to destination:

`install -p {{path/to/source}} {{path/to/destination}}`

# update-alternatives

> A convenient tool for maintaining symbolic links to determine default commands.

- Add a symbolic link:

`sudo update-alternatives --install {{link}} {{name}} {{path}} {{priority}}`

- Configure a symbolic link:

`sudo update-alternatives --config {{name}}`

- Remove a symbolic link:

`sudo update-alternatives --remove {{name}} {{path}}`

- Display information about a specified command:

`update-alternatives --display {{name}}`

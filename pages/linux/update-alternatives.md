# update-alternatives

> A convenient tool for maintaining symbolic links to determine default commands.

- Add a symbolic link:

`sudo update-alternatives --install {{link}} {{name}} {{path}} {{priority}}`

- Add a symbolic link for "java" with a priority of "300"

`sudo update-alternatives --install /usr/bin/java java /opt/java/jdk1.8.0_102/bin/java 300`

- Configure a symbolic link:

`sudo update-alternatives --config {{name}}`

- Remove a symbolic link:

`sudo update-alternatives --remove {{name}} {{path}}`

- Display information about a specified command:

`update-alternatives --display {{name}}`

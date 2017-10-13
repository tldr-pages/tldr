# update-alternatives

> A convenient tool for maintaining symbolic links determining default commands.

- Add a symbolic link:

`sudo update-alternatives --install /usr/bin/java java /opt/java/jdk1.8.0_102/bin/java 300`

- Config a symbolic link:

`sudo update-alternatives --config java`

- Remove a symbolic link:

`sudo update-alternatives --remove java /usr/bin/java`

- Display information about the link group:

`update-alternatives --display java`

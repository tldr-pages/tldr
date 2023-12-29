# sport

> Search and install SlackBuilds.
> More information: <http://slackermedia.info/handbook/doku.php?id=slackbuilds>.

- Pull the list of SlackBuilds to run `sport` for the first time:

`sudo mkdir -p /usr/ports && sudo rsync -av rsync://slackbuilds.org /slackbuilds/$(awk '{print $2}' /etc/slackware-version)/ /usr/ports/`

- Pull in any updates to the system's tree via `rsync`:

`sudo sport rsync`

- Search for a package by name:

`sport search "{{keyword}}"`

- Check if a package is installed:

`sport check {{package}}`

- Display README and `.info` files of a package:

`sport cat {{package}}`

- Install a package once the dependencies are resolved:

`sudo sport install {{package}}`

- Install a list of packages from a file (format: packages separated by spaces):

`sudo sport install $(< {{path/to/list}})`

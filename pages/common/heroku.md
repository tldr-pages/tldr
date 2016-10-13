# heroku

> A tool for creating and managing Heroku apps from the command line.

- Install for Debian/Ubuntu systems.

`wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh`

- Install standalone version.

`wget -qO- https://toolbelt.heroku.com/install.sh | sh`

- Verify your installation.

`heroku --version`

- Login to your heroku account.

`herolu login`

- Create a heroku app.

`heroku create`

- Uninstall for Debian/Ubuntu systems.

`sudo apt-get remove heroku-toolbelt`

`sudo rm /etc/apt/sources.list.d/heroku.list`

- Uninstall standalone version.

`rm -rf /usr/local/heroku`

`rm -rf ~/.heroku ~/.local/share/heroku ~/.config/heroku ~/.cache/heroku`

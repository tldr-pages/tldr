# shiny-mirrors

> Generate a pacman mirror list for Manjaro Linux.
> Every run of shiny-mirrors requires you to synchronize your database and update your system using `sudo pacman -Syyu`.

- Get the status of the current mirrors:

`shiny-mirrors status`

- Generate a mirror list using the default behavior:

`sudo shiny-mirrors refresh`

- Display the current settings file:

`shiny-mirrors config show`

- Switch to a different branch:

`sudo shiny-mirrors config --branch`

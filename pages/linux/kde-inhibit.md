# kde-inhibit

> Inhibit various desktop functions while a command runs.
> More information: <https://invent.kde.org/plasma/kde-cli-tools/-/blob/master/kdeinhibit/main.cpp>.

- Inhibit power management:

`kde-inhibit --power {{command}} {{command_arguments}}`

- Inhibit screen saver:

`kde-inhibit --screenSaver {{command}} {{command_arguments}}`

- Launch VLC, and inhibit color correction (night mode) while it's running:

`kde-inhibit --colorCorrect {{vlc}}`

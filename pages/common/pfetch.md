# pfetch

> Display system information.
> More information: <https://github.com/dylanaraps/pfetch>.

- Display the ASCII art and default fields:

`pfetch`

- Display only the ASCII art and color palette fields:

`PF_INFO="{{ascii palette}}" pfetch`

- Display all possible fields:

`PF_INFO="{{ascii title os host kernel uptime pkgs memory shell editor wm de palette}}" pfetch`

- Display a different username and hostname:

`USER="{{user}}" HOSTNAME="{{hostname}}" pfetch`

- Display without colors:

`PF_COLOR={{0}} pfetch`

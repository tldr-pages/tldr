# iewzd

> Internet Explorer Setup Wizard:  Programmatically configure installation of Internet Explorer.
> Not to be confused with `iesetup`, which also bundles a customized version of Internet Explorer and `iewzd`.
> Note: You may need to replace the `iewzd` command with your desired IE version and executable, such as `Ie11wzd.exe`, `ie10_setup.exe`, or `IE9-Windows6.0-x86-en-us.exe`.
> More information: <https://learn.microsoft.com/previous-versions/windows/internet-explorer/ie-it-pro/internet-explorer-11/ie11-ieak/ie-setup-command-line-options-and-return-codes>.

- View the documentation for `iesetup`:

`tldr {{[-p|--platform]}} windows iesetup`

- Run the Internet Explorer Wizard:

`iewzd`

- Force or do not restart the computer after installing Internet Explorer:

`iewzd {{/norestart|/forcerestart}}`

- Do not set Internet Explorer as the default browser:

`iewzd /no-default`

- Do not check for Internet Explorer updates:

`iewzd /update-no`

- Run the Wizard in passive (no interaction) or quiet (no interaction and output) mode:

`iewzd {{/passive|/quiet}}`

- Save the installation log to a file:

`iewzd /log {{path\to\file}}`

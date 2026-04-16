# iesetup

> Build customized Internet Explorer Wizard (`iewzd`) installer.
> Part of Internet Explorer Administration Kit (IEAK).
> Note: You may need to replace the `iesetup` command with your desired IEAK version and executable, such as `Ie11setup` for IE 11.
> More information: <https://learn.microsoft.com/previous-versions/windows/internet-explorer/ie-it-pro/internet-explorer-11/ie11-ieak/iexpress-command-line-options>.

- View the documentation for `iewzd`:

`tldr {{[-p|--platform]}} windows iewzd`

- Build a custom Internet Explorer Wizard executable, specifying the location of `iewzd` executable:

`iesetup /c:"iewzd"`

- Apply custom `iewzd` program arguments into the custom installer:

`iesetup /c:"iewzd {{iewzd_args}}"`

- Run the build process in a [q]uiet mode, assuming the user account invoking this command as an [a]dministrator or regular [u]ser:

`iesetup /q:{{a|u}} /c:"iewzd {{iewzd_args}}"`

- [a]sk, [n]ever, or alway[s] [r]estart the computer after successful Internet Explorer installation:

`iesetup /r:{{a|n|s}} /c:"iewzd {{iewzd_args}}"`

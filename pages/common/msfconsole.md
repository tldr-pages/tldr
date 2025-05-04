# msfconsole

> Console for the Metasploit Framework.
> More information: <https://docs.rapid7.com/metasploit/msf-overview>.

- Launch the console:

`msfconsole`

- Launch the console quietly without any banner:

`msfconsole {{[-q|--quiet]}}`

- Do not enable database support:

`msfconsole {{[-n|--no-database]}}`

- Execute console commands (Note: Use `;` for passing multiple commands):

`msfconsole {{[-x|--execute-command]}} "{{use auxiliary/server/capture/ftp; set SRVHOST 0.0.0.0; set SRVPORT 21; run}}"`

- Display help:

`msfconsole {{[-h|--help]}}`

- Display version:

`msfconsole {{[-v|--version]}}`

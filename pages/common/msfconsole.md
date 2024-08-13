# msfconsole

> Console for the Metasploit Framework.
> More information: <https://docs.rapid7.com/metasploit/msf-overview>.

- Launch the console:

`msfconsole`

- Launch the console [q]uietly without any banner:

`msfconsole --quiet`

- Do [n]ot enable database support:

`msfconsole --no-database`

- E[x]ecute console commands (Note: use `;` for passing multiple commands):

`msfconsole --execute-command "{{use auxiliary/server/capture/ftp; set SRVHOST 0.0.0.0; set SRVPORT 21; run}}"`

- Display [v]ersion:

`msfconsole --version`

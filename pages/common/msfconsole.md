# msfconsole

> Console for the Metasploit Framework.
> Note: Run `sudo msfdb init` to enable the Metasploit database backend prior to launching `msfconsole`.
> More information: <https://docs.rapid7.com/metasploit/msf-overview/>.

- Launch the interactive console (append `--quiet` to suppress the startup banner):

`sudo msfconsole`

- Execute console commands (Note: Use `;` for passing multiple commands):

`sudo msfconsole {{[-x|--execute-command]}} "{{use auxiliary/scanner/portscan/tcp; set PORTS 80,443; set RHOSTS example.com; run; quit}}"`

- Run a specific resource file:

`sudo msfconsole {{[-r|--resource]}} {{path/to/file.rc}}`

- [Interactive] Show specific type of modules:

`show {{auxiliary|encoders|evasion|exploits|nops|payloads|post}}`

- [Interactive] Use a module:

`use {{auxiliary/scanner/portscan/syn}}`

- [Interactive] Show module options (module needs to be loaded first):

`show options`

- [Interactive] Set value of variable:

`set {{variable_name}} {{value}}`

- [Interactive] Run a module (module needs to be loaded and options need to be set first):

`{{run|exploit}}`

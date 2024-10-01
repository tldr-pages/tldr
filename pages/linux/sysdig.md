# sysdig

> System troubleshooting, analysis and exploration
> Capture, filter and store systemcalls
> More information : <https://github.com/draios/sysdig/wiki>

- Capture all the events from the live system and print them to screen

`sysdig`

- Capture all the events from the live system and save them to disk

`sysdig -w {filename}.scap`

- Read events from a file and print them to screen

`sysdig -r {filename}.scap`

- Filter and Print all the open system calls invoked by cat

`sysdig proc.name=cat and evt.type=open`

- Register any found plugin and use dummy as input source passing to it open params

`sysdig -I dummy:10'`

- List the available chisels

`sysdig -cl`

- Use the spy_ip chisel to look at the data exchanged with ip address:

`sysdig -c spy_ip {ip_address}`

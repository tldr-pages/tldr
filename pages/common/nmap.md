# nmap

> Network exploration tool and security/port scanner.
> Some features (e.g. SYN scan) activate only when `nmap` is run with root privileges.
> See also: `hping3`, `masscan`, `naabu`, `rustscan`, `zmap`.
> More information: <https://nmap.org/book/man.html>.

- Scan the top 1000 ports of a remote host with various [v]erbosity levels:

`nmap -v{{1|2|3}} {{ip_or_hostname}}`

- Run a ping sweep over an entire [s]ub[n]et or individual hosts very aggressively:

`nmap -T5 -sn {{192.168.0.0/24|ip_or_hostname1,ip_or_hostname2,...}}`

- Enable OS detection, version detection, script scanning, and traceroute of hosts from a file:

`sudo nmap -A -iL {{path/to/file.txt}}`

- Scan a specific list of [p]orts (use `-p-` for all ports from 1 to 65535):

`nmap -p {{port1,port2,...}} {{ip_or_host1,ip_or_host2,...}}`

- Perform service and version detection of the top 1000 ports using default NSE scripts, writing results (`-oA`) to output files:

`nmap -sC -sV -oA {{top-1000-ports}} {{ip_or_host1,ip_or_host2,...}}`

- Scan target(s) carefully using `default and safe` NSE scripts:

`nmap --script "default and safe" {{ip_or_host1,ip_or_host2,...}}`

- Scan for web servers running on standard [p]orts 80 and 443 using all available `http-*` NSE scripts:

`nmap --script "http-*" {{ip_or_host1,ip_or_host2,...}} -p 80,443`

- Evade IDS/IPS using a slow SYN scan, 10 random [D]ecoys, source port 53, [f]ragmentation, random data, no DNS or host discovery:

`sudo nmap -sS -T1 -D RND:10 --source-port 53 -f --data-length {{16}} -Pn -n {{ip_or_host}}`

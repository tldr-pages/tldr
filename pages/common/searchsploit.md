# searchsploit

> Search Exploit Database for exploits, shellcodes and/or papers.
> If known version numbers are used as search terms, exploits for both the exact version and others whose version range covers the one specified are shown.
> More information: <https://www.exploit-db.com/searchsploit>.

- Search for an exploit, shellcode, or paper:

`searchsploit {{search_terms}}`

- Search for a known specific version, e.g. sudo version 1.8.27:

`searchsploit sudo 1.8.27`

- Show the exploit-db link to the found resources:

`searchsploit --www {{search_terms}}`

- Copy ([m]irror) the resource to the current directory (requires the number of the exploit):

`searchsploit --mirror {{exploit_number}}`

- E[x]amine the resource, using the pager defined in the `$PAGER` environment variable:

`searchsploit --examine {{exploit_number}}`

- [u]pdate the local Exploit Database:

`searchsploit --update`

- Search for the [c]ommon [v]ulnerabilities and [e]xposures (CVE) value:

`searchsploit --cve {{2021-44228}}`

- Check results in `nmap`'s XML output with service version (`nmap -sV -oX nmap-output.xml`) for known exploits:

`searchsploit --nmap {{path/to/nmap-output.xml}}`

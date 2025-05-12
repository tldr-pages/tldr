# searchsploit

> A command-line search tool for the Exploit Database to find exploits and shellcode offline.
> More information: <https://www.exploit-db.com/searchsploit>.

- Search for exploits matching multiple terms:

`searchsploit {{afd windows local}}`

- Search exploit titles only, excluding file paths:

`searchsploit {{[-t|--title]}} {{oracle windows}}`

- Search for exploits by CVE identifier:

`searchsploit --cve {{2021-44228}}`

- Perform an exact match on exploit title:

`searchsploit {{[-e|--exact]}} {{Apache Struts 2.0.0}}`

- Exclude unwanted results (e.g., Proof of Concept or Denial of Service):

`searchsploit {{linux kernel 3.2}} --exclude="{{(PoC)|/dos/}}"`

- Output search results in JSON format:

`searchsploit {{[-j|--json]}} {{linux reverse password}}`

- Copy an exploit to the current directory by EDB-ID:

`searchsploit {{[-m|--mirror]}} {{39446}}`

- Examine an exploit’s details by EDB-ID:

`searchsploit {{[-x|--examine]}} {{39446}}`

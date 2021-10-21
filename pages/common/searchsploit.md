# searchsploit

> Searchsploit searches exploit database's database for exploits, shellcodes and/or papers.
> If known version numbers are used as search terms, exploits for both the exact version and others whose version range covers the one specified are shown.
> More information: <https://www.exploit-db.com/searchsploit>.

- Search for an exploit, shellcode, or paper:

`searchsploit {{search_terms}}`

- Search for a known specific version, e.g. sudo version 1.8.27:

`searchsploit sudo 1.8.27`

- Show the exploit-db link to the found resources:

`searchsploit --www {{search_terms}}`

- Make a copy of the resource to the current directory (requires the number of the exploit):

`searchsploit --mirror {{exploit_number}}`

- Open the resource to read with the pager defined in the `$PAGER` environment variable:

`searchsploit --explore {{exploit_number}}`

- Update the local exploit database:

`searchsploit --update`

# searchsploit

> Searchsploit searches exploit database's database for exploits, shellcodes and/or papers
> If you insert known version numbers as search terms, searchsploit will show exploits for both the exact version and others whose version range covers the one specified
> More information: <https://www.exploit-db.com/searchsploit>.

- Search for an exploit/shellcode/paper:

`searchsploit Laravel`

- Search for a known specific version:

`searchsploit sudo 1.8.27`

- Show the exploit-db link to the found resources:

`searchsploit --www dirty cow`

- Makes a copy of the resource onto the current directory (requires the number of the exploit):

`searchsploit --mirror 49313`

- Explores the exploit with the pager defined in the `$PAGER` environmental variable:

`searchsploit --explore 13171`

- Updates the local exploit database:

`searchsploit --update`

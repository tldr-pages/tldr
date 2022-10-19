# dnsenum

> Multithreaded perl script used to enumerate DNS information from a domain.
> More information: <https://github.com/SparrowOchon/dnsenum2>.

- Enumerate a domain with default settings:

`dnsenum -enum {{domainname}`

- Enumerate domain without reverse lookup and save the output to file:

`dnsenum --noreverse -o {{outputfile}} {{domainname}}`

- Brute force search on subdomains along with custom file with subdomains passed as attribute:

`dnsenum -f {{filename}} -r {{domainname}}`

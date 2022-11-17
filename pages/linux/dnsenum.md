# dnsenum

> Multithreaded Perl script used to enumerate DNS information from a domain.
> More information: <https://github.com/SparrowOchon/dnsenum2>.

- Enumerate a domain with default settings:

`dnsenum -enum {{example.com}}`

- Enumerate a domain without reverse lookup and save the output to a file:

`dnsenum --noreverse -o {{path/to/file}} {{example.com}}`

- Brute force search on subdomains along with a custom file with subdomains passed as an attribute:

`dnsenum -f {{filename}} -r {{example.com}}`

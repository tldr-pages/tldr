# wfuzz

> A web application bruteforcer.
> More information: <https://wfuzz.readthedocs.io/en/latest/user/basicusage.html>.

- Directory and file bruteforce using the specified [w]ordlist and also [p]roxying the traffic:

`wfuzz -w {{path/to/file}} -p {{127.0.0.1:8080:HTTP}} {{http://example.com/FUZZ}}`

- Save the results to a [f]ile:

`wfuzz -w {{path/to/file}} -f {{filename}} {{http://example.com/FUZZ}}`

- Show [c]olorized output while only showing the declared response codes in the output:

`wfuzz -c -w {{path/to/file}} --sc {{200,301,302}} {{http://example.com/FUZZ}}`

- Use a custom [H]eader to fuzz subdomains while [h]iding specific response [c]odes and word counts. Increase the [t]hreads to 100 and include the target ip/domain:

`wfuzz -w {{path/to/file}} -H {{"Host: FUZZ.example.com"}} --hc {{301}} --hw {{222}} -t {{100}} {{example.com}}`

- Brute force Basic Authentication using a list of usernames and passwords from files for each FUZ[z] keyword, [h]iding response [c]odes of unsuccessful attempts:

`wfuzz -c --hc {{401}} -s {{delay_between_requests_in_seconds}} -z file,{{path/to/usernames}} -z file,{{path/to/passwords}} --basic 'FUZZ:FUZ2Z' {{https://example.com}}`

- Provide wordlist directly from the command line and use POST request for fuzzing:

`wfuzz -z list,{{word1-word2-...}} {{https://api.example.com}} -d {{"id=FUZZ&showwallet=true"}}`

- Provide wordlists from a file applying base64 and md5 encoding on them (`wfuzz -e encoders` lists all available encoders):

`wfuzz -z file,{{path/to/file}},none-base64-md5 {{https://example.com/FUZZ}}`

- List available encoders/payloads/iterators/printers/scripts:

`wfuzz -e {{encoders|payloads|iterators|printers|scripts}}`

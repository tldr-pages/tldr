# ffuf

> Subdomain and directory discovery tool.
> More information: <https://github.com/ffuf/ffuf>.

- Discover directories using a [w]ordlist on a target [u]rl with [c]olorized and [v]erbose output:

`ffuf -w {{path/to/wordlist}} -u {{https://target/FUZZ}} -c -v`

- Fuzz host-[H]eaders with a host file on a traget website and [m]atch HTTP 200 [c]ode responses:

`ffuf -w {{hosts.txt}} -u {{https://example.org}} -H "{{Host: FUZZ}}" -mc {{200}}`

- Discover directories using a [w]ordlist on a target website with a max individual job time of 60 seconds and recursion discovery depth of 2 levels:

`ffuf -w {{path/to/wordlist}} -u {{https://target/FUZZ}} -maxtime-job {{60}} -recursion -recursion-depth {{2}}`

- Fuzz GET parameter on a target website and [f]ilter out message [s]ize response of 4242 bytes:

`ffuf -w {{path/to/param_names.txt}} -u {{https://target/script.php?FUZZ=test_value}} -fs {{4242}}`

- Fuzz POST method with POST [d]ata of password on a target website and [f]ilter out HTTP response [c]ode 401:

`ffuf -w {{path/to/postdata.txt}} -X {{POST}} -d "{{username=admin\&password=FUZZ}}" -u {{https://target/login.php}} -fc {{401}}`

- Discover subdomains using a subdoomain list on a target website:

`ffuf -w {{subdomains.txt}} -u {{https://website.com}} -H "{{Host: FUZZ.website.com}}"`

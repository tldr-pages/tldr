# ffuf

> Subdomain and directory discovery tool.
> More information: <https://github.com/ffuf/ffuf>.

- Directory discovery using a wordlist on a target website colorized and verbose ouput:

`ffuf -w {{path/to/wordlist}} -u {{https://target/FUZZ}} -c -v`

- Host-header fuzzing with host file on a traget website and match HTTP 200 responses:

`ffuf -w {{hosts.txt}} -u {{https://example.org}} -H "{{Host: FUZZ}}" -mc {{200}}`

- Directory discovery using a wordlist on a target website with a max individual job time of 60 seconds and recusrion discovery depth of 2 levels:

`ffuf -w {{path/to/wordlist}} -u {{https://target/FUZZ}} -maxtime-job {{60}} -recursion -recursion-depth {{2}}`

- GET parameter fuzzing on a target website and filter out message size response of 4242 bytes:

`ffuf -w {{path/to/param_names.txt}} -u {{https://target/script.php?FUZZ=test_value}} -fs {{4242}}`

- Use POST method with POST data fuzzing of password on a target website and filter out HTTP response code 401:

`ffuf -w {{path/to/postdata.txt}} -X {{POST}} -d "{{username=admin\&password=FUZZ}}" -u {{https://target/login.php}} -fc {{401}}`

- Subdomain discovery using a subdoomain list on a target website:

`ffuf -w {{subdomains.txt}} -u {{http://website.com}} -H {{“Host: FUZZ.website.com”}}`

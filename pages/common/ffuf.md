# ffuf

> A fast web fuzzer written in Go.
> The `FUZZ` keyword is used as a placeholder. `ffuf` will try to hit the URL by replacing the word `FUZZ` with every word in the wordlist.
> More information: <https://github.com/ffuf/ffuf#usage>.

- Enumerate directories using [c]olored output and a [w]ordlist specifying a target [u]RL:

`ffuf -c -w {{path/to/wordlist.txt}} -u {{http://target/FUZZ}}`

- Enumerate webservers of subdomains by changing the position of the keyword:

`ffuf -w {{path/to/subdomains.txt}} -u {{http://FUZZ.target.com}}`

- Fuzz with specified [t]hreads (default: 40) and pro[x]ying the traffic and save [o]utput to a file:

`ffuf -o -w {{path/to/wordlist.txt}} -u {{http://target/FUZZ}} -t {{500}} -x {{http://127.0.0.1:8080}}`

- Fuzz a specific [H]eader ("Name: Value") and [m]atch HTTP status [c]odes:

`ffuf -w {{path/to/wordlist.txt}} -u {{http://target.com}} -H "{{Host: FUZZ}}" -mc {{200}}`

- Fuzz with specified HTTP method and [d]ata, while [f]iltering out comma separated status [c]odes:

`ffuf -w {{path/to/postdata.txt}} -X {{POST}} -d "{{username=admin\&password=FUZZ}}" -u {{http://target/login.php}} -fc {{401,403}}`

- Fuzz multiple positions with multiple wordlists using different modes:

`ffuf -w {{path/to/keys:KEY}} -w {{path/to/values:VALUE}} -mode {{pitchfork|clusterbomb}} -u {{http://target.com/id?KEY=VALUE}}`

- Proxy requests through a HTTP MITM pro[x]y (such as Burp Suite or `mitmproxy`):

`ffuf -w {{path/to/wordlist}} -x {{http://127.0.0.1:8080}} -u {{http://target.com/FUZZ}}`

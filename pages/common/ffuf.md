# ffuf

> A fast web fuzzer written in Go.
> More information: <https://github.com/ffuf/ffuf>.

- Discover hidden files and directories on a web server:

`ffuf -w {{path/to/wordlist}} -u {{http://example.com}}/FUZZ`

- Use a custom header for the fuzzing requests:

`ffuf -w {{path/to/wordlist}} -u {{http://example.com}}/FUZZ -H "{{'X-My-Header: 123'}}"`

- Save the output to a file:

`ffuf -w {{path/to/wordlist}} -u {{http://example.com}}/FUZZ -o {{path/to/output_file}}`
  
- Exclude specific HTTP response codes from the results:

`ffuf -w {{path/to/wordlist}} -u {{http://example.com}}/FUZZ -fc {{404}}`

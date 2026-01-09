# arjun

> Discover HTTP parameters for web applications.
> More information: <https://github.com/s0md3v/Arjun>.

- Scan a URL for GET parameters:

`arjun -u {{https://example.com/page.php}}`

- Scan using POST method:

`arjun -u {{https://example.com/api}} -m {{POST}}`

- Save discovered parameters to a file:

`arjun -u {{https://example.com}} -o {{output.txt}}`

- Use a custom wordlist:

`arjun -u {{https://example.com}} -w {{wordlist.txt}}`

- Increase request delay to avoid rate limiting:

`arjun -u {{https://example.com}} -d {{2}}`

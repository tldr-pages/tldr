# john

> Password cracker.
> More information: <https://www.openwall.com/john/>.

- Crack password hashes:

`john {{path/to/hashes.txt}}`

- Show passwords cracked:

`john --show {{path/to/hashes.txt}}`

- Display user's cracked password by user identifier from multiple files:

`john --show --users={{0}} {{path/to/hashes*}} {{path/to/other/hashes*}}`

- Crack password hashes, using a custom wordlist:

`john --wordlist={{path/to/wordlist.txt}} {{path/to/hashes.txt}}`

- Crack password hashes, using a specific hash format:

`john --format={{md5crypt|...}} {{path/to/hashes.txt}}`

- List available hash formats:

`john --list=formats`

- Crack password hashes, enabling word mangling rules:

`john --rules {{path/to/hashes.txt}}`

- Restore an interrupted cracking session:

`john --restore`

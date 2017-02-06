# cowsay

> Generate an ASCII character like a cow or sheep saying or thinking something.
> Available characters are stored in the /usr/share/cowsay on Linux.
> And /usr/local/share/cows/ on Mac.

- Print an ASCII cow saying "Hello world!":

`cowsay "Hello world!"`

- Print an ASCII dragon saying "Hello!":

`echo "Hello!" | cowsay -f dragon`

- Print a stoned thinking ASCII cow:

`cowthink -s "I'm just a cow, not a great thinker ..."`

- Print out a list of all characters with cowsay:

`ls -1 {{cowsay_character_directory}}  | rev | cut -c 5- | rev | xargs -I _ cowsay -f _ cowsay -f _`

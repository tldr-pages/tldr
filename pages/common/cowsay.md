# cowsay

> Print ASCII art (by default a cow) saying or thinking something.
> More information: <https://github.com/tnalpgge/rank-amateur-cowsay>.

- Print an ASCII cow saying "hello, world":

`cowsay "{{hello, world}}"`

- Print an ASCII cow saying text from `stdin`:

`echo "{{hello, world}}" | cowsay`

- List all available art types:

`cowsay -l`

- Print the specified ASCII art saying "hello, world":

`cowsay -f {{art}} "{{hello, world}}"`

- Print a dead thinking ASCII cow:

`cowthink -d "{{I'm just a cow, not a great thinker...}}"`

- Print an ASCII cow with custom eyes saying "hello, world":

`cowsay -e {{characters}} "{{hello, world}}"`

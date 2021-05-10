# cowsay

> Print an ASCII friend (by default a cow) saying or thinking something.
> More information: <https://github.com/tnalpgge/rank-amateur-cowsay>.

- Print an ASCII cow saying "Hello World":

`cowsay "Hello World"`

- Read text from stdin for the balloon:

`echo "Hello World" | cowsay`

- List all available friends:

`cowsay -l`

- Print an ASCII friend (different from default cow) saying "Hello World":

`cowsay -f {{friend}} "Hello World"`

- Print a stoned thinking ASCII cow:

`cowthink -s "I'm just a cow, not a great thinker..."`

- Print a ASCII cow with custom eyes:

`cowsay -e {{characters}} "Hello World"`

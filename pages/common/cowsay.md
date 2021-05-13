# cowsay

> Print an ASCII friend (by default a cow) saying or thinking something.
> More information: <https://github.com/tnalpgge/rank-amateur-cowsay>.

- Print an ASCII cow saying "Hello World":

`cowsay "{{Hello World}}"`

- Print an ASCII cow saying text from stdin:

`echo "{{Hello World}}" | cowsay`

- List all available friends:

`cowsay -l`

- Print a custom ASCII friend saying "Hello World":

`cowsay -f {{friend}} "{{Hello World}}"`

- Print a dead thinking ASCII cow:

`cowthink -d "{{I'm just a cow, not a great thinker...}}"`

- Print an ASCII cow with custom eyes saying "Hello World":

`cowsay -e {{characters}} "{{Hello World}}"`

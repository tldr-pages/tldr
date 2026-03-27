# resend

> Email for developers - send and manage emails from the command-line.
> More information: <https://github.com/resend/resend-cli#commands>.

- Log in to Resend (opens browser for authentication):

`resend login`

- Log in with an API key directly (for CI/agents):

`resend login --key {{re_xxxxxxxxx}}`

- Send an email:

`resend emails send --from {{email@example.com}} --to {{recipient@example.com}} --subject "{{subject}}" --text "{{message}}"`

- Create a template:

`resend templates create --name "{{Welcome}}" --subject "{{subject}}" --html "{{<h1>Hello</h1>}}"`

- Send an email using a template:

`resend emails send --to {{recipient@example.com}} --template {{template_id}}`

- List verified domains:

`resend domains list`

- Show current authentication status:

`resend whoami`

- Check CLI version, API key, and domain status:

`resend doctor`

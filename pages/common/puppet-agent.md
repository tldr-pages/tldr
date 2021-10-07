# puppet agent

> Retrieves the client configuration from the Puppet server and applies it to the local host.
> More information: <https://puppet.com/docs/puppet/7/man/agent.html>.

- Register a node at a puppetserver and apply the received catalog:

`puppet agent --test --server {{puppetserver_fqdn}} --serverport {{port}} --waitforcert {{poll_time}}`

- Run the agent in the background (uses settings from `/opt/puppetlabs/puppet/puppet.conf`):

`puppet agent`

- Run the agent once in foreground, then exit:

`puppet agent --test`

- Run the agent in dry-mode:

`puppet agent --test --noop`

- Log every resource being evaluated (even if nothing is changed):

`puppet agent --test --evaltrace`

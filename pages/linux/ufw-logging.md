# ufw logging

> Configure logging of firewall events.
> Note: Logging levels `high` and `full` may quickly fill up disk space.
> More information: <https://manned.org/ufw>.

- Enable logging with the default level (low):

`sudo ufw logging on`

- Disable logging:

`sudo ufw logging off`

- Set the logging level:

`sudo ufw logging {{low|medium|high|full}}`

- Log new connections (`log`) or all packets (`log-all`) matching a rule:

`sudo ufw {{allow|deny|reject|limit}} {{log|log-all}} {{22/tcp}}`

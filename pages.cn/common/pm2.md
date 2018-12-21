# pm2

> Process manager for Node.js.
> Used for log management, monitoring and configuring processes.

- Start a process with a name that can be used for later operations:

`pm2 start {{app.js}} --name {{myapp}}`

- List processes:

`pm2 list`

- Monitor all processes:

`pm2 monit`

- Stop a process:

`pm2 stop {{myapp}}`

- Restart a process:

`pm2 restart {{myapp}}`

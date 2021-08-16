# git instaweb

> Helper to launch a GitWeb server.
> More information: <https://git-scm.com/docs/git-instaweb>.

- Launch a GitWeb server for the current Git repository:

`git instaweb --start`

- Listen only on localhost:

`git instaweb --start --local`

- Listen on a specific port:

`git instaweb --start --port {{1234}}`

- Use a specified HTTP daemon:

`git instaweb --start --httpd {{lighttpd|apache2|mongoose|plackup|webrick}}`

- Also auto-launch a web browser:

`git instaweb --start --browser`

- Stop the currently running GitWeb server:

`git instaweb --stop`

- Restart the currently running GitWeb server:

`git instaweb --restart`

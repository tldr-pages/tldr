# valet

> A Laravel development environment that allows hosting sites via local tunnels on `http://<example>.test`.
> More information: <https://laravel.com/docs/valet>.

- Start the valet daemon:

`valet start`

- Register the current working directory as a path that Valet should search for sites:

`valet park`

- View 'parked' paths:

`valet paths`

- Serve a single site instead of an entire directory:

`valet link {{application_name}}`

- Share a project via an Ngrok tunnel:

`valet share`

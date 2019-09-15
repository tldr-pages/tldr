# valet

> A minimalist Laravel development environment that allows hosting sites via local tunnels on http://<project>.test
> More information: <https://laravel.com/docs/5.8/valet>.

- Start the valet daemon:

`valet start`

- Register your current working directory as a path that Valet should search for sites:

`valet park`

- View your 'parked' paths:

`valet paths`

- Serve a single site instead of an entire directory:

`valet link app-name`

- Share a project via Ngrok tunnel:

`valet share`

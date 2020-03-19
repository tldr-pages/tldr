# http_load

> A HTTP benchmarking tool.
> Runs multiple HTTP fetches in parallel to test the throughput of a web server.
> More information: <http://www.acme.com/software/http_load/>.

- Emulate 20 requests based on a given URL list file per second for 60 seconds:

`http_load -rate {{20}} -seconds {{60}} {{path/to/urls.txt}}`

- Emulate 5 concurrent requests based on a given URL list file for 60 seconds:

`http_load -parallel {{5}} -seconds {{60}} {{path/to/urls.txt}}`

- Emulate 1000 requests at 20 requests per second, based on a given URL list file:

`http_load -rate {{20}} -fetches {{1000}} {{path/to/urls.txt}}`

- Emulate 1000 requests at 5 concurrent requests at a time, based on a given URL list file:

`http_load -parallel {{5}} -fetches {{1000}} {{path/to/urls.txt}}`

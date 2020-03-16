# http_load

> A useful HTTP benchmarking tool.
> That lets you run multiple HTTP fetches in parallel to test the throughput of a web server.
> More information: <http://www.acme.com/software/http_load/>.

- Emulate 20 requests based on a given url list file per second for 60 seconds :

`http_load -rate {{20}} -seconds {{60}} {{urls.txt}}`

- Emulate 5 concurrent requests based on a given url list file for 60 seconds:

`http_load -parallel {{5}} -seconds {{60}} {{urls.txt}}`

- Emulate 20 requests based on a given url list file per second until 1000 requests:

`http_load -rate {{20}} -fetches {{1000}} {{urls.txt}}`

- Emulate 5 concurrent requests based on a given url list file until 1000 requests:

`http_load -parallel {{5}} -fetches {{1000}} {{urls.txt}}`

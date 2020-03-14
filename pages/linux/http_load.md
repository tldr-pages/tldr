# http_load

> A useful HTTP benchmarking tool.
> That lets you run multiple http fetches in parallel to test the throughput of web server.
> More information: <http://www.acme.com/software/http_load/>.

- Emulate 20 HTTP GET requests per second for 60 seconds(urls.txt is a text file that contains one url per line):

`http_load -rate {{20}} -seconds {{60}} {{urls.txt}}`

- Emulate 5 concurrent requests for 60 seconds:

`http_load -parallel {{5}} -seconds {{60}} {{urls.txt}}`

- Emulate 20 requests per second until 1000 requests:

`http_load -rate {{20}} -fetches {{1000}} {{urls.txt}}`

- Emulate 5 concurrent requests until 1000 requests:

`http_load -parallel {{5}} -fetches {{1000}} {{urls.txt}}`

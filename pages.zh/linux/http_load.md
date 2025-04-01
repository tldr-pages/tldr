# http_load

> 一个HTTP基准测试工具。
> 通过并行运行多个HTTP请求来测试Web服务器的吞吐量。
> 更多信息：<https://www.acme.com/software/http_load/>.

- 每秒模拟20个请求，基于给定的URL列表文件，持续60秒：

`http_load -rate {{20}} -seconds {{60}} {{path/to/urls.txt}}`

- 模拟5个并发请求，基于给定的URL列表文件，持续60秒：

`http_load -parallel {{5}} -seconds {{60}} {{path/to/urls.txt}}`

- 基于给定的URL列表文件，以每秒20个请求的速度模拟1000个请求：

`http_load -rate {{20}} -fetches {{1000}} {{path/to/urls.txt}}`

- 基于给定的URL列表文件，每次都以5个并发请求的方式模拟1000个请求：

`http_load -parallel {{5}} -fetches {{1000}} {{path/to/urls.txt}}`

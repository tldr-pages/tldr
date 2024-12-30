# http_load

> 一款HTTP基准测试工具。
> 通过并行运行多个HTTP请求来测试Web服务器的吞吐量。
> 更多信息请访问：<https://www.acme.com/software/http_load/>.

- 每秒基于给定的URL列表文件模拟20个请求，持续60秒：

`http_load -rate {{20}} -seconds {{60}} {{path/to/urls.txt}}`

- 每秒基于给定的URL列表文件模拟5个并发请求，持续60秒：

`http_load -parallel {{5}} -seconds {{60}} {{path/to/urls.txt}}`

- 基于给定的URL列表文件以每秒20个请求模拟1000个请求：

`http_load -rate {{20}} -fetches {{1000}} {{path/to/urls.txt}}`

- 基于给定的URL列表文件以5个并发请求模拟1000个请求：

`http_load -parallel {{5}} -fetches {{1000}} {{path/to/urls.txt}}`
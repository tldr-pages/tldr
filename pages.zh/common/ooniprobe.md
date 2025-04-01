# ooniprobe

> 开放网络干扰观测站 (OONI)。
> 测试网站和应用的阻断情况。测量您的网络速度和性能。
> 更多信息：<https://ooni.org/support/ooni-probe-cli/>。

- 列出所有已执行的测试：

`ooniprobe list`

- 显示特定测试的信息：

`ooniprobe list {{7}}`

- 运行所有可用的测试：

`ooniprobe run all`

- 执行特定的测试：

`ooniprobe run {{performance}}`

- 检查特定网站的可用性：

`ooniprobe run websites --input {{https://ooni.org/}}`

- 检查文件中列出的所有网站的可用性：

`ooniprobe run websites --input-file {{path/to/my-websites.txt}}`

- 以 JSON 格式显示测试的详细信息：

`ooniprobe show {{9}}`

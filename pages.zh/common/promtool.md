# promtool

> Prometheus 监控系统的工具。
> 更多信息：<https://prometheus.io/docs/prometheus/latest/getting_started/>.

- 检查配置文件是否有效（如果存在错误则报告）：

`promtool check config {{config_file.yml}}`

- 检查规则文件是否有效（如果存在错误则报告）：

`promtool check rules {{rules_file.yml}}`

- 通过 `stdin` 传递 Prometheus 指标以检查其一致性和正确性：

`curl --silent {{http://example.com:9090/metrics/}} | promtool check metrics`

- 规则配置的单元测试：

`promtool test rules {{test_file.yml}}`

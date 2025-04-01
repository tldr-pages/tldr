# nuclei

> 基于简单 YAML 语法的快速可定制漏洞扫描器。
> 更多信息：<https://docs.projectdiscovery.io/tools/nuclei/overview>.

- 更新 `nuclei` 模板到最新发布版本（将下载到 `~/nuclei-templates`）：

`nuclei -ut`

- 列出具有特定协议类型的模板：

`nuclei -tl -pt {{dns|file|http|headless|tcp|workflow|ssl|websocket|whois|code|javascript}}`

- 使用 wappalyzer 技术检测对指定的目标 URL/主机进行自动 Web 扫描：

`nuclei -as -u {{scanme.nmap.org}}`

- 使用高和关键严重性的 HTTP 协议类型模板进行扫描，并将结果导出到特定目录中的 Markdown 文件：

`nuclei -severity high,critical -pt http -u {{http://scanme.sh}} -me {{markdown_directory}}`

- 使用不同的速率限制和最大批量大小运行所有模板，并仅显示发现的结果：

`nuclei -rl {{150}} -bs {{25}} -c {{25}} -silent -u {{http://scanme.sh}}`

- 对 WordPress 站点运行 WordPress 工作流：

`nuclei -w {{path/to/nuclei-templates/workflows/wordpress-workflow.yaml}} -u {{https://sample.wordpress.site}}`

- 运行一个或多个特定模板或模板目录，并在 `stderr` 中以详细输出模式运行，将检测到的问题/漏洞输出到文件：

`nuclei -t {{path/to/nuclei-templates/http}} -u {{http://scanme.sh}} -v -o {{results}}`

- 根据一个或多个模板条件运行扫描：

`nuclei -tc "{{contains(tags, 'xss') && contains(tags, 'cve')}}" -u {{https://vulnerable.website}}`

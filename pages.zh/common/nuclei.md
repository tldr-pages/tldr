# nuclei

> 基于简单 YAML 语言的快速可定制漏洞扫描器。
> 更多信息：<https://docs.projectdiscovery.io/tools/nuclei/overview>。

- [u]pdate `nuclei` [t]emplates 到最新发布版本（将下载到 `~/nuclei-templates`）：

`nuclei -ut`

- 列出所有具有特定 [p]rotocol [t]ype 的 [t]emplates：

`nuclei -tl -pt {{dns|file|http|headless|tcp|workflow|ssl|websocket|whois|code|javascript}}`

- 使用 wappalyzer 技术检测运行自动网页 [s]can，指定要扫描的目标 [u]RL/主机：

`nuclei -as -u {{scanme.nmap.org}}`

- 运行高和关键严重性 HTTP [p]rotocol [t]ype 模板，将结果导出到特定目录中的 [m]arkdown 文件：

`nuclei -severity high,critical -pt http -u {{http://scanme.sh}} -me {{markdown_directory}}`

- 使用不同的 [r]ate [l]imit 和最大 [b]ulk [s]ize 运行所有模板，并静默输出（仅显示发现）：

`nuclei -rl {{150}} -bs {{25}} -c {{25}} -silent -u {{http://scanme.sh}}`

- 针对 WordPress 网站运行 WordPress [w]orkflow：

`nuclei -w {{path/to/nuclei-templates/workflows/wordpress-workflow.yaml}} -u {{https://sample.wordpress.site}}`

- 运行一个或多个特定的 [t]emplates 或包含 [t]emplates 的目录，以冗长的输出形式在 `stderr` 中，并将检测到的问题/漏洞输出到文件中：

`nuclei -t {{path/to/nuclei-templates/http}} -u {{http://scanme.sh}} -v -o {{results}}`

- 根据一个或多个 [t]emplate [c]onditions 运行扫描：

`nuclei -tc "{{contains(tags, 'xss') && contains(tags, 'cve')}}" -u {{https://vulnerable.website}}`
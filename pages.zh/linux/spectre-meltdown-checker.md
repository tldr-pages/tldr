# spectre-meltdown-checker

> Spectre 和 Meltdown 缓解检测工具。
> 更多信息：<https://manned.org/spectre-meltdown-checker>。

- 检查当前运行的内核是否存在 Spectre 或 Meltdown：

`sudo spectre-meltdown-checker`

- 检查当前运行的内核并显示缓解漏洞所需采取的措施的解释：

`sudo spectre-meltdown-checker --explain`

- 检查特定变体（默认为全部）：

`sudo spectre-meltdown-checker --variant {{1|2|3|3a|4|l1tf|msbds|mfbds|mlpds|mdsum|taa|mcespc|srbds}}`

- 使用特定输出格式显示输出：

`sudo spectre-meltdown-checker --batch {{text|json|nrpe|prometheus|short}}`

- 即使存在也不使用 `/sys` 接口：

`sudo spectre-meltdown-checker --no-sysfs`

- 检查一个未运行的内核：

`sudo spectre-meltdown-checker --kernel {{path/to/kernel_file}}`
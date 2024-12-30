# searchsploit

> 在漏洞数据库中搜索漏洞、Shellcode 和/或论文。
> 如果使用已知的版本号作为搜索词，则会显示该特定版本和其他版本范围涵盖指定版本的漏洞。
> 更多信息：<https://www.exploit-db.com/searchsploit>。

- 搜索漏洞、Shellcode 或论文：

`searchsploit {{search_terms}}`

- 搜索已知的特定版本，例如 sudo 版本 1.8.27：

`searchsploit sudo 1.8.27`

- 显示找到资源的 exploit-db 链接：

`searchsploit --www {{search_terms}}`

- 将资源复制（[m]irror）到当前目录（需要漏洞的编号）：

`searchsploit --mirror {{exploit_number}}`

- [E]xamine 资源，使用在 `$PAGER` 环境变量中定义的分页器：

`searchsploit --examine {{exploit_number}}`

- [u]pdate 本地漏洞数据库：

`searchsploit --update`

- 搜索 [c]ommon [v]ulnerabilities 和 [e]xposures (CVE) 值：

`searchsploit --cve {{2021-44228}}`

- 检查 `nmap` 的 XML 输出中的结果，使用服务版本（`nmap -sV -oX nmap-output.xml`）查找已知漏洞：

`searchsploit --nmap {{path/to/nmap-output.xml}}`
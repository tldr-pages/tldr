# searchsploit

> 在 Exploit Database 中搜索漏洞利用程序、Shellcode 或论文。
> 如果使用已知版本号作为搜索词，将显示针对确切版本以及其他版本范围涵盖指定版本的漏洞利用。
> 更多信息：<https://www.exploit-db.com/searchsploit>。

- 搜索漏洞利用、Shellcode 或论文：

`searchsploit {{search_terms}}`

- 搜索特定已知版本，例如 sudo 版本 1.8.27：

`searchsploit sudo 1.8.27`

- 显示找到资源的 exploit-db 链接：

`searchsploit {{[-w|--www]}} {{search_terms}}`

- 将资源复制到当前目录（需要提供漏洞利用的编号）：

`searchsploit {{[-m|--mirror]}} {{exploit_number}}`

- 使用 `$PAGER` 环境变量中定义的分页器查看资源：

`searchsploit {{[-x|--examine]}} {{exploit_number}}`

- 更新本地 Exploit Database：

`searchsploit {{[-u|--update]}}`

- 搜索 [c]ommon [v]ulnerabilities and [e]xposures (CVE) 值：

`searchsploit --cve {{2021-44228}}`

- 使用 `nmap` 的 XML 输出（包含服务版本信息 `nmap -sV -oX nmap-output.xml`）检查已知漏洞：

`searchsploit --nmap {{path/to/nmap-output.xml}}`
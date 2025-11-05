在PowerShell中，当原始wget程序（https://www.gnu.org/software/wget）未正确安装时，此命令可能是Invoke-WebRequest的别名。注意：如果version命令返回错误，PowerShell可能已经用Invoke-WebRequest命令替换了这个命令。更多信息：https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest。

查看原始wget命令的文档：
tldr wget {{[-p|--platform]}} common

查看PowerShell的Invoke-WebRequest命令的文档：
tldr invoke-webrequest

显示版本:
wget --version

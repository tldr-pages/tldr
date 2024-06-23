# 格式指导

当你在为 `tldr` 贡献时，请遵守下面的格式规范。

请注意，下面的规范仅适用于中文翻译的 `tldr` 页面。

## 排版

首先，你的页面应该看起来像这样，并且最多只能包含 8 个示例：

```md
# 命令名称

> 简短、精炼的描述。
> 描述最好只有一行；当然，如果需要，也可以是两行。
> 更多信息：<https://example.com>.

- 命令描述：

`命令 -选项 1 -选项 2 -参数 1 {{参数的值}}`

- 命令描述：

`命令 -选项 1 -选项 2`
```

当你将自己的贡献提交 pull request 时，一个脚本会自动检查你的贡献是否符合上面的格式。

你也可以在提交前在本地测试自己的贡献：

```sh
npm install --global tldr-lint
tldr-lint {{page.md}}
```

关于 `tldr-lint` 的更多使用方法，例如检查批量检查一整个目录的格式，[`tldr tldr-lint`](https://github.com/tldr-pages/tldr/blob/master/pages/common/tldr-lint.md) 是你的不二去处！

如果你用 tldr-pages 的 Node.js 客户端，你可以在命令后加 `-f` (`--render`) 来在本地预览自己的页面：

```sh
tldr --render path/to/tldr_page.md
```

### PowerShell 特定规则
在记录 PowerShell 命令时，请注意以下命名约定。

- 文件名必须以小写形式书写，例如 `invoke-webrequest.md` 而不是 `Invoke-WebRequest.md`。
- 页面标题/标题必须按照原样书写（与 Microsoft 或 PowerShell 模块作者意图一致），例如 `Invoke-WebRequest` 而不是 `invoke-webrequest`。
- 示例中的命令名称和选项也应按原样书写，例如 `Command-Name {{input}} -CommandParameter {{value}}` 而不是 `command-name {{input}} -commandparameter {{value}}`。

由于[各种兼容性差异](https://learn.microsoft.com/powershell/scripting/whats-new/differences-from-windows-powershell)和在 PowerShell 6.x 中删除的特定于 Windows 的命令，确保命令在 PowerShell 5.1（即安装在 Windows 10 和 11 中的“传统 Windows PowerShell”）和 最新版本的跨平台 PowerShell（以前称为 PowerShell Core）之间可用。如果命令或其选项在每个版本之间不可用或包含不同的行为，请在描述中注明。例如，

```md
# Clear-RecycleBin

> 清空回收站中的项目。
> 此命令仅适用于 PowerShell 版本 5.1 及以下版本，或 7.1 及以上版本。
> 更多信息： <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/clear-recyclebin>.
```

## 别名
如果一个命令可以通过其他名称调用（例如 `vim` 可以通过 `vi` 调用），可以创建别名页面将用户引导到原始命令名称。

```md
# command_name

> 此命令是 `original-command-name` 的别名。
> 更多信息： <https://example.com/original/command/help/page>.

- 查看原始命令的文档：

`tldr original_command_name`
```

示例：

```md
# vi

> 这是 `vim` 命令的一个别名。

- 原命令的文档在：

`tldr vim`
```

预先翻译好的别名模板见[这里](https://github.com/tldr-pages/tldr/blob/main/contributing-guides/translation-templates/alias-pages.md)。

### PowerShell 特定别名
某些 PowerShell 命令可能会引入别名，这些别名可以分为以下三类：

1. 替代现有的 Windows 命令提示符 (`cmd`) 命令，例如 `cd` 别名为 `Set-Location`，但带有不同的命令选项。在这种情况下，将以下别名注释添加到原始命令提示符命令的 tldr 描述的第二行中，例如：

```md
# cd

> 显示当前工作目录或移动到其他目录。
> 在 PowerShell 中，此命令是 `Set-Location` 的别名。本文档基于命令提示符 (`cmd`) 版本的 `cd`。
> 更多信息： <https://learn.microsoft.com/windows-server/administration/windows-commands/cd>.

- 原命令的文档在：

`tldr set-location`
```

> [!TIP]
> “查看等效 PowerShell 命令的文档”的示例是可选的，如果页面已经具有 8 条示例，则可以省略。

2. 提供一个新的别名，但只能在 PowerShell 中执行，例如 `ni` 代表 `New-Item`。在这种情况下，使用[标准别名模板](https://github.com/tldr-pages/tldr/blob/main/contributing-guides/translation-templates/alias-pages.md)，但添加说明“在 PowerShell 中”，或表示该命令仅限于 PowerShell。例如，

```md
# ni

> 在 PowerShell 中，此命令是 `New-Item` 的别名。
> 更多信息： <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/new-item>.

- 查看原始命令的文档：

`tldr new-item`
```

3. 与其他程序冲突时 PowerShell 会提供一个新的别名，最为突出的是将 `curl` 和 `wget` 作为 `Invoke-WebRequest` 的别名（带有不兼容的命令选项集）。请注意，此类别的 PowerShell 系统别名通常仅限于 Windows。

在这种情况下，提供一个说明，并提供一种方法来确定命令当前是否引用了 PowerShell 命令（通过别名）或其他程序。例如，

```md
# curl

> 在 PowerShell 中，当原始的 `curl` 程序 (<https://curl.se>) 未正确安装时，此命令可能是 `Invoke-WebRequest` 的别名。
> 更多信息： <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- 通过打印其版本号来检查 `curl` 是否已正确安装。如果此命令导致错误，则 PowerShell 可能已将此命令替换为 `Invoke-WebRequest`：

`curl --version`

- 查看原始 `curl` 命令的文档：

`tldr curl -p common`

- 查看 PowerShell 的 `Invoke-WebRequest` 命令的文档：

`tldr invoke-webrequest`
```

## 选项语法

- 对于常用命令（例如 `grep`、`tar` 等），我们更推荐在占位符中使用简短选项以及[助记符](#short-option-mnemonics)。
- 对于在命令中同时突出长选项和短选项（而不是使用助记符），将它们组合在占位符中，即 `{{-o|--output}}`。
- 为了用户友好，在 `common` 目录下的页面中，当它们在跨平台（在多个平台上都可以正常工作）时，我们更推荐使用**GNU 风格的长选项**（例如 `--help` 而不是 `-h`)。
- 在记录 PowerShell 命令时，使用**PowerShell 风格的长选项**（例如 `-Help` 而不是 `-H`）。
- 我们更推荐使用空格而不是等号 (`=`) 来分隔选项和其参数（即使用 `--opt arg` 而不是 `--opt=arg`），除非程序不支持此方法。

### 短选项助记符

短选项助记符是可选的提示，可以添加以帮助用户理解这些短选项的含义。分配的助记符应与命令的官方文档（例如来自 `man` 或 `Get-Help`）中的内容相匹配。例如：

```md
- [d]isplay the ins[t]allation [i]D for the current device. Useful for offline license activation:

`slmgr.vbs /dti`

Display the current license's e[xp]i[r]ation date and time:

`slmgr.vbs /xpr`
```

请注意，在第一个示例中，`[d]`、`[t]` 和 `[i]` 字符被方括号括起来，以指示命令的 `/dti` 选项分别是 "display"、"installation" 和 "ID" 的组合。连续的助记符字符可以在同一方括号下进行分组，例如 `e[xp]i[r]ation` 而不是 `e[x][p]i[r]ation`。

**助记符字符必须以区分大小写的方式编写**，即使它放在句子的第一个字符位置（例如使用 `[d]isplay` 而不是 `[D]isplay`）。这是为了避免与 GNU 风格命令选项产生冲突，GNU 风格命令选项可能会以不同于小写的方式解释大写选项，例如 `-v` 用于显示命令的 `[v]ersion` 号码，而 `-V` 则用于以 `[V]erbose` 模式运行命令。

选项助记符也可以在翻译中使用，只要突出显示的单词与命令所用语言（通常为英语）中的单词具有相似的含义即可。例如，英语中的 `[d]ownload` 可以翻译为西班牙语中的 `[d]escargar`，英语中的 `[i]nstall` 可以翻译为德语中的 `[i]nstallieren`，而英语中的 `[a]pp` 可以翻译为印尼语和马来语中的 `[a]plikasi`。

可选地，在翻译和特定页面中，助记符及其包含的术语可以用括号与描述的其余部分分开（即 `([a]ll)`），以提供额外的上下文或提及描述中不存在的单词。

> [!NOTE]
> 在翻译的单词中如果缺少字符，您可以在等效词的前面或旁边突出显示选项，或您可以在括号内的翻译旁边添加英文单词。例如，英语中的 `E[x]tract` 可以翻译为印尼语中的 `[x] ekstrak` 或 `ekstrak [x]` 或 `ekstrak (E[x]tract)`。

## 占位符语法

当命令涉及用户自己提供的值时，请用 `{{token}}` 语法来使 `tldr` 客户端能自动高亮它们：

`tar -cf {{目标.tar}} {{文件 1}} {{文件 2}} {{文件 3}}`

翻译时，请尽量翻译原文中的西文占位符。下面是命名占位符的规则：

1. 占位符需要短小精悍，
   例如 `{{源文件}}` 或者 `{{钱包.txt}}`
2. 如果占位符是西文，请用 [`snake_case`](https://en.wikipedia.org/wiki/Snake_case) 来分词。
3. 当占位符涉及文件路径时，请用 `{{目录/子目录/《占位符》}}` 的格式。
   例如：`ln -s {{目录/子目录/源文件}} {{目录/子目录/链接}}`
   如果占位符提到的文件也可能是目录，请用 `{{目录/子目录/文件或目录}}`
4. 除非文件是特定的，上述 `{{目录/子目录/《占位符》}}` 的文件路径格式应用于所有包含路径的命令。
5. 如果命令需要的文件扩展名是固定的，请在占位符里加上文件格式。
   例如：`unrar x {{压缩包.rar}}`
   如果文件 **必须** 有一个扩展名，请用 `{{.ext}}` 。
   例如，在 `find {{起始目录}} -name '{{*.ext}}'` 的例子里，
   这样做简单地演示了查找一个特定文件扩展名的方法。
   但是，在 `wc -l {{file}}` 的例子里，用不加扩展名的 `{{file}}` 就足够了。
6. 如果用实际的值比描述这个占位符更加明了，请举一个值做例子。
   例如：`iostat {{2}}` 比 `iostat {{以秒为单位的间隔}}` 更清晰。
7. 如果一个命令可能对文件系统或设备造成不可逆的影响，请在示例命令中注意改写，使其不能被盲目复制粘贴运行。
   例如，`ddrescue --force --no-scrape /dev/sda /dev/sdb` 被盲目复制粘贴时可能对系统造成毁灭性的打击；`ddrescue --force --no-scrape {{/dev/sdX}} {{/dev/sdY}}` 则更安全。
   因此，请用 `{{/dev/sdXY}}` 而不是 `{{/dev/sda1}}` 来表示一个 **块设备** 。

占位符应该尽可能简单明了，让人一眼就能看出应该替换它的值。

### 路径

- 当只期望文件名时，请使用 `{{filename}}`。
- 对于文件或目录路径的任何引用，请使用格式 `{{path/to/<placeholder>}}`，除非位置是隐含的。
- 当路径不能是相对路径，而必须从文件系统的根目录开始时，请使用斜杠作为前缀，例如 `get {{/path/to/remote_file}}`。
- 如果可能引用文件或目录，请使用 `{{path/to/file_or_directory}}`。

> [!NOTE]
> 如果命令专用于 Windows，请使用反斜杠（`\`），例如 `{{path\to\file_or_directory}}`。驱动器号（如 `C:`）是可选的，除非命令输入要求绝对路径或特定的驱动器号范围，例如 `cd /d {{C}}:{{path\to\directory}}`。

### 扩展名

- 如果文件有特定的扩展名，请写出来。
  例如，`unrar x {{path/to/compressed.rar}}`。
- 如果需要通用的扩展名，请使用 `{{.ext}}`，但**只有**在需要扩展名时才使用。
  例如，在 `find.md` 的示例“按扩展名查找文件”中（`find {{path/to/root}} -name '{{*.ext}}'`），
  使用 `{{*.ext}}` 可以解释命令而不必过于具体；
  而在 `wc -l {{path/to/file}}` 中，使用 `{{path/to/file}}`（不带扩展名）就足够了。

### 分组占位符

- 如果命令可以接受相同类型的 0 个或多个参数，请使用省略号：`{{placeholder1 placeholder2 ...}}`。
  例如，期望多个路径，则可以使用 `{{path/to/directory1 path/to/directory2 ...}}`。
- 如果命令可以接受不同类型的 0 个或多个参数，请使用竖线和省略号：`{{placeholder1|placeholder2|...}}`。
  如果可能值超过 5 个，则可以在最后一项后面使用 `|...`。
- 无法通过省略号限制占位符的最小或最大数量。

### 特殊情况

- 如果一个命令可能对文件系统或设备进行不可逆转的更改，
  请以一种不会被轻易复制粘贴的方式编写每个示例。
  例如，不要写成 `ddrescue --force --no-scrape /dev/sda /dev/sdb`，
  而是写成 `ddrescue --force --no-scrape {{/dev/sdX}} {{/dev/sdY}}`，
  并且对于*块设备*，使用 `{{/dev/sdXY}}` 占位符，而不是 `/dev/sda1`。

通常情况下，占位符应尽可能直观，以便于理解如何使用命令并填入相应的值。

在命令描述中，如果出现了技术性的专有名词，请用 `反引号` 括起来：

- 路径，例如 `package.json`，`/etc/package.json`。
- 扩展名，例如 `.dll`。
- 命令，例如 `ls`。
- 标准流：`stdout`，`stdin`，`stderr`。**不要**使用完整的名称（例如标准输出）。
- 压缩算法，例如 `zip`，`7z`，`xz`。

## 描述

### 祈使句

- **所有描述必须以祈使句表达。**

如果你担心命令在不同平台或操作系统之间可能不同（例如 Windows 对比 macOS），大多数 [tldr 页面客户端](https://github.com/tldr-pages/tldr/wiki/tldr-pages-clients) 将选择最适合的命令版本。

在这种情况下，默认将显示 Windows 版本的 `cd` 信息（存储在 `pages/windows/cd.md` 中）给 Windows 用户，并为 Linux、macOS 和其他平台显示一个通用版本（存储在 `pages/common/cd.md` 中）。

在为命令示例编写描述时，**检查任何语法错误**。例如，应该使用 `前往指定目录` 而不是：

- `正前往指定目录`（不应使用现在分词形式）
- `该命令将前往指定目录`（很明显此示例适用于 *此* 命令）
- `让我们前往指定目录！`
- `目录被更改为`（如果可能，应使用主动形式而不是被动形式）

例如，可以使用 `列出所有文件：` 的描述，下面是示例的描述可以使用 `列出所有文件：`。

```md
- 列出所有文件：

`ls`
```

### 措辞

- 所有描述**必须简洁**。
- 避免在描述中使用页面标题（例如，使用 `为数字艺术家设计的素描和绘画程序`，而不是 `Krita 是为数字艺术家设计的素描和绘画程序`），除非程序名称与可执行文件名称不同（例如 `rg` 和 Ripgrep）。
- 避免提及程序是在命令行上使用的（例如，使用 `Ripgrep 是一个递归的面向行的搜索工具`，而不是 `Ripgrep 是一个递归的面向行的 CLI 搜索工具`）。
- 例如，在为 `cd` 编写文档时，一个用于在终端或命令提示符中更改当前工作目录的工具，**不要**写出像这样冗长的描述：

```md
> `cd` 是一个系统工具，在 Windows、macOS 和 Linux 中可用，用于在命令提示符、终端和 PowerShell 中更改当前工作目录以完成任务。
```

它应该简化以使每个人都能更轻松地阅读：

```md
> 更改当前工作目录。
```

### 格式

- 在描述中，应该对专有名词进行大写（例如，使用 `用于与 Git 仓库交互的工具。`，而不是 ``用于与 `git` 仓库交互的工具。``）。
- 首字母缩写（即协议、工具等）在没有本地同类物时不应进行翻译。
- 当编写包含键盘按键或键盘快捷键时，建议将它们用反引号括起来，以突出显示在描述中（即 ``打印给定文件的最后几行，并一直读取直到按下 `Ctrl + C`：``）。 或者，您可以将它们记录为单独的命令，然后选择性地将它们突出显示为占位符（即 `:wq{{Enter}}` 或 `:wq<Enter>` 或 `:wq(Enter)`）。

## 斜体和粗体

请不要在页面上使用 *斜体*、**粗体** 或任何其他文本样式。这些样式被用于客户端对占位符的修饰。

## 更多信息链接

- 在`更多信息`链接行上，我们更推荐链接到作者提供的命令行参考文档或 man 手册。如果没有提供，请使用 <https://manned.org> 作为所有系统（除 `osx` 和除了 FreeBSD 之外的 BSD 平台）的默认链接。或者，如果命令没有文档页面，您也可以链接到作者的网站或教程页面。

- 对于 `osx`：苹果在 Xcode 中分发内置的 man 手册 [在这里](https://developer.apple.com/documentation/os/reading_unix_manual_pages)。对于那里记录的命令，我们建议使用 https://keith.github.io/xcode-man-pages/, 这是 Xcode 捆绑的所有苹果 man 手册的 HTML。

- **所有链接必须放在尖括号（`<` 和 `>`）中，以便在客户端中正确呈现。**

- 我们更倾向于在翻译页面中直接使用英文页面的更多信息链接。

### 版本化链接

当一个应用程序或发行版的包具有版本化链接时，我们更倾向于链接到文档的最新版本（即 `latest`），或者如果网站自动重定向到文档的最新版本，则不用链接到任何版本。

例如，使用：

- <https://manpages.debian.org/latest/apt/apt.8.html> 而不是 <https://manpages.debian.org/bookworm/apt/apt.8.en.html>。
- <https://docs.aws.amazon.com/cdk/latest/guide/cli.html> 而不是 <https://docs.aws.amazon.com/cdk/v2/guide/cli.html>。

### Microsoft Learn 链接

当链接到 Microsoft Learn 页面时，请删除地址中的语言环境，因为网站会自动重定向到读者的首选语言环境。例如，使用 <https://learn.microsoft.com/windows-server/administration/windows-commands/cd> 而不是 <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cd>。

此外，如果链接与 PowerShell 命令文档相关，请删除**文档版本指示符**（即文档来源的 PowerShell/module 版本），即地址中以 `?view=` 开头的部分。

- 使用 <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/select-string> 而不是 <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/select-string?view=powershell-7.4>。
- 使用 <https://learn.microsoft.com/powershell/module/powershellget/install-module> 而不是 <https://learn.microsoft.com/en-us/powershell/module/powershellget/install-module?view=powershellget-1.x>。

## 帮助和版本命令

- 通常我们将帮助命令和版本命令**按照这个顺序**放在页面的**最后两个**示例中，以突出页面开头更实用的命令。如果需要，它们可以被替换为其他有用的示例。
- 为了保持一致性，我们更推荐使用通用的术语 `显示帮助` 和 `显示版本` 来描述这些命令。
- 如果命令在 Windows 等平台中使用了不同的标志，建议记录下帮助和版本示例。

## 特定语言规则

以下部分包含了用于翻译页面的额外的特定语言规则：

## 中西文混排规则

中文、西文、阿拉伯数字写在同一个句子时，需要注意排版。

以下规则适用于中文（zh）和繁体中文（zh_TW）：

1. 在西文单词和数字前后放置一个空格。
   例如：`列出所有 docker 容器` 而不是 `列出所有 docker 容器`。
   例如：`宽度为 50 个字` 而不是 `宽度为 50 个字`。
2. 除了度数和百分比，在数字和单位之间留一个空格。
   例如：`容量 50 MB` 而不是 `容量 50MB`。
   对于度数和百分比：使用 `50°C` 和 `50%` 而不是 `50 °C` 和 `50 %`.
3. 不要在全角标点符号前后放置空格。
   例如：`开启 shell，进入交互模式` 而不是 `开启 shell ，进入交互模式`。
4. 除了西文长句，一律使用全角标点符号。
   例如：`嗨，你好。` 而不是 `嗨，你好.`。
5. 当最句子最后一个字符是半角时，使用半角标点符号来结束句子。
   例如：`将代码转化为 Python 3.` 而不是 `将代码转化为 Python 3。`。
6. 使用精准的专有名词，不要使用非官方的中文缩写。
   例如：`Facebook` 而非 `facebook`、`fb` 或 `脸书`。

为保持可读性和一致性，将页面翻译成中文时，请尽可能遵守以上 6 条规则。

有关更多中西文混排规则的信息，请参考 [《中文文案排版指北》](https://github.com/sparanoid/chinese-copywriting-guidelines)。

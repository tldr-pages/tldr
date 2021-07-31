# Style guide

When you are contributing to `tldr`, please follow the format specifications below.

Please note that the following specifications only apply to the Chinese translation of the `tldr` page.

## Layout

First of all, Your page should look like:

```
# 命令名称

> 短小精悍的描述。
> 描述最好只有一行；当然，如果需要，也可以是两行。
> 更多信息：<https://example.com>.

- 命令描述：

`命令 -选项1 -选项2 -参数1 {{参数的值}}`

- 命令描述：

`命令 -选项1 -选项2`
```

When you submit your contribution to a pull request, a script will automatically check whether your contribution conforms to the above format.

You can also test your contributions locally before submitting them:

```
npm install tldr-lint
tldrl -f {{page.md}}
```

For other ways to use `tldrl`, such as checking the formats of an entire directory, [`tldr tldrl`](https://github.com/tldr-pages/tldr/blob/master/pages/common/tldrl.md) is your best place to go!

If you use the Node.js client of tldr-pages, you can use `-f` (`--render`) option after the command to preview your page locally:

```
tldr --render {{page.md}}
```

## Chinese-Latin mix and format details

In this section, **except for commands**, the text layout follows [*Chinese Copywriting Guidelines*](https://github.com/sparanoid/chinese-copywriting-guidelines/blob/master/README.en-US.md).

Brief summary:

- A space must be added between Chinese and Latin words, numbers, and units.
- No spaces are added between full-width punctuations and other characters.
- Use full-width punctuations except for long Latin clauses.
- Use precise form for technical terms, and do not use Chinese-specific abbreviations.

For more information and examples of Chinese-Latin mix, please check out [*Chinese Copywriting Guidelines*](https://github.com/sparanoid/chinese-copywriting-guidelines/blob/master/README.en-US.md) and Pull request [#5420](https://github.com/tldr-pages/tldr/pull/5240).

## Token syntax

When the command involves the value provided by the user, please use the `{{token}}` syntax to make the `tldr` client highlight them automatically:

`tar -cf {{目标.tar}} {{文件1}} {{文件2}} {{文件3}}`

When translating, please translate tokens into Chinese as much as possible. The following are the rules for naming token:

1. The token must be short and precise.  
   For example, `{{源文件}}` or `{{钱包.txt}}`.
2. If the token is written in Latin, use [`snake_case`](https://en.wikipedia.org/wiki/Snake_case) for multi-word tokens.
3. For any reference to paths to files or directories, use the format `{{目录/子目录/<占位符>}}`.  
   For example, `ln -s {{目录/子目录/源文件}} {{目录/子目录/链接}}`.  
   In case of a possible reference both to a file or a directory, use `{{目录/子目录/文件或目录}}`
4. Unless the file is specific, the path format of the above `{{目录/子目录/<占位符>}}` applies to all commands that include a path.
5. If the file extension required by the command is ascertained, please add the file extension in the token.  
   For example, `unrar x {{压缩包.rar}}`.  
   If the file **requires** to have an extension, use `{{.ext}}`.  
   For example, `find {{起始目录}} -name '{{*.ext}}'` using `{{*.ext}}` explains the command without being unnecessarily specific;  
   But in a command like `wc -l {{文件}}`, using token without extension `{{文件}}` is sufficient.
6. If the example is clearer with an actual value rather than a generic placeholder, please use a value in the example.  
   For example, `iostat {{2}}` is clearer than `iostat {{以秒为单位的间隔}}`.
7. If a command may have an irreversible impact on the file system or device, please rewrite the example carefully so that it cannot be copied, pasted and executed blindly.  
   For example, `ddrescue --force --no-scrape /dev/sda /dev/sdb` may cause a devastating impact to the system when blindly copied and pasted;  
   `ddrescue --force --no-scrape {{/dev/sdX}} {{/dev/sdY}}` is safer.  
   Thus, please use the `{{/dev/sdXY}}` placeholder for *block devices* instead of `/dev/sda1`.

Tokens should be as understandable as possible and make people know how to fill them with other value at first glance.

If any technical term appears in a command description, please enclose it with `backquotes`:

1. Paths, ex. `package.json`, `/etc/package.json`.
2. Extensions, ex. `.dll`.
3. Commands, ex. `ls`.
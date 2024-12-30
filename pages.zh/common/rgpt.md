# rgpt

> 一个自动化代码审查工具，使用GPT，可以直接从终端使用。
> 更多信息：<https://github.com/vibovenkat123/review-gpt>。

- 向GPT请求改进代码，不使用额外选项：

`rgpt --i "$(git diff {{path/to/file}})"`

- 在审查代码时，让`rgpt`提供更详细的输出：

`rgpt --v --i "$(git diff {{path/to/file}})"`

- 请求GPT改进代码，并限制为特定数量的GPT3令牌：

`rgpt --max {{300}} --i "$(git diff {{path/to/file}})"`

- 使用0到2之间的浮动值请求GPT提供更独特的结果。（值越高，结果越独特）：

`rgpt --pres {{1.2}} --i "$(git diff {{path/to/file}})"`

- 请求GPT使用特定模型审查代码：

`rgpt --model {{davinci}} --i "$(git diff {{path/to/file}})"`

- 让`rgpt`使用JSON输出：

`rgpt --json --i "$(git diff {{path/to/file}})"`
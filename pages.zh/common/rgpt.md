# rgpt

> 一个可以从终端直接使用的自动化代码审查工具，使用了 GPT 技术。
> 更多信息：<https://github.com/vibovenkat123/review-gpt>.

- 不使用额外选项，请求 GPT 改进代码：

`rgpt --i "$(git diff {{path/to/file}})"`

- 在审查代码时，从 `rgpt` 获取更详细的详细输出：

`rgpt --v --i "$(git diff {{path/to/file}})"`

- 请求 GPT 改进代码，并限制生成的 GPT3 令牌数量：

`rgpt --max {{300}} --i "$(git diff {{path/to/file}})"`

- 使用 0 到 2 之间的浮点值请求 GPT 提供更独特的结果（值越高，结果越独特）：

`rgpt --pres {{1.2}} --i "$(git diff {{path/to/file}})"`

- 使用特定模型请求 GPT 审查代码：

`rgpt --model {{davinci}} --i "$(git diff {{path/to/file}})"`

- 使 `rgpt` 使用 JSON 输出：

`rgpt --json --i "$(git diff {{path/to/file}})"`
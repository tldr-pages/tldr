# rgpt

> An automated code review tool that uses GPT you can use straight from your terminal.
> More information: <https://github.com/vibovenkat123/review-gpt>.

- Ask GPT to improve the code with no extra options:

`rgpt --i "$(git diff {{path/to/file}})"`

- Get a more detailed verbose output from `rgpt` while reviewing the code:

`rgpt --v --i "$(git diff {{path/to/file}})"`

- Ask GPT to improve the code and limit it to a certain amount of GPT3 tokens:

`rgpt --max {{300}} --i "$(git diff {{path/to/file}})"`

- Ask GPT for a more unique result using a float value between 0 and 2. (higher = more unique):

`rgpt --pres {{1.2}} --i "$(git diff {{path/to/file}})"`

- Ask GPT to review your code using a specific model:

`rgpt --model {{text-davinci-003}} --i "$(git diff {{path/to/file}})"`

- Make `rgpt` use a JSON output:

`rgpt --json --i "$(git diff {{path/to/file}})"`

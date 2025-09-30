# repomix

> Pack a Github repository into an AI-friendly file.
> More information: <https://github.com/yamadashy/repomix>.

- Output custom format:

`repomix {{[-o|--output]}} {{path/to/file}} --style {{xml|markdown|plain}}`

- Send output to `stdout`:

`repomix --stdout > {{path/to/file}}`

- Send output to `stdout`, then pipe into another program:

`repomix --stdout | {{less}}`

- Output with compression:

`repomix --compress`

- Process specific files:

`repomix --include "{{src/**/*.ts}}" --ignore "{{**/*.test.ts}}"`

- Pack a repository from a branch:

`repomix --remote {{https://github.com/user/repo/tree/main}}`

- Pack a repository at a specific commit:

`repomix --remote {{https://github.com/user/repo/commit/836abcd7335137228ad77feb28655d85712680f1}}`

- Pack repository using shorthand:

`repomix --remote {{user/repo}}`

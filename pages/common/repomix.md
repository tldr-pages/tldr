# repomix

> Pack a Github repository into an AI-friendly file.
> More information: <https://github.com/yamadashy/repomix>.

- Custom output:

`repomix {{[-o|--output]}} {{path/to/file}} --style {{xml|markdown|plain}}`

- Output to `stdout`:

`repomix --stdout > {{path/to/file}}`

- Send output to `stdout`, then pipe into `less`:

`repomix --stdout | less`

- Custom output with compression:

`repomix --compress`

- Process specific files:

`repomix --include "{{src/**/*.ts}}" --ignore "{{**/*.test.ts}}"`

- Remote repository with branch:

`repomix --remote {{https://github.com/user/repo/tree/main}}`

- Remote repository with commit:

`repomix --remote {{https://github.com/user/repo/commit/836abcd7335137228ad77feb28655d85712680f1}}`

- Remote repository with shorthand:

`repomix --remote {{user/repo}}`

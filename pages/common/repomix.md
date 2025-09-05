# repomix

> Pack a Github repository into an AI-friendly file.
> More information: <https://github.com/yamadashy/repomix>.

- Custom output:

`repomix -o output.xml --style xml`

- Output to stdout:

`repomix --stdout > custom-output.txt`

- Send output to stdout, then pipe into another command (for example, simonw/llm):

`repomix --stdout | llm "Please explain what this code does."`

- Custom output with compression:

`repomix --compress`

- Process specific files:

`repomix --include "src/**/*.ts" --ignore "**/*.test.ts"`

- Remote repository with branch:

`repomix --remote https://github.com/user/repo/tree/main`

- Remote repository with commit:

`repomix --remote https://github.com/user/repo/commit/836abcd7335137228ad77feb28655d85712680f1`

- Remote repository with shorthand:

`repomix --remote user/repo`

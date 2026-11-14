# pkg-pr-new

> Publish continuous preview releases of npm packages for every commit and pull request without touching npm.
> More information: <https://github.com/stackblitz-labs/pkg-pr-new>.

- Publish a preview release for the package in the current directory:

`pkg-pr-new publish`

- Publish preview releases for multiple workspace packages in a monorepo:

`pkg-pr-new publish "{{./packages/*}}"`

- Publish using compact installation URLs in pull request comments:

`pkg-pr-new publish --compact`

- Generate preview tarballs using pnpm instead of npm:

`pkg-pr-new publish --pnpm`

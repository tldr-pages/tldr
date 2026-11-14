# changelogen

> Generate changelogs and bump package versions using Conventional Commits.
> More information: <https://github.com/unjs/changelogen>.

- Generate and preview the changelog since the last git tag:

`changelogen`

- Bump the version, update the changelog file, and create a git commit and tag:

`changelogen --release`

- Push the release commit and tag to the remote repository:

`changelogen --release --push`

- Specify a custom starting reference or tag for the changelog range:

`changelogen --from {{v1.0.0}}`

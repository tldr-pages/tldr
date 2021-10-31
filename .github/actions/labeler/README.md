# @tldr-pages/labeler

GitHub action that handles labeling PRs for the tldr-pages/tldr repo.

## Usage

```yaml
on: ['pull_request_target']

permissions:
  pull-requests: "write"

jobs:
  labeler:
    runs-on: ubuntu-latest

    steps:
    - uses: ./.github/actions/labeler
      with:
        repo-token: "${{ secrets.GITHUB_TOKEN }}"
```

## Contributing

1. Configure and install dependencies: `npm install`
1. Create a new branch `git checkout -b my-branch-name`
1. Make any changes
1. Update the `dist/` files: `npm run build`
1. Push your fork and submit a PR

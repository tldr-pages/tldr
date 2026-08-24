# brew tap

> Tap a Homebrew formula repository. If no arguments are provided, list all installed Homebrew taps.
> More information: <https://docs.brew.sh/Manpage#tap-options-userrepo-url>.

- List installed Homebrew taps:

`brew tap`

- Tap a Git repository hosted on GitHub:

`brew tap {{github_username}}/{{github_repository_name}}`

- Tap a Git repository hosted outside of GitHub:

`brew tap {{username}}/{{repository_name}} {{git_clone_url}}`

- Tap a repository hosted on GitLab:

`brew tap {{username}}/{{repository_name}} https://gitlab.com/{{username}}/{{repository_name}}.git`

- Display help:

`brew tap {{[-h|--help]}}`

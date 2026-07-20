# github-backup

> Backup a GitHub user or organization's repositories and metadata.
> More information: <https://github.com/josegonzalez/python-github-backup>.

- Backup a user's repositories:
  `github-backup {{username}} --output-directory {{path/to/directory}} --repositories`

  - Backup a user's repositories including private ones:
    `github-backup {{username}} --token {{github_token}} --output-directory {{path/to/directory}} --repositories --private`

    - Backup an organization's repositories:
      `github-backup {{organization}} --output-directory {{path/to/directory}} --repositories --organization`

      - Backup repositories and also include issues and pull requests:
        `github-backup {{username}} --output-directory {{path/to/directory}} --repositories --issues --pulls`

        - Backup a single repository of a user:
          `github-backup {{username}} --output-directory {{path/to/directory}} --repositories --repository {{repository_name}}`

          - Backup a user's repositories including wikis:
            `github-backup {{username}} --output-directory {{path/to/directory}} --repositories --wikis`
            

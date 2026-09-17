# fj

> Interact with Forgejo instances from the terminal.
> More information: <https://codeberg.org/forgejo-contrib/forgejo-cli>.

- Log in to a Forgejo instance:

`fj auth login`

- Clone a Forgejo repository locally:

`fj repo clone {{owner}}/{{repository}}`

- Create a new issue in the current repository:

`fj issue create`

- Open an issue in the default web browser:

`fj issue browse {{issue_number}}`

- Create a new pull request:

`fj pr create`

- Check out a specific pull request locally in a new branch:

`fj pr checkout {{pr_number}}`

- List all releases on the current repository:

`fj release list`

- Show the currently authenticated user:

`fj whoami`

# gh-ruleset

> Manage GitHub repository rulesets.
> See also: `gh rs`.
> More information: <https://cli.github.com/manual/gh_ruleset>.

- List all rulesets for the current repository:

`gh ruleset list`

- List all rulesets for a specific organization:

`gh ruleset list --org {{organization_name}}`

- Check the rules that apply to the current branch:

`gh ruleset check`

- Check the rules that apply to a specific branch in another repository:

`gh ruleset check {{branch_name}} --repo {{owner/repo}}`

- Interactively select and view a ruleset for the current repository:

`gh ruleset view`

- View a specific ruleset by its ID:

`gh ruleset view {{ruleset_id}}`

- View an organization-level ruleset by its ID:

`gh ruleset view {{ruleset_id}} --org {{organization_name}}`

- Open the list of rulesets for a specific repository in the browser:

`gh ruleset list --repo {{owner/repo}} --web`

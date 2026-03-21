# zizmor

> Find security issues in GitHub Actions workflows and action definitions.
> More information: <https://woodruffw.github.io/zizmor/>.

- Audit all workflows and actions in the current directory:

`zizmor .`

- Audit a specific workflow file:

`zizmor {{path/to/workflow.yml}}`

- Audit a remote GitHub repository (requires a GitHub token):

`zizmor --gh-token {{token}} {{username/repository}}`

- Run only offline audits (no network requests):

`zizmor --offline {{path/to/workflow.yml}}`

- Output results in SARIF format:

`zizmor --format sarif {{path/to/workflow.yml}}`

- Filter findings by minimum severity:

`zizmor --min-severity {{informational|low|medium|high}} .`

- Display help:

`zizmor --help`

- Display version:

`zizmor --version`

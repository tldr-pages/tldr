# gh-profiler

> Examine a GitHub user's profile to help decide how much to invest in their contributions.
> More information: <https://github.com/ehmatthes/gh-profiler#gh-profiler>.

- Profile a GitHub user, or the author of a PR or issue in the current repository:

`gh-profiler {{username|pr_number|issue_number}}`

- Show a concise profile with one flag per category:

`gh-profiler {{username|pr_number|issue_number}} --concise`

- Show a verbose profile, including explanations for each flag:

`gh-profiler {{username|pr_number|issue_number}} {{[-v|--verbose]}}`

- Profile the authors of the most recently opened PRs in a repository:

`gh-profiler https://github.com/{{owner}}/{{repo}} {{[-n|--num-targets]}} {{10}}`

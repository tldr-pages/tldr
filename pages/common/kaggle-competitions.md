# kaggle competitions

> Manage Kaggle competitions.
> More information: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#competitions>.

- List all competitions:

`kaggle {{[c|competitions]}} list`

- Download competition data:

`kaggle {{[c|competitions]}} download {{competition_name}}`

- Download specific file:

`kaggle {{[c|competitions]}} download {{competition_name}} {{[-f|--file]}} {{file}}`

- Submit files to a competition:

`kaggle {{[c|competitions]}} submit {{competition_name}} {{[-f|--file]}} {{path/to/file}} {{[-m|--message]}} "{{message}}"`

- Show or download leaderboard:

`kaggle {{[c|competitions]}} leaderboard {{competition_name}} {{--show|--download}}`

- View submissions:

`kaggle {{[c|competitions]}} submissions {{competition_name}}`

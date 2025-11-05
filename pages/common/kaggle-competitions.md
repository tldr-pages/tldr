# kaggle competitions

> Manage Kaggle competitions from the command-line.
> More information: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#competitions>.

- List all competitions:

`kaggle {{[c|competitions]}} list`

- Download competition data:

`kaggle competitions download {{competition_name}}`

- Download specific file:

`kaggle competitions download {{competition_name}} {{[-f|--file]}} {{file}}`

- Submit files to a competition:

`kaggle competitions submit {{competition_name}} {{[-f|--file]}} {{path/to/file}} {{[-m|--message]}} "{{message}}"`

- Show or download leaderboard:

`kaggle competitions leaderboard {{competition_name}} {{--show|--download}}`

- View submissions:

`kaggle competitions submissions {{competition_name}}`

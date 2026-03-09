# kaggle

> Official CLI for Kaggle implemented in Python 3.
> More information: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md>.

- View current configuration values:

`kaggle config view`

- Download a specific file from a competition dataset:

`kaggle {{[c|competitions]}} download {{competition}} {{[-f|--file]}} {{path/to/file}}`

- List competitions matching a search term:

`kaggle {{[c|competitions]}} list {{[-s|--search]}} {{search_term}}`

- List files available for a specific competition:

`kaggle {{[c|competitions]}} files {{competition}}`

- Submit a file to a competition with a message:

`kaggle {{[c|competitions]}} submit {{competition}} {{[-f|--file]}} {{path/to/submission.csv}} {{[-m|--message]}} "{{message}}"`

- List datasets matching a search term:

`kaggle {{[d|datasets]}} list {{[-s|--search]}} {{search_term}}`

- Download all files from a dataset:

`kaggle {{[d|datasets]}} download {{owner}}/{{dataset_name}}`

- List kernels (notebooks) matching a search term:

`kaggle {{[k|kernels]}} list {{[-s|--search]}} {{search_term}}`

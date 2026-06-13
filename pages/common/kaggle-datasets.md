# kaggle datasets

> Manage Kaggle datasets.
> More information: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#datasets>.

- List all datasets owned by a user or organization:

`kaggle {{[d|datasets]}} list --user {{username}}`

- Search dataset by name:

`kaggle {{[d|datasets]}} list {{[-s|--search]}} "{{dataset_name}}"`

- Download a dataset:

`kaggle {{[d|datasets]}} download "{{dataset_name}}"`

- Create a public dataset:

`kaggle {{[d|datasets]}} create {{[-p|--path]}} {{path/to/dataset}} {{[-u|--public]}}`

- Download metadata of dataset:

`kaggle {{[d|datasets]}} metadata {{dataset_name}}`

- Initialize metadata for dataset:

`kaggle {{[d|datasets]}} init {{[-p|--path]}} {{path/to/dataset}}`

- Delete a dataset:

`kaggle {{[d|datasets]}} delete {{dataset_name}}`

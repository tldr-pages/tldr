# kaggle datasets

> Manage Kaggle datasets from command line.
> More information: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#datasets>.

- List all datasets owned by a user or organization:

`kaggle {{[d|datasets]}} list --user {{username}}`

- Search dataset by name:

`kaggle datasets list {{[-s|--search]}} "{{dataset_name}}"`

- Download a dataset:

`kaggle datasets download "{{dataset_name}}"`

- Create a dataset with visibility type:

`kaggle datasets create {{[-p|--path]}} {{path/to/dataset}} {{--public|--private}}`

- Download metadata of dataset:

`kaggle datasets metadata {{dataset_name}}`

- Initialize metadata for dataset:

`kaggle datasets init {{[-p|--path]}} {{path/to/dataset}}`

- Delete a dataset:

`kaggle datasets delete {{dataset_name}}`

# kaggle datasets

> Manage Kaggle datasets from command line.
> More information: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#datasets>.

- List all dataset:

`kaggle datasets list --user {{username}}`

- Search dataset by name:

`kaggle datasets list -s "{{dataset_name}}"`

- Download a dataset:

`kaggle datasets download -d "{{dataset_name}}"`

- Create a dataset with visibility type:

`kaggle datasets create -p {{path/to/dataset}} {{--public|--private}}`

- Download metadata of dataset:

`kaggle datasets metadata -d {{dataset_name}}`

- Initialize metadata for dataset:

`kaggle datasets init -p {{path/to/dataset}}`

- Delete a dataset:

`kaggle datasets delete -d {{dataset_name}}`

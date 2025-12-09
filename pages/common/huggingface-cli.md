# huggingface-cli

> Interact with Hugging Face Hub.
> Login, manage local cache, download or upload files.
> More information: <https://huggingface.co/docs/huggingface_hub/guides/cli>.

- Login to Hugging Face Hub:

`huggingface-cli login`

- Display the name of the logged in user:

`huggingface-cli whoami`

- Log out:

`huggingface-cli logout`

- Print information about the environment:

`huggingface-cli env`

- Download files from an repository and print out the path (omit filenames to download entire repository):

`huggingface-cli download --repo-type {{repo_type}} {{repo_id}} {{filename1 filename2 ...}}`

- Upload an entire folder or a file to Hugging Face:

`huggingface-cli upload --repo-type {{repo_type}} {{repo_id}} {{path/to/local_file_or_directory}} {{path/to/repo_file_or_directory}}`

- Scan cache to see downloaded repositories and their disk usage:

`huggingface-cli scan-cache`

- Delete the cache interactively:

`huggingface-cli delete-cache`

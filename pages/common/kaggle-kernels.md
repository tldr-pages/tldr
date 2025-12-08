# kaggle kernels

> Manage Kaggle kernels.
> More information: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#kernels>.

- List all kernels:

`kaggle {{[k|kernels]}} list`

- List kernel output files:

`kaggle {{[k|kernels]}} files {{kernel_name}}`

- Initialize metadata file for a kernel (defaults to current directory):

`kaggle {{[k|kernels]}} init {{[-p|--path]}} {{path/to/directory}}`

- Push new code to a kernel and run the kernel:

`kaggle {{[k|kernels]}} push {{[-p|--path]}} {{path/to/directory}}`

- Pull a kernel:

`kaggle {{[k|kernels]}} pull {kernel_name}} {{-p|--path}} {{path/to/directory}}`

- Get data output from the latest kernel run:

`kaggle {{[k|kernels]}} output {{kernel_name}}`

- Display the status of the latest kernel run:

`kaggle {{[k|kernels]}} status {{kernel_name}}`

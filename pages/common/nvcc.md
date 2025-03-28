# nvcc

> The NVIDIA CUDA Compiler Driver.
> More information: <https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc>.

- Compile a CUDA program:

`nvcc {{path/to/source.cu}} {{[-o|--output-file]}} {{path/to/executable}}`

- Generate debug information:

`nvcc {{path/to/source.cu}} {{[-o|--output-file]}} {{path/to/executable}} {{[-g|--debug]}} {{[-G|--device-debug]}}`

- Include libraries from a different path:

`nvcc {{path/to/source.cu}} {{[-o|--output-file]}} {{path/to/executable}} {{[-I|--include-path]}} {{path/to/includes}} {{[-L|--library-path]}} {{path/to/library}} {{[-l|--library]}} {{library_name}}`

- Specify the compute capability for a specific GPU architecture:

`nvcc {{path/to/source.cu}} {{[-o|--output-file]}} {{path/to/executable}} {{[-gencode|--generate-code]}} arch={{arch_name}},code={{gpu_code_name}}`

# nvcc

> The NVIDIA CUDA Compiler Driver.
> More information: <https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc>.

- Compile a CUDA program:

`nvcc {{path/to/source.cu}} -o {{path/to/executable}}`

- Generate debu[g] information:

`nvcc {{path/to/source.cu}} -o {{path/to/executable}} --debug --device-debug`

- Include libraries from a different path:

`nvcc {{path/to/source.cu}} -o {{path/to/executable}} -I{{path/to/includes}} -L{{path/to/library}} -l{{library_name}}`

- Specify the compute capability for a specific GPU architecture:

`nvcc {{path/to/source.cu}} -o {{path/to/executable}} --generate-code arch={{arch_name}},code={{gpu_code_name}}`

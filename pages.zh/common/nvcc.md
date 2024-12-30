# nvcc

> NVIDIA CUDA 编译器驱动程序。
> 更多信息：<https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc>。

- 编译一个 CUDA 程序：

`nvcc {{path/to/source.cu}} -o {{path/to/executable}}`

- 生成调试信息：

`nvcc {{path/to/source.cu}} -o {{path/to/executable}} --debug --device-debug`

- 从不同路径包含库：

`nvcc {{path/to/source.cu}} -o {{path/to/executable}} -I{{path/to/includes}} -L{{path/to/library}} -l{{library_name}}`

- 为特定 GPU 架构指定计算能力：

`nvcc {{path/to/source.cu}} -o {{path/to/executable}} --generate-code arch={{arch_name}},code={{gpu_code_name}}`
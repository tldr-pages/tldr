# nvcc

> NVIDIA CUDA 编译器驱动。
> 更多信息：<https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc>。

- 编译 CUDA 程序：

`nvcc {{path/to/source.cu}} {{[-o|--output-file]}} {{path/to/executable}}`

- 生成调试信息：

`nvcc {{path/to/source.cu}} {{[-o|--output-file]}} {{path/to/executable}} {{[-g|--debug]}} {{[-G|--device-debug]}}`

- 包含来自不同路径的库：

`nvcc {{path/to/source.cu}} {{[-o|--output-file]}} {{path/to/executable}} {{[-I|--include-path]}} {{path/to/includes}} {{[-L|--library-path]}} {{path/to/library}} {{[-l|--library]}} {{library_name}}`

- 指定特定 GPU 架构的计算能力：

`nvcc {{path/to/source.cu}} {{[-o|--output-file]}} {{path/to/executable}} {{[-gencode|--generate-code]}} arch={{arch_name}},code={{gpu_code_name}}`
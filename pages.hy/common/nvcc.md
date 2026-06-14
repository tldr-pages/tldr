# nvcc

> NVIDIA CUDA Կազմողի վարորդ:.
> Լրացուցիչ տեղեկություններ. <https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/>:.

- Կազմել CUDA ծրագիր.:

`nvcc {{path/to/source.cu}} {{[-o|--output-file]}} {{path/to/executable}}`

- Ստեղծեք վրիպազերծման տեղեկատվություն.:

`nvcc {{path/to/source.cu}} {{[-o|--output-file]}} {{path/to/executable}} {{[-g|--debug]}} {{[-G|--device-debug]}}`

- Ներառեք գրադարաններ այլ ճանապարհից.:

`nvcc {{path/to/source.cu}} {{[-o|--output-file]}} {{path/to/executable}} {{[-I|--include-path]}} {{path/to/includes}} {{[-L|--library-path]}} {{path/to/library}} {{[-l|--library]}} {{library_name}}`

- Նշեք հաշվարկման հնարավորությունը հատուկ GPU ճարտարապետության համար.:

`nvcc {{path/to/source.cu}} {{[-o|--output-file]}} {{path/to/executable}} {{[-gencode|--generate-code]}} arch={{arch_name}},code={{gpu_code_name}}`

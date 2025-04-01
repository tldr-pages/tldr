# mpicc

> Open MPI C 编译器包装器。
> 这些包装器仅仅是 C 编译器上的轻量级外壳，它们在命令行中添加编译和链接 Open MPI 程序所需的相关编译器和链接器标志，然后调用底层的 C 编译器来实际执行命令。
> 更多信息：<https://www.mpich.org/static/docs/latest/www1/mpicc.html>.

- 将源代码文件编译成目标文件：

`mpicc -c {{path/to/file.c}}`

- 链接目标文件并生成可执行文件：

`mpicc -o {{executable}} {{path/to/object_file.o}}`

- 在一个命令中编译并链接源代码：

`mpicc -o {{executable}} {{path/to/file.c}}`

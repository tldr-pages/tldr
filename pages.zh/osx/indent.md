# indent

> 通过插入或删除空白来改变 C/C++ 程序的外观。
> 更多信息：<https://keith.github.io/xcode-man-pages/indent.1.html>.

- 按照 Berkeley 风格格式化 C/C++ 源代码：

`indent {{path/to/source_file.c}} {{path/to/indented_file.c}} -nbad -nbap -bc -br -c33 -cd33 -cdb -ce -ci4 -cli0 -di16 -fc1 -fcb -i4 -ip -l75 -lp -npcs -nprs -psl -sc -nsob -ts8`

- 按照 Kernighan & Ritchie (K&R) 风格格式化 C/C++ 源代码：

`indent {{path/to/source_file.c}} {{path/to/indented_file.c}} -nbad -bap -nbc -br -c33 -cd33 -ncdb -ce -ci4 -cli0 -cs -d0 -di1 -nfc1 -nfcb -i4 -nip -l75 -lp -npcs -nprs -npsl -nsc -nsob`

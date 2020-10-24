# swig

> Generate bindings between C / C++ code and various high level languages such as Javascript, Python, C#, and more.
> It uses special .i or .swg files to generate the bindings (C/C++ with SWIG directives, then outputs a C/C++ file that contains all of the wrapper code needed to build an extension module.

- Generate a binding between C++ and Python:

`swig -c++ -python -o {{path/to/output_wrapper.cpp}} {{path/to/swig_file.i}}`

- Generate a binding between C++ and Go:

`swig -go -cgo -intgosize 64 -c++ {{path/to/swig_file.i}}`

- Generate a binding between C and Java:

`swig -java {{path/to/swig_file.i}}`

- Generate a binding between C and Ruby and prefix the Ruby module with {{foo::bar::}}:

`swig -ruby -prefix "{{foo::bar::}}" {{path/to/swig_file.i}}`

# winebuild

> Generate the assembly and object files needed to build Wine DLLs and executables.
> More information: <https://manned.org/winebuild>.

- Build an assembly file for a DLL from a `.spec` or `.def` file:

`winebuild --dll {{[-E|--export]}} {{path/to/spec_file}} {{[-o|--output]}} {{path/to/output_file}}`

- Build an assembly file for an executable:

`winebuild --exe {{[-F|--filename]}} {{module_name}} {{[-o|--output]}} {{path/to/output_file}}`

- Build a `.def` file from a spec file:

`winebuild --def {{[-E|--export]}} {{path/to/spec_file}}`

- Build a static import library from a spec file:

`winebuild --implib {{[-E|--export]}} {{path/to/spec_file}} {{[-o|--output]}} {{path/to/library.a}}`

- Generate 64-bit code:

`winebuild {{[-m64]}} --dll {{[-E|--export]}} {{path/to/spec_file}}`

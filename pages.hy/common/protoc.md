# արձանագրություն

> Վերլուծեք Google Protobuf `.proto` ֆայլերը և ստացեք ելք նշված լեզվով:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/protoc>:.

- Ստեղծեք Python կոդը `.proto` ֆայլից.:

`protoc --python_out={{path/to/output_directory}} {{input_file.proto}}`

- Ստեղծեք Java կոդ `.proto` ֆայլից, որը ներմուծում է այլ `.proto` ֆայլեր:

`protoc --java_out={{path/to/output_directory}} --proto_path={{path/to/import_search_path}} {{input_file.proto}}`

- Ստեղծեք կոդ բազմաթիվ լեզուների համար.:

`protoc --csharp_out={{path/to/c#_output_directory}} --js_out={{path/to/js_output_directory}} {{input_file.proto}}`

- Տեքստային ձևաչափի հաղորդագրությունը կոդավորեք `.proto` ֆայլից ստացված պրոտոկոլային հաղորդագրության մեջ.:

`protoc < {{message.txt}} --encode={{TypeName}} {{input_file.proto}}`

- Արձանագրության հաղորդագրությունը վերծանել տեքստային ձևաչափի `.proto` ֆայլից.:

`protoc < {{message.bin}} --decode={{TypeName}} {{input_file.proto}}`

- Արձանագրության հաղորդագրությունը վերծանեք հում պիտակների/արժեքների զույգերի.:

`protoc < {{message.bin}} --decode_raw`

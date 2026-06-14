#թեստ

> Ստուգեք ֆայլերի տեսակները և համեմատեք արժեքները:.
> Վերադարձնում է 0, եթե պայմանը գնահատվում է true, 1, եթե այն գնահատվում է false:.
> Տես նաև՝ `[`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/test-invocation.html>:.

- Փորձեք, արդյոք տրված փոփոխականը հավասար է տրված տողի.:

`test "{{$MY_VAR}}" = "{{/bin/zsh}}"`

- Ստուգեք, թե արդյոք տվյալ փոփոխականը դատարկ է ([z]ero երկարություն).:

`test -z "{{$GIT_BRANCH}}"`

- Ստուգեք, արդյոք [f]ile կա.:

`test -f "{{path/to/file_or_directory}}"`

- Ստուգեք, եթե [d]գրացուցակ գոյություն չունի.:

`test ! -d "{{path/to/directory}}"`

- Եթե A-ն ճիշտ է, ապա սխալի դեպքում արեք B կամ C (նկատեք, որ C-ն կարող է գործարկվել նույնիսկ եթե A-ն ձախողվի):

`test {{condition}} && {{echo "true"}} || {{echo "false"}}`

- Օգտագործեք `test` պայմանական հայտարարության մեջ.:

`if test -f "{{path/to/file}}"; then echo "File exists"; else echo "File does not exist"; fi`

# rar

> RAR արխիվը: Աջակցում է բազմահատոր արխիվներին, որոնք կարող են ընտրովի ինքնաարտահանվել:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/rar>:.

- Արխիվացրեք 1 կամ ավելի ֆայլեր.:

`rar a {{path/to/archive_name.rar}} {{path/to/file1 path/to/file2 path/to/file3 ...}}`

- Արխիվացնել գրացուցակը.:

`rar a {{path/to/archive_name.rar}} {{path/to/directory}}`

- Արխիվը բաժանեք հավասար չափի մասերի (50 մ).:

`rar a -v{{50M}} -R {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- Գաղտնաբառը պաշտպանում է ստացված արխիվը.:

`rar a -p{{password}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- Գաղտնագրեք ֆայլի տվյալները և վերնագրերը գաղտնաբառով.:

`rar a -hp{{password}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- Օգտագործեք սեղմման հատուկ մակարդակ (0-5).:

`rar a -m{{compression_level}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

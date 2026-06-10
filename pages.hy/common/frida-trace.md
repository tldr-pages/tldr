# ֆրիդա-հետք

> Դինամիկ կերպով հետևել գործառույթի զանգերին:.
> Լրացուցիչ տեղեկություններ. <https://frida.re/docs/frida-trace/>:.

- Հետևեք գործընթացում օրինաչափությանը համապատասխանող բոլոր գործառույթներին.:

`frida-trace {{[-i|--include]}} "{{wildcard}}" {{process_name}}`

- Հետևեք որոշակի գործառույթ գործընթացում.:

`frida-trace {{[-i|--include]}} "{{function_name}}" {{process_name}}`

- Հետևեք բոլոր գործառույթներին հատուկ մոդուլում.:

`frida-trace {{[-I|--include-module]}} "{{module_name}}" {{process_name}}`

- Հետևեք գործառույթը USB-ով միացված սարքի վրա.:

`frida-trace {{[-U|--usb]}} {{[-i|--include]}} "{{function_name}}" {{process_name}}`

- Ստեղծեք գործընթաց և հետևեք գործառույթին.:

`frida-trace {{[-f|--file]}} {{path/to/executable}} {{[-i|--include]}} "{{function_name}}"`

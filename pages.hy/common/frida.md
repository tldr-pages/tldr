#Ֆրիդա

> Դինամիկ գործիքակազմ մշակողների, հակադարձ ինժեներների և անվտանգության հետազոտողների համար:.
> Լրացուցիչ տեղեկություններ. <https://frida.re/docs/frida-cli/>:.

- Սկսեք գործող գործընթացին կցված ինտերակտիվ կեղևը (REPL).:

`frida {{process_name}}`

- Սկսեք USB-ի միջոցով գործընթացին կցված ինտերակտիվ կեղևը.:

`frida {{[-U|--usb]}} {{process_name}}`

- Գործող գործընթացին կցեք իր PID-ով.:

`frida {{[-p|--attach-pid]}} {{pid}}`

- Ներբեռնեք JavaScript սկրիպտը գործընթացի մեջ.:

`frida {{[-l|--load]}} {{path/to/script.js}} {{process_name}}`

- Բեռնել սցենար Frida Codeshare-ից <https://codeshare.frida.re/>:

`frida {{[-c|--codeshare]}} {{script_name}} {{process_name}}`

# mkfifo

> Պատրաստեք անվանված խողովակներ, որոնք նաև հայտնի են որպես Առաջին դուրս գալը (FIFO):.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/mkfifo-invocation.html>:.

- Ստեղծեք անունով խողովակ տվյալ ուղու վրա.:

`mkfifo {{path/to/pipe}}`

- Ուղարկեք տվյալներ անունով խողովակի միջոցով և ուղարկեք հրամանը ֆոն.:

`echo "{{Hello World}}" > {{path/to/pipe}} &`

- Ստացեք տվյալներ անունով խողովակի միջոցով.:

`cat {{path/to/pipe}}`

- Կիսեք ձեր տերմինալի նիստը իրական ժամանակում.:

`mkfifo {{path/to/pipe}}; script {{[-f|--flush]}} {{path/to/pipe}}`

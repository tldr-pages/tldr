# unzip

> Extragerea fișierelor comprimate într-o arhivă ZIP.

- Extrageți fișierul (fișierele) zip (pentru mai multe fișiere, căi separate de fișiere în funcție de spații):

`unzip {{file(s)}}`

- Extrageţi fişierele zip la calea dată:

`unzip {{compressed_file(s)}} -d {{path/to/put/extracted_file(s)}}`

- Listează conținutul unui fișier zip fără extragere:

`unzip -l {{file.zip}}`

- Extrageţi conţinutul fişierelor pentru a stdout alături de numele fişierelor extrase:

`unzip -c {{file.zip}}`

- Extrageți un fișier zip creat pe Windows, care conține fișiere cu nume de fișiere non-ASCII (de exemplu, caractere chinezești sau japoneze):

`unzip -O {{gbk}} {{file.zip}}`

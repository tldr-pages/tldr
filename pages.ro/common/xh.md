# xh

> Instrument prietenos și rapid pentru trimiterea solicitărilor HTTP.
> Mai multe informaţii: <https://github.com/ducaale/xh>

- Trimiteți o cerere de obținere:

`xh {{httpbin.org/get}}`

- Trimiteți o solicitare POST cu un corp JSON (perechi cheie-valoare sunt adăugate la un obiect JSON de nivel superior - de exemplu `{"name”: „john”, „age”: 25}`):

`xh post {{httpbin.org/post}} {{name=john}} {{age:=25}}`

- Trimiteți o solicitare GET cu parametrii de interogare (ex. `first_param=5&second_param=true`):

`xh get {{httpbin.org/get}} {{first_param==5}} {{second_param==true}}`

- Trimiteți o solicitare de obținere cu un antet personalizat:

`xh get {{httpbin.org/get}} {{header-name:header-value}}`

- Faceți o solicitare de obținere și salvați corpul de răspuns într-un fișier:

`xh --download {{httpbin.org/json}} --output {{path/to/file}}`

# prqlc

> PRQL կոմպիլյատոր:.
> PRQL-ը տվյալների փոխակերպման ժամանակակից լեզու է՝ պարզ, հզոր, խողովակաշարով SQL-ի փոխարինում:.
> Լրացուցիչ տեղեկություններ. <https://prql-lang.org/book/project/integrations/prqlc-cli.html>:.

- Գործարկեք կոմպիլյատորը ինտերակտիվ կերպով.:

`prqlc compile`

- Կազմել որոշակի `.prql` ֆայլ `stdout`-ում՝:

`prqlc compile {{path/to/file.prql}}`

- Կազմել `.prql` ֆայլը `.sql` ֆայլում՝:

`prqlc compile {{path/to/source.prql}} {{path/to/target.sql}}`

- Կազմել հարցում.:

`echo "{{from employees | filter has_dog | select salary}}" | prqlc compile`

- Դիտեք գրացուցակը և կազմեք ֆայլի փոփոխության վրա.:

`prqlc watch {{path/to/directory}}`

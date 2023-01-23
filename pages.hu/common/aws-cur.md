# aws cur

> AWS használati jelentésdefiníciók létrehozása, lekérdezése és törlése. További információ: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/index.html>.

- AWS költség- és használati jelentésdefiníció létrehozása JSON fájlból:

`aws cur put-report-definition --report-definition file://{{path/to/report_definition.json}}`

- A bejelentkezett fiókhoz definiált használati jelentésdefiníciók listázása:

`aws cur describe-report-definitions`

- Használati jelentésdefiníció törlése:

`aws cur --region {{aws_region}} delete-report-definition --report-name {{report}}`

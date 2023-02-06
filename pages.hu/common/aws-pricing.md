# aws pricing

> Az Amazon Web Services szolgáltatásainak, termékeinek és árainak lekérdezése. További információk: <https://docs.aws.amazon.com/cli/latest/reference/pricing/>.

- Egy adott régió szolgáltatáskódjainak listázása:

`aws pricing describe-services --region {{us-east-1}}`

- Egy adott régió adott szolgáltatáskódjának attribútumainak listázása:

`aws pricing describe-services --service-code {{AmazonEC2}} --region {{us-east-1}}`

- Árképzési információk nyomtatása egy adott régióban lévő szolgáltatáskódhoz:

`aws pricing get-products --service-code {{AmazonEC2}} --region {{us-east-1}}`

- Egy adott régióban lévő szolgáltatáskód adott attribútumának értékeinek listázása:

`aws pricing get-attribute-values --service-code {{AmazonEC2}} --attribute-name {{instanceType}} --region {{us-east-1}}`

- Egy szolgáltatáskód árinformációjának nyomtatása az adott szolgáltatáskód típusára és helyére vonatkozó szűrők használatával:

`aws pricing get-products --service-code {{AmazonEC2}} --filters "{{Type=TERM_MATCH,Field=instanceType,Value=m5.xlarge}}" "{{Type=TERM_MATCH,Field=location,Value=US East (N. Virginia)}}" --region {{us-east-1}}`

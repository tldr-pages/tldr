# aws s3api

> Ստեղծեք և ջնջեք Amazon S3 դույլերը և խմբագրեք դույլի հատկությունները:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/s3api/>:.

- Ստեղծեք դույլ որոշակի տարածաշրջանում.:

`aws s3api create-bucket --bucket {{bucket_name}} --region {{region}} --create-bucket-configuration LocationConstraint={{region}}`

- Ջնջել դույլը.:

`aws s3api delete-bucket --bucket {{bucket_name}}`

- Ցուցակ դույլեր:

`aws s3api list-buckets`

- Թվարկե՛ք դույլի ներսում գտնվող առարկաները և ցույց տվեք միայն յուրաքանչյուր օբյեկտի բանալին և չափը.:

`aws s3api list-objects --bucket {{bucket_name}} --query '{{Contents[].{Key: Key, Size: Size}}}'`

- Ավելացրեք օբյեկտ դույլի մեջ.:

`aws s3api put-object --bucket {{bucket_name}} --key {{object_key}} --body {{path/to/file}}`

- Ներբեռնեք օբյեկտը դույլից (Ելքային ֆայլը միշտ վերջին փաստարկն է).:

`aws s3api get-object --bucket {{bucket_name}} --key {{object_key}} {{path/to/output_file}}`

- Կիրառեք Amazon S3 դույլի քաղաքականությունը նշված դույլի վրա.:

`aws s3api put-bucket-policy --bucket {{bucket_name}} --policy file://{{path/to/bucket_policy.json}}`

- Ներբեռնեք Amazon S3 դույլի քաղաքականությունը նշված դույլից.:

`aws s3api get-bucket-policy --bucket {{bucket_name}} --query Policy --output {{json|table|text|yaml|yaml-stream}} > {{path/to/bucket_policy}}`

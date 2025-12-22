# aws pricing

> 从 Amazon Web Services 查询服务、产品和定价信息。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/pricing/>.

- 列出特定区域的服务代码：

`aws pricing describe-services --region {{us-east-1}}`

- 列出特定区域中给定服务代码的属性：

`aws pricing describe-services --service-code {{AmazonEC2}} --region {{us-east-1}}`

- 打印特定区域中某个服务代码的定价信息：

`aws pricing get-products --service-code {{AmazonEC2}} --region {{us-east-1}}`

- 列出特定区域中某个服务代码的指定属性的取值：

`aws pricing get-attribute-values --service-code {{AmazonEC2}} --attribute-name {{instanceType}} --region {{us-east-1}}`

- 使用实例类型和位置作为过滤条件，打印某个服务代码的定价信息：

`aws pricing get-products --service-code {{AmazonEC2}} --filters "{{Type=TERM_MATCH,Field=instanceType,Value=m5.xlarge}}" "{{Type=TERM_MATCH,Field=location,Value=US East (N. Virginia)}}" --region {{us-east-1}}`

# aws pricing

> 查询来自 Amazon Web Services 的服务、产品和价格信息。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/pricing/>.

- 列出特定区域的服务代码：

`aws pricing describe-services --region {{us-east-1}}`

- 列出特定区域中给定服务代码的属性：

`aws pricing describe-services --service-code {{AmazonEC2}} --region {{us-east-1}}`

- 打印特定区域中服务代码的价格信息：

`aws pricing get-products --service-code {{AmazonEC2}} --region {{us-east-1}}`

- 列出特定区域中服务代码的特定属性的值：

`aws pricing get-attribute-values --service-code {{AmazonEC2}} --attribute-name {{instanceType}} --region {{us-east-1}}`

- 使用实例类型和位置过滤器打印服务代码的价格信息：

`aws pricing get-products --service-code {{AmazonEC2}} --filters "{{Type=TERM_MATCH,Field=instanceType,Value=m5.xlarge}}" "{{Type=TERM_MATCH,Field=location,Value=US East (N. Virginia)}}" --region {{us-east-1}}`
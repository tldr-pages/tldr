# stripe

> 与 Stripe 账户进行交互。
> 更多信息：<https://docs.stripe.com/stripe-cli>.

- 跟踪账户活动日志：

`stripe logs tail`

- 监听事件，过滤名为 `charge.succeeded` 的事件，并将它们转发到 localhost:3000/events：

`stripe listen --events="{{charge.succeeded}}" --forward-to="{{localhost:3000/events}}"`

- 发送测试的 Webhook 事件：

`stripe trigger {{charge.succeeded}}`

- 创建客户：

`stripe customers create --email="{{test@example.com}}" --name="{{Jenny Rosen}}"`

- 以 JSON 格式输出：

`stripe listen --print-json`
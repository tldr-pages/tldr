# Stripe

> 与 Stripe 账户互动。
> 更多信息：<https://docs.stripe.com/stripe-cli>。

- 跟踪账户上的活动日志：

`stripe logs tail`

- 监听事件，过滤名称为 `charge.succeeded` 的事件，并将其转发到 localhost:3000/events：

`stripe listen --events="{{charge.succeeded}}" --forward-to="{{localhost:3000/events}}"`

- 发送测试 webhook 事件：

`stripe trigger {{charge.succeeded}}`

- 创建客户：

`stripe customers create --email="{{test@example.com}}" --name="{{Jenny Rosen}}"`

- 输出为 JSON：

`stripe listen --print-json`
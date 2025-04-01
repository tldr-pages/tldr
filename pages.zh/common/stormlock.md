# Stormlock

> 集中的锁定系统。
> 更多信息：<https://github.com/tmccombs/stormlock>.

- 获取资源的租约：

`stormlock acquire {{resource}}`

- 释放指定资源的指定租约：

`stormlock release {{resource}} {{lease_id}}`

- 显示资源的当前租约信息（如果有）：

`stormlock current {{resource}}`

- 测试指定资源是否有当前活跃的租约：

`stormlock is-held {{resource}} {{lease_id}}`

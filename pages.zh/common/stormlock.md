# Stormlock

> 集中锁定系统。
> 更多信息： <https://github.com/tmccombs/stormlock>。

- 为资源获取租约：

`stormlock acquire {{resource}}`

- 释放给定资源的租约：

`stormlock release {{resource}} {{lease_id}}`

- 显示当前资源的租约信息（如果有的话）：

`stormlock current {{resource}}`

- 测试给定资源的租约是否当前有效：

`stormlock is-held {{resource}} {{lease_id}}`
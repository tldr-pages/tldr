# lvchange

> Change attributes or the activation state of logical volumes.
> More information: <https://manned.org/lvchange>.

- Activate a logical volume:

`lvchange {{[-a|--activate]}} y {{/dev/vg_name/lv_name}}`

- Deactivate a logical volume:

`lvchange {{[-a|--activate]}} n {{/dev/vg_name/lv_name}}`

- Enable autoactivation for a logical volume:

`lvchange {{[-a|--activate]}} ay {{/dev/vg_name/lv_name}}`

- Set a logical volume to read-only (use `rw` for read-write):

`lvchange {{[-p|--permission]}} r {{/dev/vg_name/lv_name}}`

- Skip activation for a logical volume:

`lvchange {{[-k|--setactivationskip]}} y {{/dev/vg_name/lv_name}}`

- Refresh a logical volume using the latest metadata:

`lvchange --refresh {{/dev/vg_name/lv_name}}`

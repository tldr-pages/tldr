# lvmpersist

> Manage persistent reservations (PR) on block devices or all PVs in a volume group.
> More information: <https://manned.org/lvmpersist>.

- Start PR on all PVs in a VG with a local key (exclusive access by default):

`lvmpersist start --ourkey {{0x1234abcd}} --vg {{vg_name}}`

- Start PR for a shared VG (allow multiple hosts):

`lvmpersist start --ourkey {{0x1234abcd}} --access {{sh}} --vg {{vg_name}}`

- Stop PR on a VG and unregister the local key:

`lvmpersist stop --ourkey {{0x1234abcd}} --vg {{vg_name}}`

- Take over a local VG by preempting another host while starting PR:

`lvmpersist start --ourkey {{0xmy_key}} --removekey {{0xother_key}} --vg {{vg_name}}`

- Remove another host's key from a shared VG:

`lvmpersist remove --ourkey {{0xmy_key}} --removekey {{0xother_key}} --vg {{vg_name}}`

- Show registered keys and reservations for a VG:

`lvmpersist read --vg {{vg_name}}`

- Operate on specific devices instead of a VG:

`lvmpersist start --ourkey {{0x1234abcd}} --device {{/dev/sdX}} --device {{/dev/mapper/mpathY}}`

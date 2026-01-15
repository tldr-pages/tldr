# iscsiadm

> Manage iSCSI sessions, nodes, and discovery.
> More information: <https://manned.org/iscsiadm>.

- Show active iSCSI sessions:

`iscsiadm --mode session`

- List all known iSCSI nodes:

`iscsiadm --mode node`

- Discover available iSCSI targets on a portal (no authentication):

`iscsiadm --mode discovery --type sendtargets --portal {{ip_address}}`

- Log in to a specific iSCSI target without authentication:

`iscsiadm --mode node --targetname {{iqn}} --portal {{ip_address}}:3260 --login`

- Log out from a specific iSCSI target:

`iscsiadm --mode node --targetname {{iqn}} --portal {{ip_address}}:3260 --logout`

- Create an iSCSI node when discovery is blocked (for CHAP authentication):

`iscsiadm --mode node --op new --targetname {{iqn}} --portal {{ip_address}}:3260`

- Configure CHAP authentication for an iSCSI target:

`iscsiadm --mode node --targetname {{iqn}} --portal {{ip_address}}:3260 --op update --name node.session.auth.authmethod --value CHAP`

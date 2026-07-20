# topgrade

> Upgrade all the things.
> More information: <https://github.com/topgrade-rs/topgrade>.
- Update everything:

  `topgrade`

  - Run only specific update steps (use `topgrade --help` to see all step names):

    `topgrade --only {{step_name1,step_name2}}`

    - Skip specific update steps:

      `topgrade --disable {{step_name1,step_name2}}`

      - Perform a dry run (show what would be done, but don't make changes):

        `topgrade --dry-run`

        - Only check for available updates without installing them:

          `topgrade --check`

          - Open the configuration file in the default editor:

            `topgrade --edit-config`

            - Cleanup old package versions after upgrading:

              `topgrade --cleanup`

# playwright

> A framework for web testing and automation.
> Note: this command is typically executed via `npx playwright`.
> More information: <https://playwright.dev/docs/intro>.

- Run all tests:

`playwright test`

- Run a specific test file:

`playwright test {{path/to/test_file.ts}}`

- Run tests in a specific browser project:

`playwright test --project={{project_name}}`

- Run tests in UI mode (interactive graphical interface):

`playwright test --ui`

- Run tests with the Playwright Inspector for debugging:

`playwright test --debug`

- Show the HTML report of the previous test run:

`playwright show-report`

- Generate tests by recording browser interactions:

`playwright codegen {{url}}`

- Install browsers required by Playwright:

`playwright install`

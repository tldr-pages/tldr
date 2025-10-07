# npm sbom

> Generate a Software Bill of Materials (SBOM) for your Node.js project.
> More information: <https://docs.npmjs.com/cli/npm-sbom>.

- Output a list of all dependencies in your project:

`npm sbom`

- Exclude both `dev` and `optional` dependencies:

`npm sbom --omit dev --omit optional`

- Generate an SBOM based only on the `package-lock.json`:

`npm sbom --package-lock-only`

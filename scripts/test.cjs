/**
 * SPDX-License-Identifier: MIT
 */
const { execSync } = require("child_process");

const isWindows = process.platform === "win32";

/**
 * Simple method to check whether the new Cross-Platform
 * PowerShell (`pwsh`) is installed.
 * 
 * More information: <https://learn.microsoft.com/powershell/scripting/whats-new/differences-from-windows-powershell>
 * 
 * @returns `"pwsh"` for the new PowerShell, `"powershell"` for legacy Windows PowerShell, and `null` for none.
 */
function detectPowerShell() {
    const checkCommand = isWindows ? "where pwsh" : "command -v pwsh";

    try {
        execSync(checkCommand, {stdio: "ignore"});
        return "pwsh"
    } catch (e) {
        return isWindows ? "powershell" : null
    }
}

if (isWindows) {
    const pwsh = detectPowerShell();
    console.info(`> ${pwsh} scripts/test.ps1`);
    execSync(`${pwsh} scripts/test.ps1`, {stdio: "inherit"});
} else {
    console.info(`> bash scripts/test.sh`);
    execSync("bash scripts/test.sh", {stdio: "inherit"});
}

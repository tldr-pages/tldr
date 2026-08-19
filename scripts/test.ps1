# SPDX-License-Identifier: MIT

# This script is executed by GitHub Actions for every successful push (on any branch, PR or not).
# It runs some basic tests on pages. If the build is also a PR, additional
# checks are run through the check-pr script, and any message or error is sent
# to tldr-bot to be commented on the PR.
#
# NOTE: must be run from the repository root directory to correctly work!

# check if a command is available to run in the system
function Exists {
    param (
        [string]$Command
    )
    
    if (Get-Command $Command -ErrorAction SilentlyContinue) {
        return $true
    }

    return $false
}

function Assert-Black {
    <#
    .DESCRIPTION
        Wrapper around black as it outputs everything to stderr,
        but we want to only print if there are actual errors, and not
        the "All done!" success message.
    #>
    $targetBlackVersion = (Get-Content requirements.txt | Where-Object { $_ -match "black==([\d.]+)" } | Select-String -Pattern "black==([\d.]+)").Matches.Groups[1].Value
    
    if ((python3 -m pip --disable-pip-version-check list) -match "black") {
        $errs = python3 -m black scripts --check --required-version "$targetBlackVersion" 2>&1
    }

    if (!$errs) {
        # skip the black check if the command is not available in the system.
        if ((!$CI) -and (-not (Exists("black")))) {
            Write-Host "Skipping black check, command not available."
            return $false
        }

        $errs = black scripts --check --required-version "$targetBlackVersion" 2>&1
    }

    if ($errs -match "does not match the running version") {
        Write-Host "Skipping black check, required version not available, try running: pip3 install -r requirements.txt"
        return $true
    }

    <#
    We want to ignore the exit code from black on failure so that we can
    do the conditional printing below
    #>
    if (!"$errs".StartsWith("All done!")) {
        Write-Error $errs
        return $false
    }
}

function Assert-Flake8 {
    # skip flake8 check if the command is not available in the system.
    if ((!$CI) -and (-not (Exists("flake8")))) {
        Write-Host "Skipping flake8 check, command not available."
        return $false
    }
    
    flake8 scripts
}

function Assert-Pytest {
    # skip pytest check if the command is not available in the system.
    if ((!$CI) -and (-not (Exists("pytest")))) {
        Write-Host "Skipping pytest check, command not available."
        return $false
    }

    $errs = pytest scripts/*.py 2>&1
    if ($errs -match "failed") {
        Write-Error $errs
        return $false
    }
}

function Assert-Shellcheck {
    # skip flake8 check if the command is not available in the system.
    if ((!$CI) -and (-not (Exists("shellcheck")))) {
        Write-Host "Skipping shellcheck check, command not available."
        return $false
    }
    
    shellcheck --enable require-double-brackets,avoid-nullary-conditions,quote-safe-variables scripts/*.sh
}

# Default test function, run by `npm test`.
function Assert-Tests {
    Get-ChildItem -Path "pages*" -Recurse | Select-String -SimpleMatch "*.md" | ForEach-Object {
        markdownlint $_.ToString()
    }
    tldr-lint ./pages
    Get-ChildItem -Path "pages.*" | ForEach-Object {
        $checks = "TLDR104"
        # Skip the `pages.en` symlink
        if (($_.LinkType) -or ($_.Name -eq "pages.en")) {
            return
        }

        $lang = @("ar", "bn", "fa", "hi", "ja", "ko", "lo", "ml", "ne", "ta", "th", "tr")
        $exp = ($lang -join "|")
        if ($_.Name -match $exp) {
            $checks += ",TLDR003,TLDR004,TLDR015"
        } elseif ($_.Name -match "zh") {
            $checks += ",TLDR003,TLDR004,TLDR005,TLDR015"
        }

        tldr-lint --ignore "$checks" $_.Name
    }
    Assert-Black | Out-Null
    Assert-Flake8 | Out-Null
    Assert-Pytest | Out-Null
    Assert-Shellcheck | Out-Null
}

function Assert-Tests-PR {
    <#
    .DESCRIPTION
        Special test function for GitHub Actions pull request builds.
        Runs run_tests collecting errors for tldr-bot.
    #>
    $errs = Assert-Tests 2>&1

    if ($errs) {
        Write-Error "Test failed!`n$errs`n"
        Write-Error 'Sending errors to tldr-bot.'
        Write-Host $errs | python3 scripts/send-to-bot.py report-errors
        Exit 1
    }
}

function Assert-Checks-PR {
    <#
    .DESCRIPTION
        Additional checks for GitHub Actions pull request builds.
        Only taken as suggestions, does not make the build fail.
    #>

    # Check which PowerShell version available, prefers `pwsh` over `powershell`.
    if (Exists("pwsh")) {
        $msgs = pwsh "scripts\check-pr.ps1"
    } else {
        $msgs = powershell "scripts\check-pr.ps1"
    }

    if ($msgs) {
        Write-Host $msgs | python3 scripts/send-to-bot.py report-check-results
    }
}

<#
###################################
# MAIN
###################################
#>

if (($CI -eq $true) -and ($GITHUB_REPOSITORY -eq "tldr-pages/tldr") -and ($PULL_REQUEST_ID)) {
    Assert-Checks-PR | Out-Null
    Assert-Tests-PR | Out-Null
} else {
    Assert-Tests | Out-Null
}

Write-Host 'Test ran successfully!'

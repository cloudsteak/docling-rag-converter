$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvDir = Join-Path $root ".venv"
$inputDir = Join-Path $root "input"
$outputDir = Join-Path $root "output"

function Remove-DirectoryContentsExceptGitkeep {
    param(
        [string]$Path
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Container)) {
        return
    }

    Get-ChildItem -LiteralPath $Path -Force | Where-Object { $_.Name -ne ".gitkeep" } | ForEach-Object {
        Remove-Item -LiteralPath $_.FullName -Recurse -Force
    }
}

if (Test-Path -LiteralPath $venvDir -PathType Container) {
    Remove-Item -LiteralPath $venvDir -Recurse -Force
}

Remove-DirectoryContentsExceptGitkeep -Path $inputDir
Remove-DirectoryContentsExceptGitkeep -Path $outputDir

Write-Host "Cleanup complete."

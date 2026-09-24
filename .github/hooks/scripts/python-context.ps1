$ErrorActionPreference = 'SilentlyContinue'

$pinned = if (Test-Path .python-version) { (Get-Content .python-version -Raw).Trim() } else { 'none' }
$system = (python --version 2>&1 | Out-String).Trim()
$uvPy   = (uv run python --version 2>&1 | Out-String).Trim()

$ctx = "Python environment (collected automatically at session start - do not re-check): " +
       ".python-version pin: $pinned; system python: $system; project python (uv run): $uvPy"

@{
  hookSpecificOutput = @{
    hookEventName     = 'SessionStart'
    additionalContext = $ctx
  }
} | ConvertTo-Json -Compress
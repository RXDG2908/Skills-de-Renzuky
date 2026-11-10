<#
  Fetch the tools the skills need, on THIS pc (nothing heavy lives in the repo).

  .\tools\install.ps1                      # list everything in tools.json
  .\tools\install.ps1 ffmpeg latentsync    # install those by name
  .\tools\install.ps1 -Category lipsync    # install a whole category
  .\tools\install.ps1 -All                 # install everything (big!)

  git tools are shallow-cloned into tools\_downloads\<name> (gitignored).
  Re-running updates them (git pull).
#>
param(
  [Parameter(Position = 0, ValueFromRemainingArguments = $true)][string[]]$Names,
  [Parameter()][string]$Category,
  [Parameter()][switch]$All
)
# Continue (not Stop): git/pip write progress to stderr, which PowerShell 5.1 would treat as fatal.
$ErrorActionPreference = 'Continue'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$manifest = Get-Content (Join-Path $here 'tools.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$dl = Join-Path $here '_downloads'
New-Item -ItemType Directory -Force $dl | Out-Null

$sel = $manifest.tools
if ($All) { }
elseif ($Category) { $sel = $sel | Where-Object { $_.category -eq $Category } }
elseif ($Names) { $sel = $sel | Where-Object { $Names -contains $_.name } }
else {
  $manifest.tools | Sort-Object category, name | Format-Table category, name, kind, license, url -AutoSize | Out-Host
  Write-Host "Usage: .\tools\install.ps1 <name> [<name>...] | -Category <cat> | -All"
  return
}
if (-not $sel) { Write-Warning "Nothing matched."; return }

foreach ($t in $sel) {
  Write-Host "==> $($t.name) [$($t.kind)]" -ForegroundColor Cyan
  if ($t.note) { Write-Host "    $($t.note)" }
  switch ($t.kind) {
    'git' {
      $dest = Join-Path $dl $t.name
      if (Test-Path (Join-Path $dest '.git')) { git -C $dest pull --ff-only }
      elseif (Test-Path $dest) { Write-Host "    $dest already exists (local copy, not a git clone) - skipped." }
      else { git clone --depth 1 $t.url $dest }
      Write-Host "    -> $dest  (read its README for setup / model weights)"
    }
    'pip'    { python -m pip install -U $t.id }
    'winget' { winget install --id $t.id -e --accept-source-agreements }
    'npx'    { Write-Host "    Nothing to install: runs with 'npx $($t.id)' (needs node)." }
    'manual' { Write-Host "    Download manually: $($t.url)" }
  }
}

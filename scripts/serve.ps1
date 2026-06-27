# Serve the site locally — open http://localhost:8080 in your browser
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location (Join-Path $Root "site")
Write-Host ""
Write-Host "  Stitch & Stone Co. — local preview" -ForegroundColor Cyan
Write-Host "  http://localhost:8080" -ForegroundColor Green
Write-Host "  Press Ctrl+C to stop" -ForegroundColor DarkGray
Write-Host ""
python -m http.server 8080

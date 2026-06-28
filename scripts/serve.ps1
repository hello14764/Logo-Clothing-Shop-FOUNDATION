# Serve the Astro site locally — open http://localhost:4321 in your browser
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $Root
Write-Host ""
Write-Host "  Logo Clothing Shop — local preview (Astro)" -ForegroundColor Cyan
Write-Host "  http://localhost:4321" -ForegroundColor Green
Write-Host "  Press Ctrl+C to stop" -ForegroundColor DarkGray
Write-Host ""
npm run dev

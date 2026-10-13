# Timeline paint benchmark (Phase 4.5). Windows PowerShell.
#
# Opens a scene with SPEEDTOON2D_TIMELINE_PAINT_LOG enabled, then either plays
# it for -Seconds or steps frames with . when -StepCount is set. Use
# -IncludeLoadPaints to keep the initial scene-open repaints; otherwise they
# are discarded before playback starts.
# Each line of the log is one cell-area repaint: "<microseconds> <width>x<height>". Summarise with
#   python test-scenes/tools/paint_stats.py <log>
#
# The run folder must be a deployed build (docs/BUILD-WINDOWS.md) and the
# startup/tips popups should be disabled so they do not cover the timeline.
param(
  [Parameter(Mandatory)] [string]$Scene,
  [Parameter(Mandatory)] [string]$Log,
  [string]$ExeDir,
  [string]$Exe = 'Tahoma2D.exe',
  [int]$LoadSeconds = 25,
  [int]$Seconds = 15,
  [int]$StepCount = 0,
  [switch]$IncludeLoadPaints
)
Add-Type -AssemblyName System.Windows.Forms
if (!$ExeDir) {
  $ExeDir = Join-Path $PSScriptRoot '..\..\toonz\build\RelWithDebInfo'
}
$Scene = (Resolve-Path $Scene).Path
$ExeDir = (Resolve-Path $ExeDir).Path
$ExePath = Join-Path $ExeDir $Exe
if (!(Test-Path $ExePath)) { throw "Executable not found: $ExePath" }
Remove-Item $Log -ErrorAction SilentlyContinue
$env:SPEEDTOON2D_TIMELINE_PAINT_LOG = $Log
$p = Start-Process -FilePath $ExePath -ArgumentList "`"$Scene`"" `
                   -WorkingDirectory $ExeDir -PassThru
Start-Sleep -Seconds $LoadSeconds
$shell = New-Object -ComObject WScript.Shell
$null = $shell.AppActivate($p.Id); Start-Sleep -Milliseconds 500
if (!$IncludeLoadPaints) {
  Remove-Item $Log -ErrorAction SilentlyContinue   # ignore load-time paints
}
if ($StepCount -gt 0) {
  for ($i = 0; $i -lt $StepCount; $i++) {
    [System.Windows.Forms.SendKeys]::SendWait('.') # Next frame
    Start-Sleep -Milliseconds 50
  }
} else {
  [System.Windows.Forms.SendKeys]::SendWait('p')   # Play
  Start-Sleep -Seconds $Seconds
  $null = $shell.AppActivate($p.Id)
  [System.Windows.Forms.SendKeys]::SendWait('p')   # Stop
}
Start-Sleep -Milliseconds 500
Stop-Process -Id $p.Id -ErrorAction SilentlyContinue
Remove-Item Env:SPEEDTOON2D_TIMELINE_PAINT_LOG
"log: $Log"

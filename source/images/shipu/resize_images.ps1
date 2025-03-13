# 调整图片大小的PowerShell脚本
Write-Host "正在调整图片大小为 2544x3464..." -ForegroundColor Green
Write-Host ""

# 获取脚本所在目录
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path

# 运行Python脚本
try {
    python "$scriptPath\resize_images_replace.py"
    Write-Host ""
    Write-Host "处理完成！" -ForegroundColor Green
} catch {
    Write-Host "发生错误: $_" -ForegroundColor Red
}

Write-Host ""
Write-Host "按任意键退出..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") 
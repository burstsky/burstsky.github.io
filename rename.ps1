$files = Get-ChildItem -Filter "IMG_*.jpg" | Sort-Object Name
$i = 1
foreach ($file in $files) {
    $newName = "$i.jpg"
    Write-Host "Renaming $($file.Name) to $newName"
    # 创建备份文件夹
    if (-not (Test-Path -Path "backup")) {
        New-Item -ItemType Directory -Path "backup" | Out-Null
    }
    # 先复制到备份文件夹
    Copy-Item -Path $file.FullName -Destination "backup\$($file.Name)"
    # 重命名文件
    Rename-Item -Path $file.FullName -NewName $newName
    $i++
}
Write-Host "重命名完成！共处理了 $($i-1) 个文件。" 
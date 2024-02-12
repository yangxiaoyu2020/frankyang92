@echo off

REM Fetch MASTER_IP using PowerShell
for /f "tokens=*" %%i in ('powershell -Command "& {& multipass info k3s | Select-String 'IPv4' | ForEach-Object { $_.ToString().Split(' ')[-1] }}"') do set MASTER_IP=%%i

REM Fetch TOKEN using PowerShell
for /f "tokens=*" %%j in ('powershell -Command "& {& multipass exec k3s sudo cat /var/lib/rancher/k3s/server/node-token}"') do set TOKEN=%%j

REM Install k3s on worker nodes
echo %TOKEN%
echo %MASTER_IP%

for %%f in (2 3) do (
    multipass exec worker%%f -- bash -c "curl -sfL https://rancher-mirror.rancher.cn/k3s/k3s-install.sh | INSTALL_K3S_MIRROR=cn K3S_URL=https://%MASTER_IP%:6443 K3S_TOKEN=\"%TOKEN%\" sh -"
)

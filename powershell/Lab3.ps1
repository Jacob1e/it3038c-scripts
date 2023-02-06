function getIP{
(get-netipaddress).ipv4address | Select-String "192*"
}

$IP = getIP
$USER = $env:Username
$HOSTNAME = $env:computername
$PS = $HOST.Version.Major
$Date = Get-Date -UFormat "%A, %B %d %Y"

Write-Host($BODY)


$BODY = ("This machines IP is $IP. The user is $USER. Hostname is $HOSTNAME. Powershell version is $PS. The date is $Date")

Send-MailMessage -To "Smit9j4@mail.uc.edu" -From "Jacobfn8@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)

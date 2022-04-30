Readme for sleep mode

- Put sleepmode.py in /home/[user]

- Update path for ExecStart to sleepmode.py in sleepmode.service

- Put sleepmode.service in /lib/systemd/system/

- Then Run: 
`sudo systemctl daemon-reload`
`sudo systemctl enable sleepmode.service`


- check status with:
`systemctl status sleepmode.service`

- stop with:
`sudo systemctl stop sleepmode.service`

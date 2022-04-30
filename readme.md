Readme for sleep mode

- Put sleepmode.py in /home/[user]

- Update path for ExecStart to sleepmode.py in sleepmode.service

- Put sleepmode.service in /lib/systemd/system/

- Then Run: 
`sudo systemctl daemon-reload`

- Then:
`sudo systemctl enable sleepmode.service`


- check status with:
`systemctl status sleepmode.service`

- stop with:
`sudo systemctl stop sleepmode.service`

CREDIT:
- https://tutorials-raspberrypi.com/connect-and-control-raspberry-pi-motion-detector-pir/ - main tutorial I used


MATERIALS:
- Ordered this: https://www.amazon.com/gp/product/B07KZW86YR/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1

Be sure to follow the pin out in the amazon listing and not the one in the tutorial.
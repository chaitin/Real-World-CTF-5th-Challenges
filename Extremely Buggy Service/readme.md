score: 500
`Web`,`difficulty:Schrödinger`

This challenge uses the official Oracle EBS image for deployment. The version used is version 12.2.10. The ovf md5 is b9411f2543fdf4b914ecb6b686972f9d.

You can download the image from the following link:

https://rwctf-attachment.oss-accelerate.aliyuncs.com/Oracle-E-Business-Suite-12.2.10_VISION_INSTALL.ova

Or, if you are familiar with Baidu Cloud, you can use the following Baidu Cloud link:

链接：https://pan.baidu.com/s/1xSkdi2q1vVvv7ArqwYv62A?pwd=dmhg

提取码：dmhg 

--来自百度网盘超级会员V6的分享

Or you can download this ovf from the Oracle official website:

http://edelivery.oracle.com/.

You need to `nc 47.90.215.212 9999` for queuing to get the challenge environment. At the same time, the number of instances that can be run is limited, please wait patiently.

Due to the instability of the queuing script, if you find the script abnormal, please contact us in time.

The online environment will only map the 8000 (web) port of the server. The flag is stored in `/home/oracle/flag`. You need to get the user `oracle` permission for read the flag.
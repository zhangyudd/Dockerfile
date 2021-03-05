[TOC]

## docker 创建vsftp容器
```
docker run -d -p 40020:20 -p 40021:21 -p 60000-60100:60000-60100 \
    -v /data/ftp/dispute-ftp:/home/vsftpd  \
    -e FTP_USER=ftpuser -e FTP_PASS=12345678 \
    -e PASV_ADDRESS=192.168.209.128 -e PASV_MIN_PORT=60000 -e PASV_MAX_PORT=60100 \
    --name ftp --restart=always fauria/vsftpd
```
## docker-compose 创建vsftp容器
```
version: '3.1'

services:
  vsftp:
    container_name: vsftp
    image: fauria/vsftpd
    restart: always
    ports:
      - "40020:20"
      - "40021:21"
      - "60000-60100:60000-60100"
    environment:
      FTP_USER: ftpuser
      FTP_PASS: "12345678"
      PASV_ADDRESS: "192.168.209.128"
      PASV_MIN_PORT: 60000
      PASV_MAX_PORT: 60100
    volumes:
      - /usr/share/zoneinfo/Asia/Shanghai:/etc/localtime
      - ./FtpDir:/home/vsftpd

```
## 创建多用户
- 以创建完成单用户ftp为前提，进入容器编辑配置文件
  
```cat /etc/vsftpd/virtual_users.txt (格式为用户名 另起一行密码，添加用户在上一个用户密码下再起一行)```

- 创建用户文件夹

```mkdir -p /home/vsftpd/lisi```

- 生成二进制文件

```db_load -T -t hash -f /etc/vsftpd/virtual_users.txt /etc/vsftpd/virtual_users.db```

- 重启容器生效





## 给ftp添加ssl证书
- 使用openssl生成ssl秘钥文件并复制到/etc/ssl/certs目录下
```
openssl req  -new -x509 -days 7300 -nodes -out vsftpd.pem -keyout vsftpd.pem 
cp vsftpd.pem /etc/ssl/certs/vsftpd.pem
chmod 400 /etc/ssl/certs/vsftpd.pem
```
- 修改配置文件
```
#ssl config
ssl_enable=YES
allow_anon_ssl=NO
force_local_data_ssl=YES
force_local_logins_ssl=YES
ssl_tlsv1=YES
ssl_sslv2=NO
ssl_sslv3=NO
rsa_cert_file=/etc/ssl/certs/vsftpd.pem
```
- 重启容器生效
[TOC]

---
# 安装

## 下载
    $ docker pull kylemanna/openvpn

## 全局变量(方便设置)
    $ OVPN_DATA="/root/ovpn-data"
    $ IP="xxx.xxx.xxx.xxx"  # 换成你的服务器的外网ip
    $ mkdir ${OVPN_DATA}
 
## 配置
    docker run -v ${OVPN_DATA}:/etc/openvpn --rm kylemanna/openvpn ovpn_genconfig -u tcp://${IP}

## 初始化
    $ docker run -v ${OVPN_DATA}:/etc/openvpn --rm -it kylemanna/openvpn ovpn_initpki

    Enter PEM pass phrase: 输入123456（你是看不见的） 
    Verifying - Enter PEM pass phrase: 输入123456（你是看不见的） 
    Common Name (eg: your user, host, or server name) [Easy-RSA CA]:回车一下 
    Enter pass phrase for /etc/openvpn/pki/private/ca.key:输入123456 

## 创建用户
  * 创建用户
    $ docker run -v ${OVPN_DATA}:/etc/openvpn --rm -it kylemanna/openvpn easyrsa build-client-full CLIENTNAME nopass
    Enter pass phrase for /etc/openvpn/pki/private/ca.key:输入123456 

  * 生成密钥
    $ docker run -v ${OVPN_DATA}:/etc/openvpn --rm kylemanna/openvpn ovpn_getclient CLIENTNAME > ${OVPN_DATA}/CLIENTNAME.ovpn

## 生成docker容器
    $ docker run --name openvpn -v ${OVPN_DATA}:/etc/openvpn -d -p 1194:1194 --privileged kylemanna/openvpn

## 注销用户
    撤销签署的证书(删除用户)

    进入docker
    $ docker exec -ti openvpn bash

    $ easyrsa revoke CLIENTNAME 
    $ easyrsa gen-crl 
    重启docker

## 配置文件参考
$ cat /etc/openvpn/server.conf 
port 1194       #openVPN端口
proto tcp       #tcp连接
dev tun         #生成tun0虚拟网卡

ca keys/ca.crt      #相关证书配置路径(可以修改为全路径/etc/openvpn/keys)
cert keys/server.crt
key keys/server.key  # This file should be kept secret
dh keys/dh2048.pem

server 10.4.82.0 255.255.255.0   #默认虚拟局域网网段，不要和实际的局域网冲突就可以
ifconfig-pool-persist ipp.txt     

push "route 10.4.82.0 255.255.255.0"    #可以通过iptables进行路由的转发
client-to-client                 #如果客户端都是用一个证书和密钥连接VPN，需要打开这个选项
duplicate-cn
keepalive 10 120
tls-auth keys/ta.key 0 # This file is secret
comp-lzo

persist-key
persist-tun

status openvpn-status.log   #状态日志路径
log-append  openvpn.log     #运行日志
verb 3                      #调试信息级别

#如果需要接入ldap，需要在server.conf下添加如下2行
plugin /usr/lib64/openvpn/plugin/lib/openvpn-auth-ldap.so "/etc/openvpn/auth/ldap.conf cn=%u"
client-cert-not-required



## 连接vpn后无法上网
* 服务端
    net.ipv4.ip_forward = 1
* 客户端配置文件添加
    route 172.21.0.0 255.255.255.0 # 只有访问这个网段走vpn
    route-nopull # 添加这一行，不从服务器拉取路由表
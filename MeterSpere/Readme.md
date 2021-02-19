[TOC]

---

## 搭建
### 在线搭建
    curl -sSL https://github.com/metersphere/metersphere/releases/latest/download/quick_start.sh | sh   
### 离线搭建
    通过官网下载包
### 安装配置
    原理实现：通过下载一个压缩包，里面可以配置安装路径，外置mysql，kafaka地址等
    安装路径：/opt/
    端口配置：通过进入到/opt/，修改yaml，配置具体的映射端口
    启动停止：通过docker-compose操作
### 访问
    地址: http://目标服务器IP地址:8081
    用户名: admin
    密码: metersphere

## 配置使用
    配置外显url、邮件、LDAP：设置-系统-系统参数设置
    配置消息通知：组织-消息设置
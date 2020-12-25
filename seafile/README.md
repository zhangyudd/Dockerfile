## 启动命令
`docker run -d -it --name seafile --restart=always -e SEAFILE_SERVER_HOSTNAME=192.168.8.102  -e SEAFILE_ADMIN_EMAIL=edgar.z@foxmail.com -e SEAFILE_ADMIN_PASSWORD=123456 -v C:\Users\Administrator\Desktop\seafileData:/shared  -p 31000:80  -p 31001:8000  -p 31002:8082  docker.seafile.top/seafileltd/seafile-pro:latest`

## 修改上传下载url
头像 - 系统管理 - 设置 - SERVICE_URL/FILE_SERVER_ROOT（宿主机的ip加端口31000）
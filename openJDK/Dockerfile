FROM alpine

LABEL maintainer="zentao Docker Maintainers <edgar.z@foxmail.com>"

ARG openJDK_VERSION=openjdk8
#setting time zone 
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk add tzdata \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && apk del tzdata

#install openjdk8
RUN apk add ${openJDK_VERSION}

FROM alpine
RUN echo "http://mirrors.aliyun.com/alpine/latest-stable/main/" > /etc/apk/repositories \
    && echo "http://mirrors.aliyun.com/alpine/latest-stable/community/" >> /etc/apk/repositories \
    && apk update

RUN apk add ansible openssh sshpass

RUN mkdir -p /etc/ansible \
    && ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa \
    && rm -rf /var/cache/apk/*
    
ADD ansible.cfg /etc/ansible/ansible.cfg
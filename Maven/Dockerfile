FROM alpine

LABEL maintainer="zentao Docker Maintainers <edgar.z@foxmail.com>"

ARG maven_version=3.6.3

#setting time zone 
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk add tzdata openjdk8 \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && apk del tzdata

RUN wget http://apache-mirror.rbc.ru/pub/apache/maven/maven-3/${maven_version}/binaries/apache-maven-${maven_version}-bin.tar.gz
RUN tar xzvf apache-maven-${maven_version}-bin.tar.gz \
	&& cp -R apache-maven-${maven_version} /usr/local/bin \
    && export PATH=apache-maven-${maven_version}/bin:$PATH \
    && export PATH=/usr/local/bin/apache-maven-${maven_version}/bin:$PATH \
    && ln -s /usr/local/bin/apache-maven-${maven_version}/bin/mvn /usr/local/bin/mvn \
    && echo $PATH
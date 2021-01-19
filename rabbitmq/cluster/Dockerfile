
FROM rabbitmq:3.6.8
MAINTAINER Edgar
ARG rabbit_Version=3.6.8
ENV RABBITMQ_USE_LONGNAME=true \
    AUTOCLUSTER_LOG_LEVEL=debug \
    AUTOCLUSTER_CLEANUP=true \
    CLEANUP_INTERVAL=60 \
    CLEANUP_WARN_ONLY=false \
    AUTOCLUSTER_TYPE=k8s \
    LANG=en_US.UTF-8
ADD https://github.com/rabbitmq/rabbitmq-autocluster/releases/download/0.10.0/autocluster-0.10.0.ez /usr/lib/rabbitmq/lib/rabbitmq_server-${rabbit_Version}/plugins/
ADD https://github.com/rabbitmq/rabbitmq-autocluster/releases/download/0.10.0/rabbitmq_aws-0.10.0.ez /usr/lib/rabbitmq/lib/rabbitmq_server-${rabbit_Version}/plugins/
RUN chmod 777 -R /usr/lib/rabbitmq/lib/rabbitmq_server-${rabbit_Version}/plugins/ \
    && rabbitmq-plugins enable --offline autocluster \
    && rabbitmq-plugins enable --offline rabbitmq_management
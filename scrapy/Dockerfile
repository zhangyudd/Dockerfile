FROM alpine as builder

LABEL maintainer="zentao Docker Maintainers <edgar.z@foxmail.com>"

ENV LANG C.UTF-8
ENV PYTHON_VERSION 3.9.0b4

RUN set -ex \ 
	&& sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
	&& apk add --no-cache --virtual .fetch-deps \
		gnupg \
		tar \
		xz \
	&& wget -O python.tar.xz "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz" \
        && mkdir -p /usr/src/python \
	&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \
	&& apk add --no-cache --virtual .build-deps  \
		bluez-dev \
		bzip2-dev \
		coreutils \
		dpkg-dev dpkg \
		expat-dev \
		findutils \
		gcc \
		gdbm-dev \
		libc-dev \
		libffi-dev \
		libnsl-dev \
		libtirpc-dev \
		linux-headers \
		make \
		ncurses-dev \
		openssl-dev \
		pax-utils \
		readline-dev \
		sqlite-dev \
		tcl-dev \
		tk \
		tk-dev \
		util-linux-dev \
		xz-dev \
		zlib-dev \
	&& apk del --no-network .fetch-deps \
        && cd /usr/src/python \
	&& ./configure --prefix=/usr/local/python \
		--build="$gnuArch" \
		--enable-loadable-sqlite-extensions \
		--enable-optimizations \
		--enable-option-checking=fatal \
		--enable-shared \
		--with-system-expat \
		--with-system-ffi \
		--without-ensurepip \
	&& make -j "$(nproc)" \
	&& make install 


FROM alpine

COPY --from=builder /usr/local/python /usr/local/python

ENV  PATH /usr/local/python/bin:$PATH
ENV PYTHON_GET_PIP_URL https://bootstrap.pypa.io/get-pip.py

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
	&& apk add --no-cache --virtual .build-deps  \
		bluez-dev \
		bzip2-dev \
		expat-dev \
		gdbm-dev \
		libc-dev \
		libffi-dev \
		libnsl-dev \
		libtirpc-dev \
		ncurses-dev \
		openssl-dev \
		readline-dev \
		sqlite-dev \
		tcl-dev \
		tk \
		tk-dev \
		util-linux-dev \
		xz-dev \
		zlib-dev \
		libxml2-dev \
		libxslt-dev \
		gcc \
	&& cp -r /usr/local/python/lib/* /usr/lib/ \
	&& cd /usr/local/python/bin \
	&& ln -s idle3 idle \
	&& ln -s pydoc3 pydoc \
	&& ln -s python3 python \
	&& ln -s python3-config python-config \
 	&&  python3 --version 
RUN set -ex; \
	\
	wget -O get-pip.py "$PYTHON_GET_PIP_URL"; \
	python get-pip.py \
	pip --version; \
	\
	find /usr/local -depth \
		\( \
			\( -type d -a \( -name test -o -name tests -o -name idle_test \) \) \
			-o \
			\( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
		\) -exec rm -rf '{}' +; \
	rm -f get-pip.py \
	&& pip install  --no-cache-dir  lxml fake-useragent -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
	&& pip install  --no-cache-dir  scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
	&& rm -rf ~/.cache/pip 
CMD ["python3"]


#!/bin/bash

# filebeat 数据清理
shijian=`date +%Y.%m.%d -d "3 days ago"`
curl -XDELETE "127.0.0.1:9200/logstash-${shijian}"

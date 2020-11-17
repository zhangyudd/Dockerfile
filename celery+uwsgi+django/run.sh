uwsgi --ini  uwsgi.ini --chdir  /friends_ios/fridens --daemonize  /friends_ios/fridens/uwsgi.log 
nohup celery -A fridens worker > friends_worker.log 2>&1  &
sleep 0.5
nohup celery -A fridens beat > friends_beat.log 2>&1  &
nginx
tail -f  /friends_ios/fridens/uwsgi.log

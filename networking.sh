#!/bin/bash


LOG=/var/log/networking.log
DATE=`date '+%Y.%m.%d %H:%M:%S'`
if [ ! -f $LOG ]
then
  echo "$DATE **** Первый запуск скрипта **** " >> $LOG
fi
prederror="$(tail -n 1 $LOG | grep -icE 'отсутствует')"

# пинг google.com с последующей проверкой на ошибки
errorscount="$(ping -c 3 google.com 2<&1| grep -icE 'unknown|expired|unreachable|time out')"
if [ "$errorscount" != 0 ]; then
  # и пишем в лог время разрыва соединения
  echo "$DATE * Cвязь отсутствует. Перезапуск " >> $LOG
  service networking restart
elif [ "$prederror" != 0 ]; then
  echo "$DATE * Cвязь востановленна!" >> $LOG
fi

cat $LOG


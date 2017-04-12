#!/bin/bash


LOG=/var/log/networking.log
DATE=`date '+%Y.%m.%d %H:%M:%S'`
if [ ! -f $LOG ]
then
  echo "$DATE **** Первый запуск скрипта **** " >> $LOG
fi

if ping -q -c 1 -W 1 google.com >/dev/null; then
  prederror="$(tail -n 1 $LOG | grep -icE 'down')"
  if [ "$prederror" != 0 ]; then
    echo "$DATE The network is up $prederror" >> $LOG
  fi
else
  echo "$DATE The network is down" >> $LOG
  ifconfig wlan0 down
  ifconfig wlan0 up
fi


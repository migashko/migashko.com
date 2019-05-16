#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: UTF-8

import requests
import vk_api
import random

vk_session = vk_api.VkApi(token='451ff58be639c45f9ae91b5b8ad53814a82d0852a907b04de52091a76623b5d2e84ffb16b24d621a39bd6')
from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
  if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
    if event.from_user: 
      vk.messages.send(
        user_id=event.user_id,
        message='нет',
        random_id=random.random()
      )


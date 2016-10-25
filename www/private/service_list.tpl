<?python from genshi import HTML ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ru" lang="ru"
      xmlns:xi="http://www.w3.org/2001/XInclude"
      xmlns:py="http://genshi.edgewall.org/">
  <head>
    <title>Список сервисов</title>
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
  </head>
  <body class="index">
    <div py:if="'services' in g" >
      <div class="service" py:for="srv in g.services">
        ${srv.name} <b>${srv.status}</b> 
        <div py:if="'start' in srv" >
          <a href="${srv.start}">Запустить</a>
        </div>
        <div py:if="'stop' in srv" >
          <a href="${srv.stop}">Остановить</a>
        </div>
        <div py:if="'restart' in srv" >
          <a href="${srv.restart}">Перезапустить</a>
        </div>
        
      </div>
    </div>
  </body>
</html>

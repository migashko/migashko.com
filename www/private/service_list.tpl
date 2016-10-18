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
    <div id="header">
    </div>
    <p>Welcome!</p>
      <ol py:if="services">
        <li py:for="srv in services">
          ${srv.name} <b>${srv.status}</b>
        </li>
      </ol>
    <div id="footer">
      <hr />
      <p class="legalese">© 2007 Edgewall Software</p>
    </div>
  </body>
</html>

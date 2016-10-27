<?python from genshi import HTML ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ru" lang="ru"
      xmlns:xi="http://www.w3.org/2001/XInclude"
      xmlns:py="http://genshi.edgewall.org/">
  <head>
    <title>Список сервисов</title>
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
    <style type="text/css">
        .result{
          /*vertical-align: middle;*/
          font-size: 32px;
          font-family: Arial, Verdana, Helvetica, sans-serif;
        }

        .img-block{
          display: block;
          margin-left: auto;
          margin-right: auto;
          border: 10px;
          border-color: black 
        }
    </style>
  </head>
  <body class="index">
    <div py:if="'result' in g" >
      <div class="result">
        ${g.result}
      </div>
    </div>
    <!-- <a href="service_list.py">Продолжить</a> 
    <div class="back"> -->
      <a href="service_list.py"><img class="img-block" src="back.png" width="256px" height="256px" alt="Back"></img></a>
    <!-- </div> -->

  </body>
</html>

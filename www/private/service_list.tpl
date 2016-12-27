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
        .service{
          display: table;
          height: 160px
        }

        .service-status{
          display: table-cell;
          vertical-align: middle;
          width:96px;
         
        }

        .service-status img{
           padding-left: 24px
        }

        .service-ico{
          display: table-cell;
          vertical-align: middle;
          width:96px;
	  height:96px;
        }
        .service-name{
          display: table-cell;
          vertical-align: middle;
          font-size: 64px;
          font-family: Arial, Verdana, Helvetica, sans-serif;
          width:420px;
          padding-left: 32px;
        }
        .service-cmd{
          display: table-cell;
          vertical-align: middle;
          width:128px;
          padding-left: 16px;
        }
        #reload
        {
          display: block;
          height : 128px;
          width:128px;
          /*padding-left: 314px;*/:
        }
        #reload-image
        {
          height : 128px;
          width:128px;
          background: url(reload.png) 100% 100% no-repeat; /* Добавляем фон */
          background-size: 128px; /* Масштабируем фон */
        }
        .img-block{
          display: inline;
          /*padding-right: 32px;*/

          margin-left: auto;
          margin-right: auto;
          border: 10px;
          border-color: black 
        }
        
    </style>
  </head>
  <body class="index">
    <div py:if="'services' in g" >
      <div class="service" py:for="srv in g.services">
        <div class="service-status">        
          <img width="48px" src="${srv.status}.png"></img>
          <!-- <b>${srv.status}</b> --> 
        </div>
        <div class="service-ico" >
          <img src="${srv.name}.png" width="96px" height="96px"></img>
        </div>
        <div class="service-name">
          ${srv.name} 
        </div>
        <div class="service-cmd" py:if="'restart' in srv" >
          <a href="${srv.restart}"><img src="restart.png"></img></a>
        </div>
        <div class="service-cmd" py:if="'start' in srv" >
          <a href="${srv.start}"><img src="start.png"></img></a>
        </div>
        <div class="service-cmd" py:if="'stop' in srv" >
          <a href="${srv.stop}"><img src="stop.png"></img></a>
        </div>
      </div>
    </div>
    <div id="reload">
      <a id="reload-a" href="service_list.py">
        <div id="reload-image">
        </div>
      </a>
    </div>
    <a href="index.html"><img class="img-block" src="back.png" width="128px" height="128px" alt="Back"></img></a>
  </body>
</html>

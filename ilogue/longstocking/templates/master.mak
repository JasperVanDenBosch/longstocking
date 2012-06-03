<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>longstocking</title>
    <meta http-equiv="Content-type" content="text/html;charset=UTF-8" />
    <link rel="stylesheet" type="text/css" 
        href="${request.static_url('ilogue.longstocking:static/longstocking.css')}" />
    <meta http-equiv="content-language" content="en" />

</head>
<body>
    <div id="header" class="container">
        <div class="centerstage">
            <a class="nav" href="${request.resource_url(request.root)}">index</a>
        </div>
    </div>
    <div id="content" class="container">
        <div class="centerstage">
            ${self.body()}
        </div>
    </div>
    <div id="footer" class="container">
        <div class="centerstage">
            <span class="understated">© 2012 ilogue</span>
        </div>
    </div>
</body>
</html>



<%inherit file="master.mak" />



<h4>${package.name}</h4>

<ul>
% for a in package.artifacts:
    <li><a href="${request.resource_url(a)}">${a.name}</a></li>
% endfor
</ul>




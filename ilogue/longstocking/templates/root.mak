<%inherit file="master.mak" />

<ul>
% for f in root.files:
    <li>${f}</li>
% endfor
</ul>




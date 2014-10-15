---
layout: page
title: Usuarios por puesto
permalink: /rspi/usuarios_puesto.html
---
<h1 class="page-header">Usuarios por puesto</h1>

<div style="width: 1000px; height: 500px;"
	 data-htsql="/users_puesto{nombre,count(auth_user)-}?count(auth_user)>2"
	 data-widget="chart"
	 data-type="bar"
	 data-yint="true"
	 data-x-vertical="true"
         data-show-title="false"
         data-show-title="false">
</div>


<h2 class="sub-header">Usuarios</h2>
<div class="table-responsive">
  <table class="table table-striped"
	 data-htsql="/users_puesto{nombre,count(auth_user)- :as 'Usuarios'}?count(auth_user)>2">
  </table>
</div>

---
layout: page
title: Avance tesis
permalink: /rspi/tesis_avance.html
---
<h1 class="page-header">Avance tesis</h1>

<div style="width: 1000px; height: 500px;"
	 data-htsql="/protocolos_tesis{apellidos_estudiante,grado_avance}"
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
	 data-htsql="/protocolos_tesis{apellidos_estudiante :as 'Autor', grado_avance- :as 'Grado Avance'}">
  </table>
</div>

---
layout: page
title: Destino de Recursos
permalink: /rspi/proyectos_costos_sunburst.html
---
<h1 class="page-header">Destino de Recursos</h1>

<div style="width: 800px; height: 600px;"
	 data-htsql="/protocolos_gasto{desc:=descripcion}^desc {desc,sum(protocolos_gasto.monto) :as monto-}.limit(20)"
	 data-widget="chart"
	 data-type="bar"
	 data-yint="true"
	 data-x-vertical="true"
     data-show-title="false"
	 data-title="Destino de recursos">
</div>


<h2 class="sub-header">Recursos</h2>
<div class="table-responsive">
  <table class="table table-striped"
	 data-htsql="/protocolos_gasto{desc:=descripcion}^desc {desc
	 :as 'descripción',sum(protocolos_gasto.monto) :as monto-}">
  </table>
</div>

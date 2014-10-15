---
layout: page
title: Colaboración con otras Instituciones
permalink: /rspi/colaboradores.html
---

<h1 class="page-header">Colaboración con otras Instituciones</h1>

<div style="width: 800px; height: 500px;"
	 data-htsql="/protocolos_dependencia{siglas,colaboradores:=count(protocolos_otropersonalparticipante)-}?colaboradores>=2"
	 data-widget="chart"
	 data-type="bar"
	 data-yint="true"
	 data-x-vertical="true"
     data-show-title="false"
	 data-title="Colaboradores externos">
</div>


<h2 class="sub-header">Colaboradores por Institución</h2>
<div class="table-responsive">
  <table class="table table-striped"
	 data-htsql="/protocolos_dependencia{siglas :as 'institución',
	 colaboradores:=count(protocolos_otropersonalparticipante)-}?colaboradores>0">

  </table>
</div>

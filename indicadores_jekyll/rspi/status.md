---
layout: page
title: Status
permalink: /rspi/status.html
---
<h1 class="page-header">Status</h1>


<div style="width: 500px; height: 350px;"
     data-htsql="/protocolos_proyecto{estatus:=status}^estatus {estatus,count(protocolos_proyecto)}"
     data-widget="chart"
     data-type="pie"
     data-show-title="false">
</div>

<h2 class="sub-header">Proyectos por su status</h2>
<div class="table-responsive">
  <table class="table table-striped"
         data-htsql="/protocolos_proyecto{estatus:=status}^estatus
         {estatus :as 'status', count(protocolos_proyecto) :as 'cantidad'}">
  </table>
</div>

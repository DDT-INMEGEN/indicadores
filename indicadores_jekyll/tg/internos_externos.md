---
layout: page
title: Estados de tickets
permalink: /tg/internos_externos.html
---

<h1 class="page-header">
  Proporción de servicios internos vs. externos</h1>

<div style="width: 500px; height: 350px;"
     data-htsql="/helpdesk_ticket{mitipo:=tipo.tipo}^mitipo {mitipo,count(helpdesk_ticket)}"
     data-widget="chart"
     data-type="pie"
     data-show-title="false"
     data-title="Proporción de servicios internos vs. externos">
</div>


<div class="table-responsive">
<table class="table table-striped"
         data-htsql="/helpdesk_ticket{mitipo:=tipo.tipo}^mitipo
         {mitipo :as tipo, count(helpdesk_ticket) :as tickets}">
</table>
</div>

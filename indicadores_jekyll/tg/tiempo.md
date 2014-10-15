---
layout: page
title: Dinámica de Tickets Atendidos
permalink: /tg/tiempo.html
---
<h1 class="page-header">Dinámica de Tickets Atendidos</h1>
<div style="width: 800px; height: 350px;"
	 data-widget="chart"
	 data-type="line"
	 data-yint="true"
	 data-title="Tickets al paso del tiempo"
         data-show-title="false"
	 data-htsql="/helpdesk_ticket^fecha_creacion {fecha_creacion-, count(helpdesk_ticket) :as tickets}.limit(50)">
</div>


<div class="table-responsive">
  <table class="table table-striped"
	 data-htsql="/helpdesk_ticket^fecha_creacion {fecha_creacion-
	 :as fecha, count(helpdesk_ticket) :as tickets}.limit(50)">
  </table>
</div>

---
layout: page
tipo: ti
title: Dinámica de Tickets Atendidos
permalink: /ti/dinamica.html
---

<h1 class="page-header">Dinámica de Tickets Atendidos</h1>
<div style="width: 800px; height: 350px;"
	 data-widget="chart"
	 data-type="line"
	 data-yint="true"
	 data-title="Tickets al paso del tiempo"
         data-show-title="false"
	 data-htsql="/hesk_tickets{epa:=date(dt)}^epa {epa-,count(hesk_tickets) :as 'tickets'}.limit(50)">
</div>


<div class="table-responsive">
  <table class="table table-striped"
	 data-htsql="/hesk_tickets{epa:=date(dt)}^epa {epa- :as fecha,count(hesk_tickets) :as 'tickets'}.limit(50)">
  </table>
</div>

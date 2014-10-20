---
layout: page
title: Estados de tickets
aguas: cave canem
permalink: /tg/estados.html
---

<h1 class="page-header">Estados de tickets</h1>

<div style="width: 500px; height: 350px;"
     data-htsql="/helpdesk_estadoticket{estado,count(helpdesk_ticket) :as tickets-}"
     data-widget="chart"
     data-type="bar"
     data-show-title="false"
     data-title="Tickets por sus estados">
</div>


<div class="table-responsive">
  <table class="table table-striped"
	 data-htsql="/helpdesk_estadoticket{estado,count(helpdesk_ticket)
	 :as tickets-}">
  </table>
</div>

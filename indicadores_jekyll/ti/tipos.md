---
layout: page
tipo: ti
title: Categorías de tickets
permalink: /ti/tipos.html
---

<h1 class="page-header">Categorías de tickets</h1>

<div style="width: 500px; height: 350px;"
	 data-htsql="/hesk_tickets^custom3 {custom3,count(hesk_tickets)}"
	 data-widget="chart"
	 data-type="pie"
	 data-title="Proporciones de tipos de ticket">
    </div>


<div class="table-responsive">
  <table class="table table-striped"
	 data-htsql="/hesk_tickets^custom3 {custom3 :as 'categoría',
	 count(hesk_tickets) :as tickets-}">
  </table>
</div>

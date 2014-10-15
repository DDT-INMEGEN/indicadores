---
layout: page
title: Volumen de impresión
permalink: /admin/impresora_dinamica.html
---

<h1 class="page-header">Volumen de Impresión</h1>


<select id="ubicacion"
        data-htsql="/impresoras{ubicacion}^ubicacion">
</select> 

<div style="width: 800px; height: 350px;"
	 data-widget="chart"
	 data-type="line"
	 data-yint="true"
	 data-title="Volumen de Impresión"
     data-show-title="false"
	 data-htsql="/impresoras_volumen{fecha}?impresora.ubicacion=$ubicacion^fecha {fecha,sum(impresoras_volumen.volumen) :as impresiones}"
     data-ref="ubicacion">
</div>

<div class="table-responsive">
  <table class="table table-striped"
	 data-htsql="/impresoras_volumen{fecha}?impresora.ubicacion=$ubicacion^fecha {fecha-,sum(impresoras_volumen.volumen) :as impresiones}?sum(impresoras_volumen.volumen)>0"
         data-ref="ubicacion">
  </table>
</div>
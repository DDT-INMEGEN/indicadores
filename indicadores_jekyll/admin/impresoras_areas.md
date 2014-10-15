---
layout: page
title: Impresión por Áreas
permalink: /admin/impresoras_areas.html
---
<h1 class="page-header">Impresión por áreas</h1>
<select id="fecha_elegida"
        data-htsql="/impresoras_volumen{fecha}^fecha {fecha-}">
</select>

<div class="table-responsive">
    <table class="table table-striped"
        data-htsql="/impresoras_volumen{impresora.ubicacion,volumen}?fecha=$fecha_elegida^impresora.ubicacion{ubicacion,sum(impresoras_volumen.volumen) :as impresiones}"
        data-ref="fecha_elegida">

    </table>
    
</div>
<div style="width: 800px; height: 350px;"
    data-widget="chart"
    data-type="pie"
    data-title="Volumen de Impresión por áreas"
    data-show-title="false"
    data-x-vertical="true"
    data-htsql="/impresoras_volumen{impresora.ubicacion,volumen}?fecha=$fecha_elegida^impresora.ubicacion {ubicacion,sum(impresoras_volumen.volumen)}.limit(10)"
    data-ref="fecha_elegida">
</div>

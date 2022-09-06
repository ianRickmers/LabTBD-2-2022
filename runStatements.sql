-- 1) horario con menos citas durante el día por peluquería, identificando la comuna
select p."nombre", h."horaInicio", minimo
from (select  * ,min(s1.total) over(partition by s1.idPelu) as minimo 
from(select distinct clp."idPeluqueria" as idPelu, c."idHorario" as idHorario, count(*) as total
    from public.cita as c
    inner join public.cliente_pelu as clp ON clp."idCita" = c.id
    group by clp."idPeluqueria", c."idHorario"
    order by clp."idPeluqueria" asc, total asc) as s1) as s2
inner join public.peluqueria as p ON p.id = s2.idPelu
inner join public.horario as h ON h.id = s2.idHorario
where s2.minimo=s2.total;







-- 2) lista de clientes que gastan más dinero mensual por peluquería, indicando comuna
-- del cliente y de peluquería, además de cuanto gasto
Select s4.nombre, s4.apellido, pl.nombre as peluqueria, s4.mes, s4."ano", s4.comuna_cliente, cm2.nombre as comuna_pelu, s4.total  
from (Select cl.nombre, cl.apellido, s3."idPeluqueria", s3.mes, s3."ano", cm.nombre as comuna_cliente, s3.total 
	from(select s2."idPeluqueria", s2."idCliente", s2.mes, s2.ano, s2.total
		from (select *, max(s1.total) over(partition by s1."idPeluqueria", s1.mes, s1.ano)
			from(select  clp."idPeluqueria", clp."idCliente", c.mes, c."ano", sum(p.total) as total
				from public.cita as c 
				inner join public.cliente_pelu as clp on clp."idCita" = c.id 
			inner join public.detalle as d on d.id = c."idDetalle" 
			inner join public.pago as p on p.id = d."idPago" 
			group by clp."idPeluqueria", clp."idCliente", c.mes, c."ano" 
			order by clp."idPeluqueria" asc, c.mes asc, c."ano" asc, total desc) as s1) as s2
		where s2.total = s2.max) as s3 
	inner join public.cliente as cl on cl.rut = s3."idCliente" 
	inner join public.comuna as cm on cm.id = cl."idComuna") as s4 
inner join public.peluqueria as pl on pl.id = s4."idPeluqueria" 
inner join public.comuna as cm2 on cm2.id = pl."idComuna";






-- 3) lista de peluqueros que ha ganado más por mes los últimos 3 años, esto por
-- peluquería
select s1."idPeluqueria", s1.mes, s1."ano", s1."idEmpleado",s1.monto
from (
    select s.mes, e."idPeluqueria", s."ano", s."idEmpleado", s.monto, max(s.monto) over(partition by e."idPeluqueria") as maximo
    from public.sueldo as s
    inner join public.empleado as e on e.rut = s."idEmpleado"
    order by s.mes asc, e."idPeluqueria" asc, s."ano" asc, s.monto desc) as s1
inner join public.peluqueria as p on s1."idPeluqueria" = p.id
where s1.monto = s1.maximo;







-- 4) lista de clientes hombres que se cortan el pelo y la barba
create view clCoHombre as (select cp."idCliente", sd."idServicio" 
from cliente_pelu as cp, cita as ci, detalle as d, servicio_detalle as sd 
where cp."idCita"=ci.id 
and ci.id=d.id and d.id=sd."idDetalle" 
and sd."idServicio"='1');

create view clCoBarba as (select cp."idCliente", sd."idServicio" 
from cliente_pelu as cp, cita as ci, detalle as d, servicio_detalle as sd 
where cp."idCita"=ci.id 
and ci.id=d.id and d.id=sd."idDetalle" 
and sd."idServicio"='4');

select distinct cliente from cliente, clCoHombre, clCoBarba 
where clCoHombre."idCliente"=clCoBarba."idCliente" and 
cliente.rut=clCoHombre."idCliente" and cliente.genero = 'M';







-- 5) lista de clientes que se tiñen el pelo, indicando la comuna del cliente, la peluquería
-- donde se atendió y el valor que pagó
SELECT distinct cliente.nombre, comuna.nombre as Nombre_Comuna, pago.total, peluqueria.nombre as Peluqueria, servicio.tipo 
FROM cliente, comuna, cliente_pelu, cita, detalle, servicio, servicio_detalle, pago, peluqueria 
WHERE servicio.tipo = 'TenirPelo' and
	servicio."id" = servicio_detalle."idServicio" and 
	servicio_detalle."idDetalle" = detalle."id" and 
	detalle."idPago" = pago."id" and 
	detalle."id" = cita."idDetalle" and 
	cita."id" = cliente_pelu."idCita" and 
	cliente_pelu."idCliente" = cliente.rut and 
	cliente."idComuna" = comuna."id" and 
	cliente_pelu."idPeluqueria" = peluqueria."id"; 







-- 6) identificar el horario más concurrido por peluquería durante el 2018 y 2029,
-- desagregados por mes
create view pyh as select distinct cp."idPeluqueria", p.nombre, c."idHorario", c."mes", c."ano",
COUNT(c."idHorario") OVER(PARTITION BY p.id, c."idHorario", c."ano", c."mes") AS CountOfOrders 
from peluqueria as p, cliente_pelu as cp, cita as c,
horario as h
where p.id=cp."idPeluqueria" and cp."idCita"=c.id and
c."idHorario"=h.id and c."ano">2017 and c."ano"<2030
order by cp."idPeluqueria", CountOfOrders desc, c."ano", c."mes", c."idHorario";


select distinct s."idPeluqueria", s.nombre, s.CountOfOrders, s."idHorario", s."ano", s."mes"
from pyh s
inner join(select distinct pyh."nombre", pyh."idPeluqueria", max(pyh.CountOfOrders) as maximo
FROM pyh
group by pyh.nombre, pyh."idPeluqueria"
order by pyh.nombre, maximo desc) z
on s.nombre=z.nombre and s.CountOfOrders=z.maximo
order by s."idPeluqueria", s.CountOfOrders, s.CountOfOrders, s."ano", s."mes"







-- 7) identificar al cliente que ha tenido las citas más largas por peluquería, por mes
CREATE VIEW t2 as 
(SELECT p.id as idPelu, p."nombre" as peluquería, c."ano", c."mes", cl."nombre" as nombre_cliente, d."duracion" as duracion_cita 
FROM cita as c, cliente as cl, cliente_pelu as clp, detalle as d, peluqueria as p 
WHERE (cl."rut" = clp."idCliente") and 
      (clp."idCita" = c."id") and 
      (c."idDetalle" = d."id") and 
      (clp."idPeluqueria" = p."id") 
ORDER BY p."nombre" asc, c."ano", c."mes" asc, d."duracion" desc);

select distinct t2.idPelu, t2.peluquería, t2.ano, t2.mes, t2.nombre_cliente, t2.duracion_cita
from t2
inner join(select distinct t2.peluquería, t2.idPelu, max(t2.duracion_cita) over(partition by t2.peluquería,t2."ano", t2."mes") as maximo
FROM t2
group by t2.peluquería, t2.idPelu, t2.duracion_cita,t2."ano", t2."mes"
order by t2.peluquería, maximo desc) z
on t2.peluquería=z.peluquería and t2.duracion_cita=z.maximo
order by t2.idPelu,t2."ano" , t2."mes", t2.duracion_cita







-- 8) identificar servicio más caro por peluquería
select s1."idPeluqueria", p.nombre as peluqueria, s1.tipo, s1.monto 
from (select sp."idPeluqueria", s.tipo, p.monto, max(p.monto) over(partition by sp."idPeluqueria") as maximo 
	from public.servicio_precio as sp 
	inner join public.precio as p on p.id = sp."idPrecio" 
	inner join public.servicio as s on s.id = sp."idServicio" 
	order by sp."idPeluqueria" asc, p.monto desc) as s1 
inner join public.peluqueria as p on s1."idPeluqueria" = p.id 
where s1.monto = s1.maximo; 







-- 9) identificar al peluquero que ha trabajado más por mes durante el 2021
select s2.mes, e.nombre, e.apellido, s2.total
from(select *, max(s1.total) over(partition by s1.mes) as maximo
	from (select c.mes, c."idPeluquero", sum(d.duracion) as total
		from public.cita as c 
		inner join public.detalle as d on d.id = c."idDetalle" 
		where c."ano" = 2021 
		group by c.mes, c."idPeluquero") as s1) as s2
inner join public.peluquero as p on p.id = s2."idPeluquero"
inner join public.empleado as e on e.rut = p."idEmpleado"
where s2.total = s2.maximo
order by s2.mes asc, s2.total desc;







-- 10) identificar lista de totales por comuna, cantidad de peluquerías, cantidad de clientes
-- residentes en la comuna
create view v1 as 
SELECT cm.nombre, COALESCE(s1.cant_cliente, 0) AS cant_cliente 
FROM ( SELECT c."idComuna", count(*) AS cant_cliente 
        FROM cliente c 
        GROUP BY c."idComuna") as s1 
RIGHT JOIN comuna cm ON cm.id = s1."idComuna";

create view v2 as  
SELECT cm.nombre, COALESCE(s2.cant_pelu, 0) AS cant_pelu 
FROM ( SELECT p."idComuna", count(*) AS cant_pelu 
        FROM peluqueria p 
        GROUP BY p."idComuna") as s2 
RIGHT JOIN comuna cm ON cm.id = s2."idComuna";

SELECT v1.nombre, cant_cliente, cant_pelu 
FROM public.v2, public.v1 
where v1.nombre = v2.nombre;
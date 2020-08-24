/* Valor vendido por contato*/
SELECT deals."contactsId" , contacts."contactsName", sum ("dealsPrice")
from deals, contacts
where deals."contactsId" = contacts." contactsId"
group by deals."contactsId",contacts."contactsName"
order by deals."contactsId"
/*Valor vendido por mes*/
SELECT cast(extract(month from (TO_DATE("dealsDateCreated", 'MM/DD/YYYY'))) as integer) as monthid , TO_CHAR(TO_DATE("dealsDateCreated", 'MM/DD/YYYY'), 'Month') AS "Month",sum("dealsPrice")
from deals
group by "Month", monthid
order by monthid
/*Porcentagem por setor*/
select ca."sector",round(sum ("dealsPrice")/(select sum("dealsPrice") from deals),3) as porcentagem
from deals join (select co."companiesId", "sector"
				 from companies as co join sectors as se on co."sectorKey"=se."sectorKey") as ca on deals."companiesId"=ca."companiesId"
group by ca."sector"
order by porcentagem desc
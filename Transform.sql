/* Valor vendido por contato*/
SELECT deals."contactsId" , contacts."contactsName", sum ("dealsPrice")
from deals, contacts
where deals."contactsId" = contacts." contactsId"
group by deals."contactsId",contacts."contactsName"
order by deals."contactsId"
/*Valor vendido por mes*/

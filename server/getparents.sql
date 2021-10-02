with recursive getparents  as (
	select 
		cc.id,
		cc.author_id, 
		cc."text" ,
		cc.parent_id 
	from colibri_colibri cc 
	where cc.id =3
	union  all 
	select 
	cc2.id ,
	cc2.author_id, 
	cc2."text" ,
	cc2.parent_id 
	from colibri_colibri cc2
	inner join getparents gp on gp.parent_id = cc2.id
	
)select  * from getparents
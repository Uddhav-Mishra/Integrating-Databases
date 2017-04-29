alter procedure total 
as
declare @n1 nchar(50);
declare @n2 nchar(50);
declare @n3 nchar(50);
declare @n4 nchar(50);
declare @n5 int ;
declare @n6 nchar(50);
   
declare c1 cursor static for select dab_name,table_name,price,author from ANS.dbo.tb1;
open c1;
if @@cursor_rows>0
begin
fetch next from c1 into @n1,@n2,@n3,@n4
while @@Fetch_status = 0
begin
exec('declare c2 cursor static for select '+ @n3+','+@n4+' from '+@n1+'.dbo.'+@n2);
open c2
if @@cursor_rows>0
begin
fetch next from c2 into @n5,@n6
while @@Fetch_status = 0
begin
if @n5>200 print(@n6)
fetch next from c2 into @n5,@n6
end
end
close c2
deallocate c2
fetch next from c1 into @n1,@n2,@n3,@n4
end
end
close c1
deallocate c1
set nocount off
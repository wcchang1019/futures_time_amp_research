input:
	len(5);
variable:
	count(0);

condition1 = True;
for count = 0 to len*2-1 begin
	if low[len] > low[count] then begin
		condition1 = False;
		break;
	end;
end;

condition2 = True;
for count = 0 to len*2-1 begin
	if high[len] < high[count] then begin
		condition2 = False;
		break;
	end;
end;

if condition1 then TL_New(date[len],time[len],low[len],date,time,low[len]);
if condition2 then TL_New(date[len],time[len],high[len],date,time,high[len]);

variable:
	pre_date(0), pre_price(0), pre_kbar_num(0), pre_type(0),
	now_date(0), now_price(0), now_kbar_num(0), now_type(0);
if condition1 or condition2 then begin
	now_kbar_num = currentbar[len];
	now_date = date[len];
	if condition1 then begin
		now_price = low[len];
		now_type = -1;
	end;
	if condition2 then begin
		now_price = high[len];
		now_type = 1;
	end;
	value1 = 0;
	if now_type = 1 and pre_type = -1 then value1 = 1;
	if now_type = -1 and pre_type = 1 then value1 = -1;
	print(pre_date, ",", now_date, ",", value1, ",", now_kbar_num-pre_kbar_num, ",", (now_price-pre_price));
	pre_kbar_num = now_kbar_num;
	pre_price = now_price;
	pre_type = now_type;
	pre_date = now_date;
end;


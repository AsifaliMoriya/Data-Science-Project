#1. Import Data from table Grocery_Sales using the provided CSV File. 


#2. Write an SQL query to show all Item_Identifier.
select item_identifier from grocery_table;


#3. Write an SQL query to show count of total Item_Identifier. 
select count(item_identifier) from grocery_table;


#4. Write an SQL query to show maximum Item Weight. 
select max(item_weight) from grocery_table;


#5. Write an SQL query to show minimum Item Weight. 
select min(item_weight) from grocery_table;


#6. Write an SQL query to show average Item_Weight. 
select avg(item_weight) from grocery_table;


#7. Write an SQL query to show count of Item_Fat_Content WHERE Item_Fat_Content is Low Fat.
select count(item_fat_content) from grocery_table where item_fat_content = 'low fat';


#8. Write an SQL query to show count of Item_Fat_Content WHERE Item_Fat_Content is Regular. 
select count(item_fat_content) from grocery_table where item_fat_content = 'Regular';


#9. Write an SQL query to show maximum Item_MRP. 
select max(item_mrp) from grocery_table;


#10. Write an SQL query to show minimum Item_MRP.
select min(item_mrp) from grocery_table;


#11. Write an SQL query to show Item_Identifier , Item_Fat_Content ,Item_Type, Item_MRP whose Item_MRP is greater than 200. 
select item_identifier,item_fat_content,item_type,item_mrp from grocery_table where item_mrp > 200;


#12. Write an SQL query to show maximum Item_MRP WHERE Item_Fat_Content is Low Fat.
select max(item_mrp) from grocery_table where item_fat_content = 'low fat';


#13. Write an SQL query to show minimum Item_MRP whose Item_Fat_Content is Low Fat.
select min(item_mrp) from grocery_table where item_fat_content = 'low fat';


#14. Write an SQL query to show ALL DATA WHERE item MRP is BETWEEN 50 to 100.
select * from grocery_table where item_mrp between 50 and 100;


#15. Write an SQL query to show ALL UNIQUE value of Item_Fat_Content.
select distinct item_fat_content from grocery_table;


#16. Write an SQL query to show ALL UNIQUE value of Item_Type.
select distinct item_type from grocery_table;


#17. Write an SQL query to show ALL DATA in descending ORDER by Item MRP.
select * from grocery_table order by item_mrp desc;


#18. Write an SQL query to show ALL DATA in ascending ORDER by Item_Outlet_Sales.
select * from grocery_table order by item_outlet_sales asc;


#19. Write an SQL query to show ALL DATA in ascending by Item_Type.
select * from grocery_table order by item_type asc;


#20. Write an SQL query to show DATA of item_type dairy & Meat.
select * from grocery_table where item_type in ('dairy','meat');


#21. Write an SQL query to show ALL UNIQUE value of Outlet_Size.
select distinct outlet_size from grocery_table;


#22. Write an SQL query to show ALL UNIQUE value of Outlet_Location_Type.
select distinct outlet_location_type from grocery_table;


#23. Write an SQL query to show ALL UNIQUE value of Outlet_Type.
select distinct outlet_type from grocery_table;


#24. Write an SQL query to show count of number of items by Item_Type and order it in descending order.
select item_type, count(item_type) total_items from grocery_table group by item_type order by item_type desc;


#25. Write an SQL query to show count of number of items by Outlet_Size and ordered it in ascending order.
select outlet_size, count(outlet_size) total_outlet  from grocery_table group by outlet_size order by outlet_size asc;


#26. Write an SQL query to show count of number of items by Outlet_Type and ordered it in descending order.
select outlet_type, count(outlet_type) total_outlet from grocery_table group by outlet_type order by outlet_type desc;


#27. Write an SQL query to show count of items by Outlet_Location_Type and order it in descending order.
select outlet_Location_Type, count(outlet_Location_Type) total_outlet  from grocery_table group by outlet_Location_Type order by outlet_Location_Type desc;


#28. Write an SQL query to show maximum MRP by Item_Type
select item_type, max(item_mrp) max_mrp from grocery_table group by item_type;


#29. Write an SQL query to show minimum MRP by Item_Type
select item_type, min(item_mrp) min_mrp from grocery_table group by item_type;


#30. Write an SQL query to show minimum MRP by Outlet_Establishment_Year and order it in descending order.
select outlet_establishment_year, min(item_mrp) min_mrp from grocery_table group by outlet_establishment_year order by outlet_establishment_year desc;


#31. Write an SQL query to show maximum MRP by Outlet_Establishment_Year and order it in descending order.
select outlet_establishment_year, max(item_mrp) max_mrp from grocery_table group by outlet_establishment_year order by outlet_establishment_year desc;


#32. Write an SQL query to show average MRP by Outlet_Size and order it in descending order. 
select outlet_size, avg(item_mrp) avg_mrp  from grocery_table group by outlet_size order by outlet_size desc;


#33. Write an SQL query to Average MRP by Outlet_Type and ordered in ascending order.
select outlet_type, avg(item_mrp) avg_mrp from grocery_table group by outlet_type order by outlet_type asc;


#34. Write an SQL query to show maximum MRP by Outlet_Type.
select outlet_type,max(item_mrp) max_mrp from grocery_table group by outlet_type;


#35. Write an SQL query to show maximum Item_Weight by Item_Type.
select item_type, max(item_weight) max_weight from grocery_table group by item_type;


#36. Write an SQL query to show maximum Item_Weight by Outlet_Establishment_Year.
select Outlet_Establishment_Year, max(item_weight) max_weight from grocery_table group by Outlet_Establishment_Year;


#37. Write an SQL query to show minimum Item_Weight by Outlet_Type.
select outlet_type, min(item_weight) min_weight from grocery_table group by outlet_type;


#38. Write an SQL query to show average Item_Weight by Outlet_Location_Type and arrange it by descending order.
select outlet_location_type as location, avg(item_weight) avg_weight from grocery_table group by outlet_location_type order by outlet_location_type desc;


#39. Write an SQL query to show maximum Item_Outlet_Sales by Item_Type.
select item_type, max(Item_Outlet_Sales) max_sales from grocery_table group by Item_type;


#40. Write an SQL query to show minimum Item_Outlet_Sales by Item_Type.
select item_type, min(Item_Outlet_Sales) min_sales from grocery_table group by Item_type;


#41. Write an SQL query to show minimum Item_Outlet_Sales by Outlet_Establishment_Year.
select Outlet_Establishment_Year as year , min(Item_Outlet_Sales) min_sales from grocery_table group by Outlet_Establishment_Year;


#42. Write an SQL query to show maximum Item_Outlet_Sales by Outlet_Establishment_Year and order it by descending order.
select Outlet_Establishment_Year as year , max(Item_Outlet_Sales) max_sales from grocery_table group by Outlet_Establishment_Year order by Outlet_Establishment_Year desc;


#43. Write an SQL query to show average Item_Outlet_Sales by Outlet_Size and order it by descending order.
select outlet_size, avg(item_outlet_sales) avg_sales from grocery_table group by outlet_size order by outlet_size desc;


#44. Write an SQL query to show average Item_Outlet_Sales by Outlet_Type.
select outlet_type, avg(item_outlet_sales) avg_sales from grocery_table group by outlet_type;


#45. Write an SQL query to show maximum Item_Outlet_Sales by Outlet_Type.
select outlet_type, max(item_outlet_sales) max_sales from grocery_table group by outlet_type;


#46. Write an SQL query to show total Item_Outlet_Sales by Item_Type.
select item_type, sum(item_outlet_sales) total_sales from grocery_table group by item_type; 


#47. Write an SQL query to show total Item_Outlet_Sales by Item_Fat_Content.
select item_fat_content, sum(item_outlet_sales) total_sales from grocery_table group by item_fat_content;


#48. Write an SQL query to show maximum Item_Visibility by Item_Type.
select item_type, max(item_visibility) from grocery_table group by item_type;


#49. Write an SQL query to show Minimum Item_Visibility by Item_Type.
select item_type, min(item_visibility) from grocery_table group by item_type;


#50. Write an SQL query to show total Item_Outlet_Sales by Item_Type but only WHERE Outlet_Location_Type is Tier 1.
select item_type, sum(item_outlet_sales) total_sales from grocery_table where outlet_location_type = 'tier 1' group by item_type;


#51. Write an SQL query to show total Item_Outlet_Sales by Item_Type WHERE Item_Fat_Content is ONLY Low Fat & LF.
select item_type, sum(item_outlet_sales) total_sales from grocery_table where item_fat_content in ('low fat','lf') group by item_type;












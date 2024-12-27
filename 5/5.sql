--1
select product_name
from products
where unit_price between 3 and 6;

--2
select min(unit_price) min_price
from products
where category_id = 1;

--3
select supplier_id, max(unit_price) max_price
from products
where supplier_id in (1, 3, 5)
group by supplier_id
order by supplier_id;
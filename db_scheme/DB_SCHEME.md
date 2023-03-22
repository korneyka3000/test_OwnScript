# 1. Сущности БД:

### 1.  `TABLE NOMENCLATURE` Номенклатура:
  ```
   - id primary key (VARCHAR | INTEGER)
   - name (VARCHAR)
   - quantity (INTEGER)
   - price (DECIMAL)
   - category_id (Foreign Key -> CATALOG)
   ``` 
---
 ### 2. `TABLE CATEGORY` Каталог номенклатуры/Дерево категорий:
```
   - id primary key (VARCHAR | INTEGER)
   - name (VARCHAR)
   - parent_category_id (Foreign Key -> CATEGORY)
```
---
### 3. `TABLE CLIENTS` Клиенты:
```
   - id primary key (VARCHAR | INTEGER)
   - address (VARCHAR)
   - name (VARCHAR)
```
---
### 4. `TABLE NOMENCLATURE_ORDERS` Наименование_Заказы:
```
   - id primary key (VARCHAR | INTEGER)
   - nomenclature_id (Foreign Key -> NOMENCLATURE)
   - order_id (Foreign Key -> ORDERS)
```
---
### 4. `TABLE ORDERS` Заказы:
```
   - id primary key (VARCHAR | INTEGER)
   - client_id (ForeignK Key -> CLIENTS)
```
---
# 2. Написать следующие SQL запросы:
- Получение информации о сумме товаров заказанных под каждого клиента
(Наименование клиента, сумма)
    ```sql
    select clients.name, SUM(nomenclature.price * nomenclature.quantity) as total_sum 
    from clients
    join orders on clients.id = client_id
    join nomenclature_orders on orders.id = nomenclature_orders.order_id
    join nomenclature on nomenclature_orders.nomenclature_id = nomenclature.id
    group by clients.name;
    ```
- Найти количество дочерних элементов первого уровня вложенности для
категорий номенклатуры.
    ```sql
    select category.name, COUNT(child_category.id) as num_child_category
    from category
    left join category as child_category on category.id = child_category.parent_category_id
    where category.parent_category_id is null
    group by category.id;
    ```
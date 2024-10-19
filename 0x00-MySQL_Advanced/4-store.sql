-- creatting trigger which decreases quantity of item after adding new order

CREATE TRIGGER decrement
AFTER INSERT
ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE NAME = NEW.item_name;

-- Use the correct database
USE alx_book_store;

-- Get full description of the books table using INFORMATION_SCHEMA
SELECT COLUMN_NAME, COLUMN_TYPE 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_SCHEMA = 'alx_book_store' 
AND TABLE_NAME = 'Books';

from core.db import db
from loguru import logger
from database.database import SAMPLE_PRODUCTS
async def check_table_customer():
    await db.execute('''
            CREATE TABLE IF NOT EXISTS customers(
                       customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       telegram_id INTEGER UNIQUE NOT NULL,
                       full_name TEXT,
                       username TEXT,
                       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
                       ''')
    logger.error("table CUSTOMER")

async def check_table_products():
    await db.execute('''
            CREATE TABLE IF NOT EXISTS products(
                       product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       price REAL NOT NULL,
                       description TEXT,
                       category TEXT NOT NULL,
                       is_available BOOLEAN)
                       ''')
    logger.error("table products")

async def check_table_orders():
    await db.execute('''
            CREATE TABLE IF NOT EXISTS orders(
                       order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       customer_id INTEGER NOT NULL,
                       total_amount REAL NOT NULL,
                       status BOLEAN DEFAULT TRUE,
                       adress TEXT,
                       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                       FOREIGN KEY (customer_id) REFERENCES customers(customer_id))
                       ''')
    logger.error("table orders")

async def check_table_order_item():
    await db.execute('''
            CREATE TABLE IF NOT EXISTS order_item(
                       item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       order_id INTEGER NOT NULL,
                       product_id INTEGER NOT NULL,
                       product_name TEXT NOT NULL,
                       quantity INTEGER NOT NULL,
                       price REAL NOT NULL,
                       FOREIGN KEY (order_id) REFERENCES orders(order_id),
                       FOREIGN KEY (product_id) REFERENCES products(product_id))
                       ''')
    logger.warning("table order_item")

async def check_table_carts():
    await db.execute('''
            CREATE TABLE IF NOT EXISTS carts(
                       cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       customer_id INTEGER NOT NULL,
                       items TEXT NOT NULL,
                       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                       updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                       FOREIGN KEY (customer_id) REFERENCES customers(customer_id))
                       ''')
    logger.warning("table carts")

async def add_items_into_table_products():
    try:
        await db.execute('''
            INSERT INTO products (product_id, name, price, description, category, is_available)
                               VALUES($1, $2, $3, $4, $5, $6)
                               ''', (2, "Продукт №2", 100, "Описание продукта №1", "категория 2", True,))
        logger.warning("add items into table products")
    except Exception as e:
        logger.error("fail add items into table products")

async def get_categories():
    logger.warning("get_categories")
    a = await db.fetchall("SELECT DISTINCT category FROM products WHERE is_available = TRUE", ())
    logger.error(a)
    for row in a:
        logger.error(row[0])
        logger.error(row)
    logger.warning("get_categories")

    

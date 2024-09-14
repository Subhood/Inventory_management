from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home Page to View Items
@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return render_template('index.html', items=items)

# Add New Item
@app.route('/add', methods=('GET', 'POST'))
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO items (name, quantity, price) VALUES (?, ?, ?)',
                     (name, quantity, price))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_item.html')

# Update an Item
@app.route('/update/<int:id>', methods=('GET', 'POST'))
def update_item(id):
    conn = get_db_connection()
    item = conn.execute('SELECT * FROM items WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']
        
        conn.execute('UPDATE items SET name = ?, quantity = ?, price = ? WHERE id = ?',
                     (name, quantity, price, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    conn.close()
    return render_template('update_item.html', item=item)

# Delete an Item
@app.route('/delete/<int:id>')
def delete_item(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM items WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

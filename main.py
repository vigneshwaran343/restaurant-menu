from flask import Flask

app = Flask(__name__)

STYLE = """
<style>
body{
    font-family: Arial, sans-serif;
    background:#f4f4f4;
    margin:0;
    padding:20px;
}

h1{
    text-align:center;
    color:#8B0000;
}

.menu-card{
    background:white;
    margin:15px auto;
    width:85%;
    padding:20px;
    border-radius:15px;
    box-shadow:0 4px 12px rgba(0,0,0,0.15);
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.item-name{
    font-size:22px;
    font-weight:bold;
}

.item-desc{
    color:gray;
    margin-top:5px;
    font-size:14px;
}

.price{
    color:#8B0000;
    font-size:24px;
    font-weight:bold;
}

.badge{
    margin-top:8px;
    display:inline-block;
    background:#ffeaa7;
    padding:5px 10px;
    border-radius:20px;
    font-size:12px;
}

.back-btn{
    display:block;
    width:150px;
    margin:30px auto;
    text-align:center;
    text-decoration:none;
    background:#8B0000;
    color:white;
    padding:12px;
    border-radius:10px;
}

.category-card{
    background:white;
    width:280px;
    margin:20px auto;
    padding:20px;
    border-radius:15px;
    box-shadow:0 4px 12px rgba(0,0,0,0.15);
    text-align:center;
}

.category-card a{
    text-decoration:none;
    color:black;
    font-size:22px;
    font-weight:bold;
}

.home{
    background:linear-gradient(to right,#8B0000,#b22222);
    min-height:100vh;
    color:white;
    text-align:center;
    padding-top:120px;
}

.home h1{
    color:white;
    font-size:50px;
}

.menu-btn{
    background:white;
    color:#8B0000;
    padding:15px 40px;
    border-radius:10px;
    text-decoration:none;
    font-size:22px;
    font-weight:bold;
}
</style>
"""


@app.route('/')
def home():
    return f"""
    <html>
    <head>
    <title>Royal Spice Restaurant</title>
    {STYLE}
    </head>

    <body class="home">

        <h1>🍽 Royal Spice Restaurant</h1>

        <h3>Welcome to Our Digital Menu</h3>

        <br><br>

        <a href="/categories" class="menu-btn">
            VIEW MENU
        </a>

    </body>
    </html>
    """


@app.route('/categories')
def categories():
    return f"""
    <html>
    <head>{STYLE}</head>

    <body>

        <h1>📋 Menu Categories</h1>

        <div class="category-card">
            <a href="/biriyani">🍛 Biriyani</a>
        </div>

        <div class="category-card">
            <a href="/juice">🥤 Juice</a>
        </div>

        <div class="category-card">
            <a href="/starters">🍗 Starters</a>
        </div>

        <div class="category-card">
            <a href="/desserts">🍰 Desserts</a>
        </div>

    </body>
    </html>
    """


@app.route('/biriyani')
def biriyani():
    return f"""
    <html>
    <head>{STYLE}</head>
    <body>

    <h1>🍛 Biriyani Menu</h1>

    <div class="menu-card">
        <div>
            <div class="item-name">Chicken Biriyani</div>
            <div class="item-desc">Traditional dum cooked chicken biriyani.</div>
            <div class="badge">⭐ Best Seller</div>
        </div>
        <div class="price">₹220</div>
    </div>

    <div class="menu-card">
        <div>
            <div class="item-name">Mutton Biriyani</div>
            <div class="item-desc">Rich and spicy mutton biriyani.</div>
        </div>
        <div class="price">₹280</div>
    </div>

    <div class="menu-card">
        <div>
            <div class="item-name">Fish Biriyani</div>
            <div class="item-desc">Fresh fish cooked with aromatic spices.</div>
        </div>
        <div class="price">₹260</div>
    </div>

    <div class="menu-card">
        <div>
            <div class="item-name">Hyderabadi Biriyani</div>
            <div class="item-desc">Authentic Hyderabadi style biriyani.</div>
        </div>
        <div class="price">₹250</div>
    </div>

    <a href="/categories" class="back-btn">⬅ Back</a>

    </body>
    </html>
    """


@app.route('/juice')
def juice():
    return f"""
    <html>
    <head>{STYLE}</head>
    <body>

    <h1>🥤 Juice Menu</h1>

    <div class="menu-card">
        <div>
            <div class="item-name">Mango Juice</div>
            <div class="item-desc">Fresh mango blend.</div>
        </div>
        <div class="price">₹80</div>
    </div>

    <div class="menu-card">
        <div>
            <div class="item-name">Orange Juice</div>
            <div class="item-desc">Fresh squeezed oranges.</div>
        </div>
        <div class="price">₹70</div>
    </div>

    <div class="menu-card">
        <div>
            <div class="item-name">Watermelon Juice</div>
            <div class="item-desc">Refreshing summer drink.</div>
        </div>
        <div class="price">₹60</div>
    </div>

    <div class="menu-card">
        <div>
            <div class="item-name">Apple Juice</div>
            <div class="item-desc">Pure apple goodness.</div>
        </div>
        <div class="price">₹100</div>
    </div>

    <a href="/categories" class="back-btn">⬅ Back</a>

    </body>
    </html>
    """


@app.route('/starters')
def starters():
    return f"""
    <html>
    <head>{STYLE}</head>
    <body>

    <h1>🍗 Starters</h1>

    <div class="menu-card">
        <div>
            <div class="item-name">Chicken 65</div>
            <div class="item-desc">Spicy fried chicken.</div>
        </div>
        <div class="price">₹180</div>
    </div>

    <div class="menu-card">
        <div>
            <div class="item-name">Dragon Chicken</div>
            <div class="item-desc">Sweet and spicy chicken.</div>
        </div>
        <div class="price">₹220</div>
    </div>

    <div class="menu-card">
        <div>
            <div class="item-name">Paneer Tikka</div>
            <div class="item-desc">Grilled paneer cubes.</div>
        </div>
        <div class="price">₹190</div>
    </div>

    <a href="/categories" class="back-btn">⬅ Back</a>

    </body>
    </html>
    """


@app.route('/desserts')
def desserts():
    return f"""
    <html>
    <head>{STYLE}</head>
    <body>

    <h1>🍰 Desserts</h1>

    <div class="menu-card">
        <div>
            <div class="item-name">Gulab Jamun</div>
            <div class="item-desc">Traditional Indian sweet.</div>
        </div>
        <div class="price">₹60</div>
    </div>

    <div class="menu-card">
        <div>
            <div class="item-name">Ice Cream</div>
            <div class="item-desc">Creamy vanilla delight.</div>
        </div>
        <div class="price">₹80</div>
    </div>

    <div class="menu-card">
        <div>
            <div class="item-name">Chocolate Brownie</div>
            <div class="item-desc">Rich chocolate dessert.</div>
        </div>
        <div class="price">₹120</div>
    </div>

    <a href="/categories" class="back-btn">⬅ Back</a>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
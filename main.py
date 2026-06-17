from flask import Flask

app = Flask(__name__)

@app.route('/')
def menu():
    return """
    <html>
    <head>
        <title>Restaurant Menu</title>
    </head>
    <body>
        <h1>ABC Restaurant</h1>

        <h2>Starters</h2>
        <ul>
            <li>Veg Soup - ₹80</li>
            <li>Chicken Soup - ₹120</li>
        </ul>

        <h2>Main Course</h2>
        <ul>
            <li>Fried Rice - ₹150</li>
            <li>Chicken Biryani - ₹220</li>
        </ul>

        <h2>Drinks</h2>
        <ul>
            <li>Coffee - ₹50</li>
            <li>Lime Juice - ₹40</li>
        </ul>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
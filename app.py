from flask import Flask,render_template



"""Creare applicazione web con due pagine:

    home page con una navbar con due collegamenti (home page, details)
    pagina details contenente una tabella con dei prodotti (nome prodotto, scaffale, prezzo), una navbar con tre collegamenti (home page, details e wikipedia.
    ogni pagina ha un titolo.

I dati dei prodotti sono memorizzati all'interno di una tupla di tuple."""

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",titolo = 'home')
@app.route("/details")
def details():
    return render_template("details.html",titolo = 'details')

app.run(debug=True)

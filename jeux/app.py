from flask import Flask, render_template, request
import random

app = Flask(__name__)

# On garde le nombre mystère en mémoire simple (pour un vrai jeu, on utiliserait une session)
nombre_mystere = random.randint(1, 100)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    global nombre_mystere

    if request.method == "POST":
        try:
            proposition = int(request.form.get("proposition"))
            if proposition < nombre_mystere:
                message = "C'est plus 👆"
            elif proposition > nombre_mystere:
                message = "C'est moins 👇"
            else:
                message = "Bravo ! Tu as trouvé 🎉 Nouveau nombre généré."
                nombre_mystere = random.randint(1, 100)
        except ValueError:
            message = "Entre un nombre valide 😉"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)

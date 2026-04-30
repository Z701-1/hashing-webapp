from hashlib import sha256

from flask import Flask, render_template, request


app = Flask(__name__, template_folder=".", static_folder=".", static_url_path="")
ALGORITHM = "SHA-256"
MODES = {
    "Plaintext": "Plaintext",
    "Hash": "Hash with SHA-256",
    "Hash and Salt": "Hash with SHA-256 + Salt",
}


@app.route("/", methods=["GET", "POST"])
def index():
    error = ""
    text = ""
    algorithm = ALGORITHM
    mode = "Plaintext"
    salt = ""
    details = None
    comparison = None

    if request.method == "POST":
        text = request.form.get("text", "")
        algorithm = request.form.get("algorithm", ALGORITHM)
        mode = request.form.get("mode", "Plaintext")
        salt = request.form.get("salt", "")
        salt_present = bool(salt.strip())

        if not text.strip():
            error = "Input is required."
        elif algorithm != ALGORITHM:
            error = "Invalid algorithm selected."
        elif mode not in MODES:
            error = "Invalid mode selected."
        elif mode == "Hash and Salt" and not salt_present:
            error = "Salt is required for Hash with SHA-256 + Salt."
        elif mode == "Plaintext":
            details = {
                "algorithm": algorithm,
                "mode": MODES[mode],
                "plaintext": text,
                "salt": "",
                "combined_input": "",
                "final_output": text,
            }
        elif mode == "Hash":
            details = {
                "algorithm": algorithm,
                "mode": MODES[mode],
                "plaintext": text,
                "salt": "",
                "combined_input": "",
                "final_output": sha256(text.encode("utf-8")).hexdigest(),
            }
        elif mode == "Hash and Salt":
            combined_input = f"{text}{salt}"
            plain_hash = sha256(text.encode("utf-8")).hexdigest()
            salted_hash = sha256(combined_input.encode("utf-8")).hexdigest()
            details = {
                "algorithm": algorithm,
                "mode": MODES[mode],
                "plaintext": text,
                "salt": salt,
                "combined_input": combined_input,
                "final_output": salted_hash,
            }
            comparison = {
                "plain_hash": plain_hash,
                "salted_hash": salted_hash,
            }

    return render_template(
        "index.html",
        error=error,
        text=text,
        algorithm=algorithm,
        mode=mode,
        salt=salt,
        details=details,
        comparison=comparison,
        algorithm_options=[ALGORITHM],
        mode_options=MODES,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

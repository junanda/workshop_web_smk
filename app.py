from flask import Flask, render_template, request, redirect, url_for, jsonify

task_list = [
    {"id": 1, "title": "Buy groceries","completed": False},
    {"id": 2, "title": "Read a book", "completed": True},
    {"id": 3, "title": "Write code", "completed": False},
]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", tasks=task_list)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    # Menambahkan tugas baru ke dalam daftar
    # tulis kode untuk menambahkan tugas di sini
    # jangan lupa untuk memvalidasi input dan memberikan ID unik untuk setiap tugas
    return redirect(url_for("index"))

# Route untuk mengubah status tugas (selesai/belum)
@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    for task in task_list:
        if task['id'] == task_id:
            # Mengubah status 'done' (True menjadi False atau sebaliknya)
            # tuliskan kode untuk mengubah status di sini
            return jsonify({'status': 'success'})
    return jsonify({'status': 'error'}), 404

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    global task_list
    # Menghapus tugas berdasarkan ID
    # tuliskan kode untuk menghapus tugas di sini
    return jsonify({'status': 'success'})

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    new_title = request.json.get('title')
    # kode untuk mengubah judul tugas
    # Cari tugas berdasarkan ID dan perbarui judulnya
    return jsonify({'status': 'error'}), 404

if __name__ == "__main__":
    app.run(debug=True)
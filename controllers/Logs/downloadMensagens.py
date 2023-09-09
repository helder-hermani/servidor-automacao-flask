from flask import send_file, render_template

def downloadMensagens(id):
    log_file_path = f'static/app/logs/history/{id}.log'
    try:
        return send_file(log_file_path, as_attachment=True)
    except Exception as err:
        return render_template('logs/not-found.html.jinja')
from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        # Параметры вашей почты
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        sender_email = 'zummerot@gmail.com'
        sender_password = 'ваш_пароль'
        recipient_email = 'zummerot@gmail.com'

        # Получение данных из запроса
        data = request.json

        # Формирование текста письма
        email_text = f"Новые данные от пользователя:\n\n{data}"

        # Отправка письма
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            msg = MIMEText(email_text)
            msg['Subject'] = 'Новые данные от пользователя'
            msg['From'] = sender_email
            msg['To'] = recipient_email

            server.sendmail(sender_email, recipient_email, msg.as_string())

        return 'Данные успешно отправлены.', 200
    except Exception as e:
        print(f'Ошибка: {e}')
        return 'Ошибка при отправке данных.', 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)

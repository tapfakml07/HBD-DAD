from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # คุณสามารถเปลี่ยนชื่อและคำอวยพรตรงนี้ได้
    name = "คุณพ่อ"
    message = "ขอให้มีความสุขมากๆ สุขภาพแข็งแรง คิดสิ่งใดขอให้สมปรารถนา และมีความสุขในทุกๆ วันนะ!"
    
    return render_template('index.html', name=name, message=message)

if __name__ == '__main__':
    app.run(debug=True)
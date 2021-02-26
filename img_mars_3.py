from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style3.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 Align=center>Анкета претендента</h1>
                            <h2 Align=center>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="Фамилия" class="form-control" id="text" placeholder="Введите фамилию" name="text">
                                    <input type="Имя" class="form-control" id="text" placeholder="Введите имя" name="text">
                                    <label for="text"></label>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Дошкольное образование</option>
                                          <option>Обязательное образование</option>
                                          <option>Высшее образование</option>
                                        </select>
                                    </div>
                                    <label for="text"></label>
                                    <fieldset class="form-group">
                                        <label for="job">Какие у Вас профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="1" value="1" checked>
                                          <label class="form-check-label" for="1">
                                            инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="2" value="2">
                                          <label class="form-check-label" for="2">
                                            пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="3" value="3">
                                          <label class="form-check-label" for="3">
                                            строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="4" value="4">
                                          <label class="form-check-label" for="4">
                                            экзобиолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="5" value="5">
                                          <label class="form-check-label" for="5">
                                            врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="6" value="6">
                                          <label class="form-check-label" for="6">
                                            инженер по терраформированию
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="7" value="7">
                                          <label class="form-check-label" for="7">
                                            климатолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="8" value="8">
                                          <label class="form-check-label" for="8">
                                            специалист по радиационной защите
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="9" value="9">
                                          <label class="form-check-label" for="9">
                                            астрогеолог
                                          </label>
                                        </div>
                                        </label>
                                     </fieldset>
                                    <label for="text"></label>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                     </div>
                                    <label for="text"></label>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <label for="text"></label>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <label for="text"></label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <label for="text"></label>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
# Решение

Как следует из описания - наша цель купить байкальской воды. Для этого нужно зарегистрироваться и авторизоваться.  
Но на странице регистрации мы видим плашку о том, что регистрация временно закрыта из-за ажиотажа. Оставшийся вариант - найти креды аккаунта и войти под ними.  

Изучив страницы сайта, в файле `static/styles.css` мы находим логин и пароль от аккаунта. Но при вводе этих данных от нас просят код двухфакторной аутентификации. Далее необходимо было проверить наличие rate limit или других ограничений на количество попыток ввода кода, и обнаружить, что их нет.  

Для эксплуатации уязвимости нужно было перебрать код двухфакторной аутентификации, например через скрипт на python или burp suite. Пример скрипта вы можете найти в файле `exploit.py`.
# Encyclopedia

## Описание скрипта

Скрипт производит конвертирование md-файлов статей в HTML и делает
из них статический сайт.

## Описание рабочей директории

Рабочая директория состоит из следующих папок:

* articles - директория, в которой содержатся статьи в формате Markdown;
* site - директория, в которой сохраняется сгенерированный сайт.
  Включает в себя папки:
    * articles - директория, в которой сохраняются сгенерированные
      html-файлы статей;
    * js - файлы bootstrap с кодом на JavaScript;
    * css - файлы bootstrap со css-стилями;
    * ico - файлы bootstrap изображений;
* templates - директория с шаблонами Jinja2.

## pre-commit hook

В рабочей директории содержится git-перехватчик (файл pre-commit).
Для его использования указанный файл следует поместить в каталог
.git/hooks/. Перехватчик отслеживает измение md-файлов статей в 
каталоге articles. Если он обнаруживает, что в индексе содержатся
статьи, которые войдут в следующий коммит, то сайт будет пересобран 
автоматически при выполнении команды `git commit`.

## Пример использования

Ниже приведен пример использования скрипта и его вывод:
```sh
$ python3.5 ./site_generator.py
[site_generator.py#] INFO     [01/08/2017 01:12:23 PM] Index page has been created
[site_generator.py#] INFO     [01/08/2017 01:12:23 PM] Article "Гит/История" has been created
[site_generator.py#] INFO     [01/08/2017 01:12:23 PM] Article "Арсенал/Гугл" has been created
[site_generator.py#] INFO     [01/08/2017 01:12:23 PM] Article "Арсенал/Девман" has been created
[site_generator.py#] INFO     [01/08/2017 01:12:23 PM] Article "Арсенал/Английский" has been created
[site_generator.py#] INFO     [01/08/2017 01:12:23 PM] Article "Арсенал/Кодэнви" has been created
[site_generator.py#] INFO     [01/08/2017 01:12:23 PM] Article "Арсенал/Консоль" has been created
[site_generator.py#] INFO     [01/08/2017 01:12:23 PM] Article "Арсенал/Гит и Гитхаб" has been created
[site_generator.py#] INFO     [01/08/2017 01:12:23 PM] Article "Основы Питона/Стайлгайд" has been created
[site_generator.py#] INFO     [01/08/2017 01:12:23 PM] Article "Основы Питона/Комментарии" has been created
[site_generator.py#] INFO     [01/08/2017 01:12:23 PM] Article "Основы Питона/Зачем нужен Питон" has been created
[site_generator.py#] INFO     [01/08/2017 01:12:23 PM] Article "Основы Питона/Основные типы данных" has been created
[site_generator.py#] INFO     [01/08/2017 01:12:23 PM] Article "Основы Питона/Основные конструкции" has been created
[site_generator.py#] INFO     [01/08/2017 01:12:23 PM] Article "Основы Питона/Типы данных" has been created
[site_generator.py#] INFO     [01/08/2017 01:12:23 PM] Article "Основы Питона/Модули" has been created
[site_generator.py#] INFO     [01/08/2017 01:12:23 PM] Article "Основы Питона/Полезные приёмы" has been created
```

Ниже приведен пример работы git-перехватчика:

```sh
$ git commit -m "Тестирование pre-commit"
pre-commit# WARNING  [01/08/2017 02:22:30 PM] 
            Markdown source files changes are detected. The site will be rebuilt. Files with changes:
            
pre-commit# WARNING  [01/08/2017 02:22:30 PM] articles/4_git/22_git_history.md
[site_generator.py#] INFO     [01/08/2017 02:22:30 PM] Index page has been created
[site_generator.py#] INFO     [01/08/2017 02:22:30 PM] Article "Гит/История" has been created
[site_generator.py#] INFO     [01/08/2017 02:22:30 PM] Article "Основы Питона/Стайлгайд" has been created
[site_generator.py#] INFO     [01/08/2017 02:22:30 PM] Article "Основы Питона/Комментарии" has been created
[site_generator.py#] INFO     [01/08/2017 02:22:30 PM] Article "Основы Питона/Зачем нужен Питон" has been created
[site_generator.py#] INFO     [01/08/2017 02:22:30 PM] Article "Основы Питона/Основные типы данных" has been created
[site_generator.py#] INFO     [01/08/2017 02:22:30 PM] Article "Основы Питона/Основные конструкции" has been created
[site_generator.py#] INFO     [01/08/2017 02:22:30 PM] Article "Основы Питона/Типы данных" has been created
[site_generator.py#] INFO     [01/08/2017 02:22:30 PM] Article "Основы Питона/Модули" has been created
[site_generator.py#] INFO     [01/08/2017 02:22:30 PM] Article "Основы Питона/Полезные приёмы" has been created
[site_generator.py#] INFO     [01/08/2017 02:22:30 PM] Article "Арсенал/Гугл" has been created
[site_generator.py#] INFO     [01/08/2017 02:22:30 PM] Article "Арсенал/Девман" has been created
[site_generator.py#] INFO     [01/08/2017 02:22:30 PM] Article "Арсенал/Английский" has been created
[site_generator.py#] INFO     [01/08/2017 02:22:30 PM] Article "Арсенал/Кодэнви" has been created
[site_generator.py#] INFO     [01/08/2017 02:22:30 PM] Article "Арсенал/Консоль" has been created
[site_generator.py#] INFO     [01/08/2017 02:22:30 PM] Article "Арсенал/Гит и Гитхаб" has been created
[master be82a4b] Тестирование pre-commit
 1 file changed, 1 insertion(+), 1 deletion(-)
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

# duvar-app

![](app/static/assets/duvarov.png)

Duvarov kişilerin kendilerine anonim bir duvar yaratabileceği bir uygulamadır. 

## Demo
[Duvarov Websitesi](https://duvarov.herokuapp.com/)

## Installation

`wsgi.py` dosyası çalıştırılarak direkt `0.0.0.0:5000` adresinden erişim sağlanabilir. 


Repo heroku deployment için tamamen hazırdır, `Procfile` ve `runtime.txt` dosyaları değiştirilerek versiyon değişikliği yapılabilir.
Pythonanywhere tarafında sadece requirements.txt yüklenilerek proje canlıya alınabilir.

Duvar temizliği için heroku içerisinde yerel değişkeniniz `password`'un ayarlanması gerekmektedir.

## Docker
`docker build -t duvar:latest .`

`docker run -d -p 5000:5000 duvar:latest`

## Requirements:
- flask
- sqlite3
- gunicorn

# To-Do's
- [ ]  Link, telefon numaraları gönderilmesini engellemek için regex
- [ ] Küfür gönderilmesini engellemek için bir çalışma
- [ ] Tamamen boşluk veya yazı içermeyen karakterlerin gönderilmesini engelleme
- [ ] header kısımlarının bir kez yazılıp diğer sayfalarda extend edilmesi
- [ ] HTML ve CSS dosyalarında düzenlemeler
> front-end tarafında muhtemelen çok fazla hatam vardır, projeyi yaparken öğrendim :)
- [ ] Database'in app içerisinde değil servis tarafında tutulması

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

## To-Do's
- [ ] Link, telefon numaraları gönderilmesini engellemek için regex
- [x] Küfür gönderilmesini engellemek için bir çalışma [Melih](https://github.com/msrexe)
- [x] Tamamen boşluk veya yazı içermeyen karakterlerin gönderilmesini engelleme [Melih](https://github.com/msrexe) | [Murat Can Kurtulus](https://github.com/makermotion)
- [x] header kısımlarının bir kez yazılıp diğer sayfalarda extend edilmesi. [Selman Baskaya](https://github.com/selmanbaskaya)
- [x] HTML ve CSS dosyalarında düzenlemeler. [Enes Sonmez](https://github.com/enesonmez)
- [x] Database'in app içerisinde değil servis tarafında tutulması [Mert Cobanov](https://github.com/cobanov)
- [x] Projenin dockerize edilmesi [Mert Cobanov](https://github.com/cobanov)

## Contributors
- [Selman Baskaya](https://github.com/selmanbaskaya)
- [Enes Sonmez](https://github.com/enesonmez)

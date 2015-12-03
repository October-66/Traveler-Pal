# Traveler-Pal

traveler-pal, a helper for travelers

## Quick Start

1.Download and install Python, Django(1.8.4), MySQL, Node，gulp

2.Install DjangoUeditor, duoshuo

```shell
pip install DjangoUeditor
```
install [duoshuo](http://dev.duoshuo.com/threads/500c9c58a03193c12400000c)
```
pip install install.py
```
3.Watch the static files

```shell
cd ./Traveler-Pal/Traveler-Pal/app/static && npm install
cd ./Traveler-Pal/Traveler-Pal/app/static && gulp
```
4.Run
open the mysql and make a migrate
```shell
python manage.py makemigrations
python manage.py migrate
```
```shell
cd ./Traveler-Pal && python manage.py runserver
```

5.Open the [127.0.0.1:8000](http://127.0.0.1:8000)

## Plugins
* DjangoUeditor
* amaps
* duoshuo
# team-work-demo

## Instalación

```shell
git clone https://github.com/Galindo-lab/team-work-demo.git
cd team-work-demo
python -m venv venv
pip install -r requirements.txt
```

## Hacer las migraciones
Para agilizar el desarollo se utilizo MongoDB, pero se puede usar otra base de datos en settings.py

```shell
cd teamworkdemo
python manage.py makemigrations teamwork
python manage.py migrate
```

## Ejecutar el servidor
```shell
python manage.py runserver
```

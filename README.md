# team-work-demo

## Instalación y migracion 

```shell
git clone https://github.com/Galindo-lab/team-work-demo.git
cd team-work-demo
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Hacer las migraciones
Para agilizar el desarollo se utilizo MongoDB, pero se puede usar otra base de datos en settings.py

```shell
cd teamworkdemo
python manage.py makemigrations teamwork
python manage.py migrate
```

### Ejecutar el servidor
```shell
python manage.py runserver
```

## Diagrama de Models
![your-UML-diagram-name](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/Galindo-lab/team-work-demo/develop/diagrams/clases.iuml)
=======

<!-- 
## Informacion adicional
https://www.belbin.es/roles-de-equipo/
https://www.belbin.com/about/belbin-team-roles
-->
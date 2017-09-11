# Pré Requisitos
- python 3 e pip3
- ``$ sudo apt-get install python3 python3-pip``

- MK Virtualenv
- ``$ pip3 install mkvirtualenv``

# Instalação
- ``$ mkvirtualenv agenday -p python3``

Sempre que for utilizar o sistema, entre no isolamento do mkvirtualenv com o comando

- ``$ workon agenday``

Instale os plugins python

- ``(agenday) $ pip install -r requirements.txt``

Rode as migrações

- ``(agenday) $ python manage.py migrate``

Rode o servidor

- ``(agenday) $ python manage.py runserver``
**************************************
SCP - Sistema de Controle de Pacientes
**************************************

Instalação de dependências para uso do postgresql como database
---------------------------------------------------------------
    ``sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib``


Instalação da virtualenv
------------------------
  ``
    $ sudo pip install virtualenvwrapper
    $ sudo vim .bashrc
  ``
* No final do arquivo adicionar:
  ``
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
  ``
* Após fechar rodar:
  ``
    source ~/.bashrc
  ``


Instalação das dependências do projeto:
---------------------------------------
* Criar uma virtualenv para instalar dependências do projeto:
  ``mkvirtualenv --python=/usr/bin/python3 scp``
* Entrar na virtualenv:
  ``workon scp``
* Instalar dependências:
  ``
    pip install -r requirements.txt
    ./manage.py bower install
  ``


Criar banco:
---------------------------------------
* Em outro terminal rode:
  ``
    sudo su - postgres
    createdb scp
    psql
    GRANT ALL PRIVILEGES ON DATABASE scp TO postgres;
    \q
    exit
  ``

* De volta ao terminal dentro da virtualenv rode:
  ``
    ./manage.py migrate
    ./manage.py loaddata criar_tipos.yaml
  ``

Rodando projeto:
---------------------------------------
* Rode:
  ``./manage.py runserver``
* Acesse no navegador:
  ``localhost:8000``

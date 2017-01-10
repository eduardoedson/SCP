**************************************
SCP - Sistema de Controle de Pacientes
**************************************

Instalação de dependências para uso do postgresql como database
---------------------------------------------------------------
    ``sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib``


Instalação da virtualenv
------------------------
  ``
    $ sudo pip install virtualenvwrapper<br />
    $ sudo vim .bashrc
  ``
* No final do arquivo adicionar:<br />
  ``
    export WORKON_HOME=$HOME/.virtualenvs<br />
    source /usr/local/bin/virtualenvwrapper.sh
  ``
* Após fechar rodar:<br />
  ``
    source ~/.bashrc
  ``


Instalação das dependências do projeto:
---------------------------------------
* Criar uma virtualenv para instalar dependências do projeto:<br />
  ``mkvirtualenv --python=/usr/bin/python3 scp``
* Entrar na virtualenv:<br />
  ``workon scp``
* Instalar dependências:<br />
  ``
    pip install -r requirements.txt
    ./manage.py bower install
  ``


Criar banco:
---------------------------------------
* Em outro terminal rode:<br />
  ``
    sudo su - postgres
    createdb scp
    psql
    GRANT ALL PRIVILEGES ON DATABASE scp TO postgres;
    \q
    exit
  ``

* De volta ao terminal dentro da virtualenv rode:<br />
  ``
    ./manage.py migrate
    ./manage.py loaddata criar_tipos.yaml
  ``

Rodando projeto:<br />
---------------------------------------
* Rode:<br />
  ``./manage.py runserver``
* Acesse no navegador:<br />
  ``localhost:8000``


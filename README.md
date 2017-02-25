**************************************
SCP - Sistema de Controle de Pacientes
**************************************

Instalação de dependências para uso do postgresql como database<br />
---------------------------------------------------------------
  ``sudo apt-get install python-pip python-dev python3-dev libpq-dev postgresql postgresql-contrib``<br />


Instalação da virtualenv<br />
------------------------
  ``sudo pip install virtualenvwrapper``<br />
  ``sudo vim .bashrc``<br />
* No final do arquivo adicionar:<br />
  ``export WORKON_HOME=$HOME/.virtualenvs``<br />
  ``source /usr/local/bin/virtualenvwrapper.sh``<br />
* Após fechar rodar:<br />
  ``source ~/.bashrc``<br />


Instalação das dependências do projeto:<br />
---------------------------------------
* Criar uma virtualenv para instalar dependências do projeto:<br />
  ``mkvirtualenv --python=/usr/bin/python3 scp``<br />
* Entrar na virtualenv:<br />
  ``workon scp``<br />
* Instalar dependências:<br />
  ``pip install -r requirements.txt``<br />
  ``./manage.py bower install``<br />


Criar banco:<br />
---------------------------------------
* Em outro terminal rode:<br />
  ``sudo su - postgres``<br />
  ``createdb scp``<br />
  ``psql``<br />
  ``GRANT ALL PRIVILEGES ON DATABASE scp TO postgres;``<br />
  ``\q``<br />
  ``exit``<br />

* De volta ao terminal dentro da virtualenv rode:<br />
  ``./manage.py migrate``<br />
  ``./manage.py loaddata criar_padroes.yaml``<br />

Rodando projeto:<br />
---------------------------------------
* Rode:<br />
  ``./manage.py runserver --insecure``<br />
* Acesse no navegador:<br />
  ``localhost:8000``<br />

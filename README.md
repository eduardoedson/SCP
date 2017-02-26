**************************************
SCP - Sistema de Controle de Pacientes
**************************************

Instalação de dependências<br />
---------------------------------------------------------------
  ``sudo apt-get install python-pip python-dev python3-dev libpq-dev postgresql postgresql-contrib npm curl git vim pgadmin3``<br />
  ``sudo curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -``<br />
  ``sudo apt-get install -y nodejs``<br />
  ``sudo apt-get install -y build-essential``<br />
  ``sudo npm install -g bower``<br />

  ``git clone https://github.com/eduardoedson/scp.git``
  
  Criar banco:<br />
---------------------------------------
* Em outro terminal rode:<br />
  ``sudo su - postgres``<br />
  ``createdb scp``<br />
  ``psql``<br />
  ``CREATE USER scp WITH PASSWORD '1234';``<br />
  ``GRANT ALL PRIVILEGES ON DATABASE scp TO scp;``<br />
  ``\q``<br />
  ``exit``<br />

Instalação da virtualenv<br />
------------------------
  ``sudo pip install virtualenvwrapper``<br />
  ``sudo vim ~/.bashrc``<br />
* No final do arquivo adicionar:<br />
  ``export WORKON_HOME=$HOME/.virtualenvs``<br />
  ``source /usr/local/bin/virtualenvwrapper.sh``<br />
* Após fechar rodar:<br />
  ``source ~/.bashrc``<br />


Instalação das dependências do projeto:<br />
---------------------------------------
* Criar uma virtualenv para instalar dependências do projeto:<br />
  ``mkvirtualenv --python=/usr/bin/python3 scp``<br />
* Instalar dependências:<br />
  ``pip install -r requeriments.txt``<br />
  ``./manage.py bower install``<br />


Depedências do banco:<br />
---------------------------------------
  ``./manage.py migrate``<br />
  ``./manage.py loaddata pre_data.yaml``<br />
  ``./sql_scripts inser_cid.py``<br />
  ``./sql_scripts inser_medicamentos.py``<br />

Criar usuário administrador:<br />
---------------------------------------
  ``./manage.py createsuperuser``<br />
  
Rodando projeto:<br />
---------------------------------------
* Rode:<br />
  ``./manage.py runserver --insecure``<br />
* Acesse no navegador:<br />
  ``localhost:8000``<br />

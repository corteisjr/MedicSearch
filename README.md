# MedicSearch

Software que permite, achar médicos de uma determinada região.

## Instalação

- Primeiro clone o repositório e instale os pacotes
  
  ```Terminal
  git clone https://github.com/corteisjr/MedicSearch
  cd MedicSearch
  pip install -r requirements.txt
  ```
- Activação do ambiente virtual em Ubuntu ou distros Linux

```Terminal
    python3 -m venv venv
    source venv/bin/activate
```

- Activação do ambiente virtual no windows
  
```Terminal
    python -m venv venv
    venv/Scripts/activate
```

- Migrate e rodar o servidor

```Terminal
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
```

### Referências

[Django de A a Z](https://www.amazon.com.br/Django-aplica%C3%A7%C3%B5es-r%C3%A1pidas-seguras-escal%C3%A1veis-ebook/dp/B094PW2MF2)

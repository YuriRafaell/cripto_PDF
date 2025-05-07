# Proteja seus arquivos com senha

Converta um arquivo `.txt` em `.pdf` e proteja com uma senha segura de sua escolha.

## COMO USAR?


1. Clone o projeto no seu ambiente local:

```
git clone (link do projeto)
```

2. Abra o VS Code manualmente ou via CMD (no CMD, vá até o diretório do projeto):

```
code .
```

3. No terminal do VS Code ou no seu próprio CMD, execute:

```
python3 app.py
```

OBS: Rode o python de acordo com sua versão instalada no seu sistema.

### Para tornar um executavel 

1. Instale 
```
pip install pyinstaller
```

2. Rode
```
pyinstaller --onefile app.py
```

Vai gerar duas pastas: `build`e `dist`. Dentro da pasta `dist` estará o executavel.

### Desde as versões mais recentes do Ubuntu (como 22.04 em diante), o sistema protege a instalação global do Python com o PEP 668, impedindo instalações com pip fora de ambientes virtuais.

#### "Então como rodar se o ubuntu protege o sistema?"

### Criando um ambiente virtual

1. Abra o terminal no diretório do projeto e rode:
```
python3 -m venv venv
source venv/bin/activate
pip install PyPDF2
```

2. Isso irá criar um ambiente virtual chamado `venv` na pasta do seu projeto, para rodar, execute:
```
source venv/bin/activate
python app.py
```
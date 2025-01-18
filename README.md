# EM ATUALIZAÇÃO

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
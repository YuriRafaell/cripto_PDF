# COMO USAR?


1. Clone o projeto no seu no seu ambiente local:

```
git clone (link do projeto)
```

2. Coloque o arquivo PDF que deseja criptografar na pasta do projeto.

3. Abra o VS Code manualmente ou via CMD (no CMD, vá até o diretório do projeto):

```
code .
```

4. Renomeie os documentos no código:

```
caminho_pdf = 'teste.pdf'
caminho_pdf_protegido = 'documento_protegido.pdf'
senha = 'sua_senha'
```

5. No terminal do VS Code ou no seu próprio CMD, execute:

```
python3 app.py
```

OBS: Rode o python de acordo com sua versão instalada no seu sistema.

# Explicando um pouco do código

1. O que é buffer?
 * É uma área de memória temporária usada para armazenar dados enquanto eles são transferidos de um local para outro. O buffer é usado para criar um PDF na memória antes de gravá-lo em um arquivo.
 ### Vantagens do Uso de Buffer
  * Eficiência: Operações de leitura e gravação em memória são geralmente mais rápidas do que    operações de disco.
  * Flexibilidade: Permite manipular os dados antes de gravá-los no disco, como aplicar criptografia ou compressão.
  * Segurança: Dados sensíveis podem ser mantidos na memória temporariamente e manipulados antes de serem escritos em um local permanente.

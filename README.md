# Project-Init
## Depende de ter _GIT_ e _Python >= 3.8_ instalados

Script para criação de pastas de projeto para múltiplas linguagens de programação.

Para instalar, execute `python -m pip install .` dentro da pasta raíz (onde o 'pyproject.toml' está localizado)

Para usar basta chamar o comando `pinit` no terminal (no diretório onde o projeto deve ser criado) e então seguir o questionário.

As linguagens atualmente suportadas são:
```
Python
JavaScript
TypeScript
Java
C
C++
```

Para configurar uma nova linguagem é necessário:
- Adicionar o nome da linguagem em `languages` no arquivo `pinit/cli.py`
- Adicionar um template em `pinit/templates.py`
  > O template deve conter os arquivos a serem gerados e os conteúdos dentro deles, só segue o padrão dos que já existem e vai dar certo

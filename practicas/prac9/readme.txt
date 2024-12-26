Se han guardado algunos de los Alias propuestos.
Ejecutando los siguientes comandos se guardan en la shell:

git config --global alias.co checkout
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.br branch

Para comprobarlo, se pueden recuperar todos los alias guardados con:
git config --global --list

En mi caso, la salida es la siguiente:
"
user.name=jcerveto
user.email=joan.cerveto@ua.es
pull.rebase=false
core.autocrlf=input
alias.co=checkout
alias.ci=commit
alias.st=status
alias.br=branch
"

- He utilizado el repositorio de GitHub que he estado utilizando durante todo el curso de manera privada. Para esta entrega lo acabo de hacer público. (https://github.com/jcerveto/DCA.git)
- Uso de git bisect:
* git bisect start
* git bisect good/bad hasta encontrar donde pasa de good a bad
* git bisect reset 


- Se ha creado un Git Hook para darle una categoría al commit en el mensaje. Las categorías serán las siguientes: types=("feat" "fix" "docs" "style" "refactor" "test" "chore" "rearrange")

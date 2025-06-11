# Expedição do Milhão: Histórias e Mapas

## Como Instalar

### Criar um ambiente virtual (necessário apenas uma vez)
> python -m venv .venv

### Ativar o ambiente virtual
> .venv\Scripts\activate

### Instalar dependências
> pip install -r requirements.txt

## Como Contribuir

### Ao adicionar qualquer dependência ao projeto, atualize o arquivo "requirements.txt" com o seguinte comando:
> pip freeze > requirements.txt

### Para compilar:
> nuitka emhm.py --standalone --enable-plugin=tk-inter --include-data-file=.env=.env --include-data-dir=images=images --windows-console-mode=disable --output-dir=build

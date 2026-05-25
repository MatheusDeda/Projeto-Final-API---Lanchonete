1- Projeto Final — API Lanchonete:
Este repositório contém a entrega do projeto final da disciplina de **Desenvolvimento Rápido de Aplicações em Python**. 
O objetivo principal deste projeto é evoluir uma API base de uma lanchonete, implementando um sistema para o controle operacional dos pedidos na cozinha, aplicando boas práticas de programação e Arquitetura em Camadas.

2- Funcionalidades Implementadas

O sistema foi concebido para organizar o fluxo de preparação da lanchonete, garantindo as seguintes regras de negócio:

- **Fila de Preparo:** Lista os pedidos ativos, colocando automaticamente os pedidos prioritários no topo da fila. Pedidos cancelados ou já entregues são omitidos.
- **Cancelamento:** Permite cancelar um pedido apenas se este ainda não tiver sido entregue ou previamente cancelado.
- **Observações nos Pedidos:** Clientes podem adicionar observações (ex: "Sem cebola", "Carne ao ponto"). As observações são validadas para não estarem vazias e respeitarem o limite de 200 caracteres.
- **Prioridade dos Pedidos:** Possibilidade de marcar um pedido normal como prioritário, alterando a sua posição na fila da cozinha.

3- Tecnologias Utilizadas

- **[Python 3](https://www.python.org/)**: Linguagem principal.
- **[FastAPI](https://fastapi.tiangolo.com/)**: Framework web moderno e de alto desempenho para a construção da API.
- **[Pydantic](https://docs.pydantic.dev/)**: Validação de dados e gestão de definições (Schemas).
- **[Pytest](https://docs.pytest.org/)**: Framework para a criação e execução de testes automatizados.
- **[Uvicorn](https://www.uvicorn.org/)**: Servidor ASGI para executar a aplicação FastAPI.

4- Arquitetura do Projeto

O projeto segue estritamente um padrão arquitetural em camadas para separar responsabilidades e isolar as regras de negócio:

```text
lanchonete_api/
├── main.py                    
├── domain/                  
├── schemas/                   
├── repositories/              
├── services/                  
├── api/routes/                
└── tests/

5- Como Execultar o Projeto

5.1. Instale as dependências necessárias:
As quatros dependências necessárias desse Projeto são:
FastAPI/ Pydantic/ Pytest/ Uvicorn.
No terminal, execute o seguinte comando para instalar os pacotes utilizados:
pip install fastapi pydantic uvicorn pytest

5.2. Inicie o servidor da API:
Na raiz do projeto (onde se encontra o ficheiro main.py), execute:
uvicorn main:app --reload

5.3. Aceda à documentação interativa:
Abra o navegador e aceda a http://127.0.0.1:8000/docs para testar os endpoints diretamente através do Swagger UI.

6- Como Executar os Testes
O projeto conta com uma suite completa de testes automatizados para garantir a integridade das regras de negócio (cancelamentos, observações, prioridades e ordenação da fila).
Para executar os testes, utilize o comando abaixo na raiz do projeto:
pytest -q

Observação: Todos os 7 testes obrigatórios da atividade devem passar com sucesso, indicados por pontos verdes

# Projeto de Automação Behave com Page Objects

## Visão Geral

Este projeto é uma suíte de automação **BDD (Behavior Driven Development)** usando **Behave** e **Selenium**, voltada para testes do formulário de cadastro de entregadores do site **Buger Eats**.

O objetivo principal é validar cenários de **sucesso** e **falha** no cadastro, incluindo campos obrigatórios, validações de CPF, email, CEP e upload de documentos.

Principais tecnologias e técnicas utilizadas:

- Python 3.13
- Selenium WebDriver
- Behave (BDD)
- Docker e Selenium Grid (para execução distribuída)
- Padrão Page Object Model (POM)
- Estrutura de fixtures e steps separadas
- Relatórios e screenshots automáticos

---

## Como Executar os testes

### Pré-requisitos

- Python 3.13
- Docker e Docker Compose
- Navegador Chrome
- Pip packages: `selenium`, `behave`, etc.

Instalação de dependências:

```bash
pip install -r requirements.txt
```

### Rodando Selenium Grid via Docker

```bash
cd docker
docker-compose up -d
```

- Acessa o Selenium Hub em `http://localhost:4444`
- Nós Chrome preparados para execução paralela

### Executando testes

### Testes gerais, sucesso, falha e específicos:

```bash
behave
```

### Executar cenários específicos por tag:

```bash
behave --tags=@success       # Apenas cenários de sucesso
behave --tags=@failure       # Apenas cenários de falha
behave --tags=@cpf           # Apenas cenários de CPF
```

### Executar em paralelo (com BehaveX):

```bash
behavex --parallel-processes=6
```

- Suporta execução **por cenário** ou **por feature**
- Suporta controle de ordem e retry com tags específicas
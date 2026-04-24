# 🛒 Carrinho de Compras com BDD (pytest-bdd)

Este projeto é um exercício prático de **Behavior-Driven Development (BDD)** utilizando Python, `pytest` e `pytest-bdd`.

O objetivo é demonstrar como transformar um requisito de negócio em **cenários executáveis**, conectando linguagem natural (Gherkin) ao código Python.

---

## 📌 Objetivo

Implementar um sistema simples de carrinho de compras com as seguintes regras:

* O usuário pode adicionar produtos ao carrinho
* O valor total deve ser atualizado corretamente
* Não é permitido adicionar produtos com quantidade maior que o estoque disponível
* Deve ocorrer erro em caso de estoque insuficiente

---

## 🧱 Estrutura do Projeto

```
bdd_carrinho_compras/
│
├── carrinho.feature     # Cenários em Gherkin (BDD)
├── carrinho.py          # Regra de negócio (código Python)
├── test_carrinho.py     # Testes automatizados (pytest-bdd)
└── README.md            # Documentação do projeto
```

---

## 🧪 Tecnologias Utilizadas

* Python 3.x
* pytest
* pytest-bdd

---

## 🧠 Conceitos Aplicados

* Behavior-Driven Development (BDD)
* Gherkin (Feature, Scenario, Given, When, Then)
* Testes automatizados
* Separação entre regra de negócio e testes
* Tratamento de exceções em testes

---

## 📄 Cenários Implementados

### ✔️ Cenário 1: Adicionar produto com sucesso

* Adiciona produto com estoque suficiente
* Atualiza total do carrinho
* Atualiza quantidade de itens

### ❌ Cenário 2: Estoque insuficiente

* Tenta adicionar mais produtos do que o disponível
* Sistema lança erro: `"Estoque insuficiente"`

---

## ⚙️ Como Executar o Projeto

### 1. Instalar dependências

```bash
python -m pip install pytest pytest-bdd
```

---

### 2. Executar os testes

```bash
python -m pytest test_carrinho.py -v
```

---

## ✅ Resultado Esperado

```bash
2 passed in X.XXs
```

---

## 🔍 Exemplo de Regra de Negócio

```python
def adicionar_produto(carrinho, quantidade_desejada, estoque_disponivel, preco_unitario):
    if quantidade_desejada <= estoque_disponivel:
        carrinho["itens"] += quantidade_desejada
        carrinho["total"] += quantidade_desejada * preco_unitario
    else:
        raise ValueError("Estoque insuficiente")
```

---

## 💡 Por que usar BDD?

O BDD permite:

* Melhor comunicação entre negócio e desenvolvimento
* Documentação viva do sistema
* Garantia de que o comportamento esperado está sendo testado
* Redução de ambiguidades nos requisitos

---

## 🚀 Possíveis Melhorias

* Suporte a múltiplos produtos
* Remoção de itens do carrinho
* Aplicação de descontos
* Estrutura orientada a objetos (classes)
* Integração com banco de dados

---

## 🏁 Conclusão

Este projeto demonstra de forma prática como alinhar:

**Requisito de Negócio → Cenário BDD → Teste Automatizado → Código**

Garantindo que o sistema funcione exatamente como esperado.

---

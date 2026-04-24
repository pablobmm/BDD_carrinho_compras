Feature: Carrinho de compras

  Scenario: Adicionar um produto com sucesso
    Given que o carrinho está vazio
    When eu adicionar 2 unidades com estoque 10 e preço 50
    Then o total do carrinho deve ser 100
    And a quantidade de itens deve ser 2

  Scenario: Tentar adicionar produto sem estoque suficiente
    Given que o carrinho está vazio
    When eu adicionar 5 unidades com estoque 2 e preço 50
    Then deve ocorrer um erro de estoque insuficiente
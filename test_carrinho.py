import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from carrinho import criar_carrinho, adicionar_produto

scenarios("carrinho.feature")

@given("que o carrinho está vazio", target_fixture="carrinho")
def carrinho_vazio():
    return criar_carrinho()


@when(parsers.parse("eu adicionar {quantidade:d} unidades com estoque {estoque:d} e preço {preco:d}"))
def adicionar(carrinho, quantidade, estoque, preco):
    try:
        adicionar_produto(carrinho, quantidade, estoque, preco)
    except ValueError as e:
        carrinho["erro"] = str(e)


@then(parsers.parse("o total do carrinho deve ser {total_esperado:d}"))
def verificar_total(carrinho, total_esperado):
    assert carrinho["total"] == total_esperado


@then(parsers.parse("a quantidade de itens deve ser {itens_esperados:d}"))
def verificar_itens(carrinho, itens_esperados):
    assert carrinho["itens"] == itens_esperados


@then("deve ocorrer um erro de estoque insuficiente")
def verificar_erro(carrinho):
    assert "erro" in carrinho
    assert carrinho["erro"] == "Estoque insuficiente"
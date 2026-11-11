# Atividade 4: Testes Automatizados do LocalEats

**Unidade Curricular:** Qualidade de Software
**Projeto:** LocalEats (https://local-eats-unisenac.vercel.app/)
**Modalidade:** Individual
**Integrante:** Erick Peter

## Identificação dos testes

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
|----|-----------|------|--------------------------|------------------|
| TU01 | Erick Peter | Unitário | Pedido de R$ 150 recebe 10% de desconto | tests/test_regras_localeats.py::test_pedido_de_150_recebe_desconto_de_10_por_cento |
| TU02 | Erick Peter | Unitário | Pedido abaixo de R$ 100 não recebe desconto | tests/test_regras_localeats.py::test_pedido_abaixo_de_100_nao_recebe_desconto |
| TU03 | Erick Peter | Unitário (borda) | Pedido de exatamente R$ 100 recebe desconto | tests/test_regras_localeats.py::test_pedido_de_exatamente_100_recebe_desconto |
| TU04 | Erick Peter | Unitário (exceção) | Valor negativo gera ValueError (`pytest.raises`) | tests/test_regras_localeats.py::test_valor_negativo_gera_value_error |
| TF01 | Erick Peter | Funcional | Tela de login: redirecionamento, título, campos e preenchimento do e-mail | tests/test_localeats.py::test_tela_de_login_apresenta_campos_e_aceita_email |
| TF02 | Erick Peter | Funcional (opcional) | Aba "Criar Conta" exibe o formulário de cadastro | tests/test_localeats.py::test_alternar_para_criar_conta_exibe_formulario_de_cadastro |

## Parte 1: TDD de Erick Peter

- **Regra escolhida:** Regra 2, `calcular_desconto(valor_pedido)`.
- **Primeiro teste escrito:** `test_pedido_de_150_recebe_desconto_de_10_por_cento` (`calcular_desconto(150) == 15`).
- **Por que o teste falhou inicialmente:** a função ainda não existia (`ImportError`/`NameError`).
- **Implementação mínima realizada:** função que retornava `valor_pedido * 0.10`.
- **Segundo teste escrito:** `test_pedido_abaixo_de_100_nao_recebe_desconto` (`calcular_desconto(80) == 0`). Falhou, pois a versão mínima retornava 8.
- **Melhoria ou refatoração realizada:** inclusão da condição `< 100` retornando 0, da validação de valores negativos (`ValueError`) e extração das constantes `VALOR_MINIMO_DESCONTO` e `PERCENTUAL_DESCONTO`. Depois foram adicionados o teste de borda (R$ 100) e o teste com `pytest.raises`.

## Parte 2: Testes funcionais com Playwright

- **Observação da exploração:** ao acessar o LocalEats sem sessão, o sistema redireciona para `login.html`. Por isso os fluxos automatizados partem da tela de login.
- **TF01:** acessa o LocalEats, verifica o redirecionamento para `login.html`, o título "Entrar | Local Eats" e a mensagem "Bem-vindo ao app de Qualidade de Software"; depois preenche o campo de e-mail e verifica o valor digitado.
- **TF02:** clica na aba "Criar Conta" e verifica que o campo "Nome Completo" e o botão "Registrar" ficam visíveis.
- Locators usados: `get_by_role`, `get_by_text` e `get_by_placeholder`. Não há `time.sleep`; as esperas são as automáticas das assertions `expect`.

## Falha encontrada e corrigida

Na primeira execução completa, os 2 testes funcionais falharam e os 4 unitários passaram (2 failed, 4 passed). Os testes assumiam que a página inicial abriria direto, mas o LocalEats redireciona para `login.html` quando não há sessão. A correção foi reescrever os dois testes para partirem da tela de login. Na execução seguinte, os 6 testes passaram.

## Como executar

```powershell
pip install -r requirements.txt
playwright install
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

## Uso de inteligência artificial

- **Ferramenta utilizada:** Claude (Anthropic).
- **Como a ferramenta foi utilizada:** apoio para estruturar os arquivos,e o rascunho deste documento.
- **Uma sugestão que precisou ser alterada ou rejeitada:** os testes funcionais sugeridos inicialmente esperavam a página inicial com categorias de restaurantes. 
- **Como o código sugerido foi verificado:** execução dos testes com pytest, leitura do código e conferência dos textos na página real.

## Relatório

Ver `relatorio-pytest.txt` (gerado com o comando acima).

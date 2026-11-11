import re

from playwright.sync_api import Page, expect

URL = "https://local-eats-unisenac.vercel.app/"


# Responsável: Erick Peter
def test_tela_de_login_apresenta_campos_e_aceita_email(page: Page):
    page.goto(URL)

    # Sem sessão, o LocalEats redireciona para a tela de login
    expect(page).to_have_url(re.compile(r"login\.html"))
    expect(page).to_have_title("Entrar | Local Eats")
    expect(page.get_by_text("Bem-vindo ao app de Qualidade de Software")).to_be_visible()

    # Interação: preencher o campo de e-mail
    campo_email = page.get_by_placeholder("teste@teste.com").first
    expect(campo_email).to_be_visible()
    campo_email.fill("aluno@exemplo.com")
    expect(campo_email).to_have_value("aluno@exemplo.com")


# Responsável: Erick Peter
def test_alternar_para_criar_conta_exibe_formulario_de_cadastro(page: Page):
    page.goto(URL)

    # Interação: abrir a aba "Criar Conta"
    page.get_by_role("button", name="Criar Conta").click()

    expect(page.get_by_text("Nome Completo")).to_be_visible()
    expect(page.get_by_role("button", name="Registrar")).to_be_visible()

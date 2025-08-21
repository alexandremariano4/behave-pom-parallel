# language:pt

    Funcionalidade: Cadastro de usuário

    @success
    Cenário: Acessar o formulário de cadastro e preencher os dados corretamente 
        Dado que estou na página principal 
        Quando clico no botão de "Cadastre-se para fazer entregas"
        E preencho o formulário de cadastro com os dados abaixo
            | name  |     cpf     |     email       |   phone     |   cep    | number | complement | deliveryMethod|
            | Teste | 00000014141 | teste@gmail.com | 31984679630 | 30855184 | 50     |    casa    |     Moto      |
        E envio uma imagem da cnh
        E clico no botão "Cadastre-se para fazer entregas"
        Então devo receber a mensagem de confirmação "Recebemos os seus dados. Fique de olho na sua caixa de email, pois e em breve retornamos o contato."

    @failure @cpf
    Cenário: Acessar o formulário de cadastro e preencher CPF incorreto
        Dado que estou na página principal 
        Quando clico no botão de "Cadastre-se para fazer entregas"
        E preencho o formulário de cadastro com os dados abaixo
            | name  |     cpf     |     email       |   phone     |   cep    | number | complement | deliveryMethod|
            | Teste | abcdefghijk | teste@gmail.com | 31984679630 | 30855184 | 50     |    casa    | Bike Elétrica |
        E envio uma imagem da cnh
        E clico no botão "Cadastre-se para fazer entregas"
        Então devo receber a mensagem de erro "Oops! CPF inválido"

    @failure @email
    Cenário: Acessar o formulário de cadastro e preencher Email incorreto
        Dado que estou na página principal 
        Quando clico no botão de "Cadastre-se para fazer entregas"
        E preencho o formulário de cadastro com os dados abaixo
            | name  |     cpf     |     email       |   phone     |   cep    | number | complement | deliveryMethod|
            | Teste | 00000014141 |    incorreto    | 31984679630 | 30855184 | 50     |    casa    |  Van/Carro    |
        E envio uma imagem da cnh
        E clico no botão "Cadastre-se para fazer entregas"
        Então devo receber a mensagem de erro "Oops! Email com formato inválido."

    @failure @cep
    Cenário: Acessar o formulário de cadastro e preencher CEP incorreto
        Dado que estou na página principal 
        Quando clico no botão de "Cadastre-se para fazer entregas"
        E preencho o formulário de cadastro com os dados abaixo
            | name  |     cpf     |     email       |   phone     |   cep    | number | complement | deliveryMethod|
            | Teste | 00000014141 | teste@gmail.com | 31984679630 | abcdefg  | 50     |    casa    |     Moto      |
        Então devo receber a mensagem de erro "Informe um CEP válido"

    @failure @imagem
    Cenário: Acessar o formulário de cadastro, preencher e não enviar a imagem
        Dado que estou na página principal 
        Quando clico no botão de "Cadastre-se para fazer entregas"
        E preencho o formulário de cadastro com os dados abaixo
            | name  |     cpf     |     email       |   phone     |   cep    | number | complement | deliveryMethod|
            | Teste | 00000014141 | teste@gmail.com | 31984679630 | 30855184 | 50     |    casa    |     Moto      |
        E clico no botão "Cadastre-se para fazer entregas"
        Então devo receber a mensagem de erro "Adicione uma foto da sua CNH"
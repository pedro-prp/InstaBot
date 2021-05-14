# InstaBot

## 1. Descrição
Projeto desenvolvido com objetivo de desenvolver um bot para *acesso* e *interação* com o **instagram web** por meio de um navegador autômato.

## 2. Tecnologias utilizadas

* Python
* Selenium

## 3. Funções
Atualmente o bot é capaz de realizar três funções principais:


* Login
* Acesso a um publicação
* Comentários automáticos.

## 4. Como rodar

### 4.1 Dependências
*  Primeiro é necessário possuir o navegador Firefox instalado.

 * Após isso temos a instalação do selenium, a qual pode ser realizada com o seguinte comando:

```
$ pip3 install selenium
```

### 4.2 Geckodriver
Para a automação do firefox é necessário informar ao computador onde se encontra o arquivo geckodriver. 

Com o seguinte comando na raiz do projeto:

```
$ export PATH=$PATH:.
```

### 4.3 Configuração de Login, senha e publicação
Basta abrir o arquivo **app.py** e alterar os dados de login, senha e publicação no dicionário **data**. Além disso é possível também alternar a frequência dos comentários realizados pelo bot.

### 4.4 Finalmente rodando
Para rodar so se faz necessário rodar o seguinte comando na raiz do projeto:

```
python3 app.py
```
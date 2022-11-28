<p align="center"><img src="https://user-images.githubusercontent.com/101838119/204174423-b62e560f-9a41-4674-86b0-52b0cd682e52.png"></p>


<p align="center">
<a href="https://labinventary-ow6376zhsq-uc.a.run.app/"><img src="https://img.shields.io/badge/API-online-brightgreen"></a>
</p>

<h1>⚙️ LABinventory API </h1>

<p> API desenvolvida em Flask para o projeto final do Curso DEVInHouse. A API foi feita para as requisições do frontend de uma Single Page Application desenvolvida em Vue.js</P>

# ⚙️ Instalação

## Setup do Projeto

```bash
# Clone este repositório
$ git clone https://github.com/DEVin-ConectaNuvem/M3P2-LABinventory-BackEnd-Squad1
```

### Instale as dependências

```sh
poetry install
```

### Compilação para desenvolvimento

```sh
poetry run flask run
```



<hr>

<h2> 🔑 ENDPOINT: (POST) /users/create </h2>

<p> Endpoint para a criação de conta. </p>

<h5> Body params: <h5>


```js
{
    "email": "", 
    "password": ""
}
```

<hr>


<h2> 🔑 ENDPOINT: (POST) /users/auth/google </h2>

<p> Esse endpoint ao realizar a requisição retorna a URL para realizar o seu login com a conta Google no APP. </p>

<hr>

<h2>  🔑 ENDPOINT: (GET) /users/callback </h2>

<p> Esse endpoint é o callback do Google onde pega as informações do usuario e o retorna ao Frontend </p>

<hr>

<h2> 🔑 ENDPOINT: (POST) /users/login </h2> 

<p> Endpoint para o login de conta. </p>

<h5> Body params: <h5>


```js
{
    "email": "", 
    "password": ""
}
```

<hr>

<h2> 📚 ENDPOINT: (POST) /inventory/create </h2> 

<p> Endpoint para a criação de item. </p>

<h5> Body params: <h5>


```js
{
    "codPatrimonio": "",
    "title": "",
    "description": "",
    "category": "",
    "value": 0,
    "brand": "",
    "model": ""
}
```

<hr>

<h2> 📚 ENDPOINT: (GET) /inventory/ </h2> 

<p> Endpoint para o retorno de dados dos itens. </p>

<hr>

<h2> 📚 ENDPOINT: (GET) /inventory/<id> </h2> 

<p> Endpoint para pesquisa de item pelo ID. </p>

<h5> Query params exemplo: <h5>


```js
example: http://localhost:5000/inventory/2
```

<hr>

<h2> 📚 ENDPOINT: (GET) /inventory/list </h2> 

<p>  Endpoint para o retorno de dados dos itens na tela de empréstimo. </p>

<hr>

<h2> 📚 ENDPOINT: (PATCH) /inventory/update </h2> 

<p> Endpoint para atualizar um item. </p>

<h5> Body params: <h5>


```js
{
  id: ""
  dataset: {
       title: ""
   }
}
```

<hr>

<h2> 📚 ENDPOINT: (DELETE) /inventory/delete </h2> 

<p> Endpoint para deletar um item. </p>

<h5> Body params: <h5>


```js
{
  id: ""
}
```

<hr>
<h2> 📚 ENDPOINT: (GET) /inventory/analytics </h2> 

<p> Endpoint para retornar os dados do inventario. </p>

<hr>

<h2> 🧍 ENDPOINT: (POST) /employees/create </h2>

<p> Endpoint para a criação de conta. </p>

<h5> Body params: <h5>


```js
{
    "name": "",
    "email": "",
    "phone": "",
    "position": "",
    "gender": "",
    "zipcode": "",
    "birthDay": "",
    "city": "",
    "state": "",
    "neighborhood": "",
    "street": "",
    "houseNumber": 0,
    "complement": "",
    "reference": ""
}
```

<hr>

<h2> 🧍 ENDPOINT: (GET) /employees/ </h2> 

<p> Endpoint para o retorno de dados dos colaboradores. </p>

<hr>

<h2> 🧍 ENDPOINT: (GET) /employees/<id> </h2> 

<p> Endpoint para pesquisa de colaborador pelo ID. </p>

<h5> Query params exemplo: <h5>


```js
example: http://localhost:5000/employees/2
```

<hr>

<h2> 🧍 ENDPOINT: (PATCH) /employees/update </h2> 

<p> Endpoint para atualizar um item. </p>

<h5> Body params: <h5>


```js
{
  id: ""
  dataset: {
       name: ""
   }
}
```

<hr>

<h2> 🧍 ENDPOINT: (DELETE) /employees/delete </h2> 

<p> Endpoint para deletar um colaborador. </p>

<h5> Body params: <h5>


```js
{
  id: ""
}
```


## 👋 Desenvolvedores

|          [<sub>Breno Martins</sub><br><img src="https://avatars.githubusercontent.com/u/95316873?v=4" width=100><br>](https://github.com/Breno-MT)           | [<sub>Luiz Gustavo Seemann</sub><br><img src="https://avatars.githubusercontent.com/u/101838119?v=4" width=100><br>](https://github.com/Gustavo-Seemann) | [<sub>Eduardo Martins Ribeiro</sub><br><img src="https://avatars.githubusercontent.com/u/98466110?v=4" width=100><br>](https://github.com/edumartinsrib) |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [<sub>Rafael Telles Carneiro</sub><br><img src="https://avatars.githubusercontent.com/u/98103640?v=4" width=100><br>](https://github.com/rafatellescarneiro) |       [<sub>Bruno V</sub><br><img src="https://avatars.githubusercontent.com/u/100861122?v=4" width=100><br>](https://github.com/brunobedretchuk)        |       [<sub>Thiago William</sub><br><img src="https://avatars.githubusercontent.com/u/94487053?v=4" width=100><br>](https://github.com/ThiagoW21)        |

# 🤝 Agradecimentos:

A realização deste projeto apenas foi possível em razão do excelente ensino disponibilizado por toda a equipe DEVInHouse e ConectaNuvem!

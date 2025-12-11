# 🔐 Sistema de Login em Python (Desafio 2)

Este projeto é um **sistema simples de cadastro e login** utilizando arquivos `.txt` para armazenar usuários e senhas.

É ideal para iniciantes que estão aprendendo:

* Manipulação de arquivos em Python (`open`, leitura e escrita)
* Estrutura de menus
* Lógica de validação de dados
* Tratamento de erros básicos

---

## 📌 Funcionalidades

✔ Cadastro de novos usuários
✔ Armazenamento de login e senha em arquivo `.txt`
✔ Validação de senha (confirmação)
✔ Menu simples e intuitivo
✔ Sistema pronto para receber a função **login** futuramente

---

## 🗂 Estrutura do Arquivo

O arquivo `Cadastros.txt` armazena dados no formato:

```
usuario;senha
```

Cada linha representa um usuário.

Exemplo:

```
renan;1234
admin;abcd
```

---

## ▶ Como usar

1. Execute o programa:

```bash
python login.py
```

2. Escolha uma opção no menu:

```
1 - Cadastro
2 - Entrar
0 - Sair
```

3. Para cadastrar:

   * Informe usuário
   * Informe a senha
   * Confirme a senha

---

## 📂 Código Principal (resumo)

```python
menu_entrada()
```

O programa inicia abrindo o menu principal.

---

## 🚀 Melhorias futuras

Você pode evoluir este projeto adicionando:

* [ ] Função de login
* [ ] Ocultar senha digitada (usando `getpass`)
* [ ] Validação de usuário duplicado
* [ ] Senhas criptografadas (`hashlib` ou `bcrypt`)
* [ ] Interface colorida
* [ ] Sistema de tentativas (bloquear após erros repetidos)

---

## 📄 Licença

Este projeto é livre para estudo e modificação.

---

Se quiser, posso adicionar GIF de demonstração, cores, instruções avançadas ou transformar isso em um projeto mais robusto! 🚀

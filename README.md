# 📦 Backend API – Django REST Framework

API REST desenvolvida em **Django + Django REST Framework**, com foco em **boas práticas de backend**, autenticação segura via **JWT**, organização de código e separação de responsabilidades.

O projeto foi construído com o objetivo de estudo, portfólio e aplicação real de conceitos de **APIs RESTful**, autenticação, permissões e regras de negócio no backend.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Django
- Django REST Framework (DRF)
- Simple JWT
- PostgreSQL (ou SQLite para testes)
- Insomnia (testes de endpoints)
- dotenv (variáveis de ambiente)

---

## 📁 Estrutura do Projeto
📁project/
│
├──📁 apps/
│ ├── 📁users/ # Usuários e perfil
│ ├──📁 auth/ # Autenticação e JWT
│
├── 📁core/ # Configurações globais
├── </> manage.py
└──🧾requirements.txt




---

## 🔐 Autenticação

A autenticação é feita utilizando **JWT (JSON Web Token)**.

### Fluxo de autenticação:
1. Registro de usuário
2. Login (gera access e refresh token)
3. Uso do token nos endpoints protegidos
4. Refresh de token
5. Logout
6. Mudança de senha

---


## 📌 Endpoints Principais

### 🔑 Autenticação

| Método | Endpoint | Descrição |
|------|--------|----------|
| POST | `/api/users/create/` | Registro de usuário |
| POST | `/api/token/` | Login e geração de tokens |
| POST | `/api/token/refresh/` | Refresh do token |


---

### 👤 Usuários

| Método | Endpoint | Descrição |
|------|--------|----------|
| GET | `/api/users/me/` | Dados do usuário autenticado |
| PUT | `/api/users/me/` | Atualização de perfil |
| PUT  | `/api/users/change-password/` | Alteração de senha |
| DELETE | `/api/users/me/` | Exclusão da conta |

---


## 🛡️ Segurança

- Autenticação obrigatória nos endpoints protegidos
- Uso de `set_password()` para criptografia de senha
- Validações de permissão personalizadas
- Variáveis sensíveis armazenadas em `.env`
- Tokens JWT com tempo de expiração

---

## 🧪 Testes

Os endpoints foram testados utilizando **Insomnia**, validando:
- Respostas HTTP corretas (200, 201, 400, 401, 403)
- Autenticação via Bearer Token
- Validação de erros e permissões

---




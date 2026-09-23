# 🏥 Plataforma de Onboarding e Treinamento Corporativo (Multi-Tenant & White-Label)

> Sistema web desenvolvido em **Python + Django** projetado para automatizar e padronizar o treinamento e integração de novos colaboradores em empresas, eliminando a necessidade de acompanhamento presencial contínuo por funcionários veteranos.

---

## 🎯 Sobre o Projeto

A rotatividade de funcionários em empresas gera um alto custo de tempo para os profissionais mais experientes, que precisam pausar suas atividades diárias para ensinar processos operacionais básicos, uso de softwares e normas de biossegurança aos recém-contratados.

Esta plataforma resolve esse gargalo ao centralizar:
- **Trilhas de Aprendizado por Cargo** (vídeos, tutoriais e procedimentos operacionais padrão - POPs).
- **Checklists Interativos** para acompanhamento da rotina nos primeiros 30/60 dias.
- **Quizzes de Fixação** para validação do aprendizado.
- **Painel de Métricas** para acompanhamento em tempo real pelo gestor/RH.

---

## 🏗️ Arquitetura Multi-Tenant & White-Label

A plataforma utiliza uma **única base de código** para atender múltiplos clientes de forma isolada e segura:
* **Isolamento de Dados:** Cada empresa possui seus próprios colaboradores, cargos, trilhas e relatórios.
* **White-Label Dinâmico:** Cada empresa acessa por um identificador exclusivo na URL (`/<slug-da-empresa>/login/`), e o sistema carrega automaticamente a **logo**, o **nome** e a **paleta de cores da marca da empresa** via variáveis CSS sem necessidade de alterações no código-fonte.
* **Segurança de Acesso:** Usuários de uma empresa são impedidos de autenticar no portal de outra empresa.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Framework Web:** Django (Arquitetura MVT)
* **Frontend / Estilização:** Django Templates + Tailwind CSS (via CDN)
* **Autenticação:** Custom User Model com login por e-mail e papéis (Superadmin, Gestor, Colaborador)
* **Processamento de Imagens:** Pillow
* **Metodologia de Gestão:** Scrum / Ágil (Product Backlog documentado em [`docs/backlog.md`](docs/backlog.md))

---

## 📊 Status do Desenvolvimento (Scrum)

- [x] **Sprint 1: Fundação Multi-Tenant & Autenticação** *(Concluída)*
  - Setup do projeto e estrutura modular de apps (`core`, `empresas`, `usuarios`).
  - Modelagem de Empresa (Tenant Base) com slug dinâmico e paleta de cores.
  - Custom User Model com autenticação por e-mail e vínculo a cargos.
  - Django Admin customizado com suporte a multi-empresas.
  - Fluxo de login e dashboard inicial com isolamento de dados por empresa.
- [ ] **Sprint 2: Gestão de Trilhas, Módulos e Consumo de Aulas** *(Próxima)*
- [ ] **Sprint 3: Checklists de Rotina (POPs) e Quizzes de Avaliação**
- [ ] **Sprint 4: Dashboard do Gestor (Progresso dos Alunos) e Relatórios**

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos:
* Python 3.10+ instalado
* Git instalado

### Passo a passo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/arthur-rn/plataforma-treinamento-onboarding.git
   cd plataforma-treinamento-onboarding
   ```

2. **Crie e ative o ambiente virtual:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Instale as dependências:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Aplique as migrações no banco de dados:**
   ```powershell
   python manage.py migrate
   ```

5. **Crie um superusuário (Administrador Geral):**
   ```powershell
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento:**
   ```powershell
   python manage.py runserver
   ```

7. **Acesse no navegador:**
   * Painel Administrativo: `http://127.0.0.1:8000/admin/`
   * Portal da Empresa cadastrada: `http://127.0.0.1:8000/<slug-da-empresa>/login/`

---

## 📄 Licença e Autoria

Projeto desenvolvido por **Arthur** como projeto pessoal de portfólio e aplicação prática para integração de colaboradores em empresas.

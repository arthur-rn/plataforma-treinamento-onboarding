# 📋 Planejamento Scrum & Product Backlog

## 🎯 Visão do Produto
Desenvolver uma plataforma web de onboarding e treinamento corporativo **multi-tenant** e **white-label**, que permita a empresas capacitar novos colaboradores de forma autônoma, padronizada e mensurável, reduzindo drasticamente a necessidade de acompanhamento presencial contínuo por funcionários veteranos.

---

## 👥 Personas

1. **Novo Colaborador:**
   * *Perfil:* Funcionário recém contratado.
   * *Objetivo:* Aprender a rotina do cargo, dominar procedimentos operacionais padrão (POPs) e ferramentas da clínica de forma autônoma e segura.
2. **Gestor / Líder da Empresa:**
   * *Perfil:* Responsável técnico, gerente de unidade ou gerente de RH.
   * *Objetivo:* Acompanhar a evolução dos novatos, garantir conformidade com normas (ex: biossegurança) e gerenciar conteúdos de treinamento.
3. **Superadministrador (Plataforma):**
   * *Perfil:* Administrador do sistema SaaS.
   * *Objetivo:* Cadastrar novas empresas clientes e gerenciar o ecossistema multi-tenant.

---

## 📌 Definições Ágeis (Padrões de Qualidade)

### Definition of Ready (DoR) - Quando uma história pode entrar na Sprint:
- [x] O valor de negócio está claro ("Como... Quero... Para...").
- [x] Os critérios de aceite estão definidos e testáveis.
- [x] Dependências de banco de dados ou arquitetura foram mapeadas.

### Definition of Done (DoD) - Quando uma história é considerada concluída:
- [x] Código implementado seguindo boas práticas do Django.
- [x] Migrations criadas e aplicadas sem erros.
- [x] Regras de isolamento multi-tenant validadas.
- [x] Commit atômico com mensagem semântica (ex: `feat: ...`, `fix: ...`).
- [x] Documentação técnica atualizada se necessário.

---

## 🗺️ Mapa de Épicos

* **EP-01:** Fundação Multi-tenant e Gestão de Acessos
* **EP-02:** Gestão de Conteúdo e Trilhas de Aprendizado
* **EP-03:** Experiência do Colaborador (Área do Aluno)
* **EP-04:** Checklists Operacionais (POPs) e Quizzes de Fixação
* **EP-05:** Painel de Acompanhamento e Métricas do Gestor
* **EP-06:** White-label e Customização de Marca

---

## 🚀 Sprint 1: Fundação Multi-tenant e Gestão de Acessos
**Meta da Sprint:** Criar a estrutura base do projeto Django, os modelos de Empresa, Cargo e Usuário customizado, garantindo isolamento de dados e autenticação funcional.

### 📝 Histórias de Usuário da Sprint 1

#### **US-01: Inicialização da Arquitetura do Projeto**
* **Como** desenvolvedor do sistema,
* **Quero** inicializar o projeto Django com separação modular em apps (`core`, `empresas`, `usuarios`),
* **Para que** a arquitetura seja escalável e de fácil manutenção.
* **Critérios de Aceite:**
  - [ ] Projeto Django criado com configurações separadas (desenvolvimento/produção).
  - [ ] Apps `empresas`, `usuarios` e `core` registrados no `INSTALLED_APPS`.
  - [ ] Banco de dados SQLite inicializado localmente.

#### **US-02: Modelo de Empresa (Tenant Base)**
* **Como** administrador da plataforma,
* **Quero** cadastrar empresas com dados cadastrais e slug único,
* **Para que** diferentes empresas possam usar o mesmo sistema de forma isolada.
* **Critérios de Aceite:**
  - [ ] Modelo `Empresa` criado com `nome`, `slug` único, `cnpj` (opcional), `criado_em` e `ativo`.
  - [ ] O `slug` deve ser gerado automaticamente a partir do nome se não informado.

#### **US-03: Modelo Customizado de Usuário e Cargos**
* **Como** gestor da empresa,
* **Quero** cadastrar cargos e vincular novos colaboradores à minha empresa e ao cargo deles,
* **Para que** os treinamentos futuros sejam direcionados automaticamente.
* **Critérios de Aceite:**
  - [ ] Modelo `Cargo` vinculado a uma `Empresa`.
  - [ ] `CustomUser` estendendo `AbstractUser` do Django, com campos `email` (único para login), `empresa` (ForeignKey) e `cargo` (ForeignKey).
  - [ ] Papéis de usuário definidos: `ADMIN_EMPRESA` e `COLABORADOR`.

#### **US-04: Django Admin com Suporte a Multi-empresa**
* **Como** gestor ou administrador,
* **Quero** acessar o Django Admin para gerenciar os cadastros iniciais,
* **Para que** possamos cadastrar a primeira empresa, cargos e usuários de teste.
* **Critérios de Aceite:**
  - [ ] Modelos registrados no `admin.py` com listagens claras e filtros.
  - [ ] Criação de um superuser local para testes.

#### **US-05: Fluxo de Autenticação (Login / Logout)**
* **Como** colaborador ou gestor,
* **Quero** fazer login utilizando meu e-mail e senha,
* **Para que** eu seja direcionado para a área correspondente do sistema.
* **Critérios de Aceite:**
  - [ ] Tela de login funcional via e-mail e senha.
  - [ ] Mensagens de erro claras para credenciais inválidas.
  - [ ] Redirecionamento após login e rota de logout funcional.

---

## 🔮 Backlog das Próximas Sprints

* **Sprint 2:** Modelagem de Trilhas, Módulos, Aulas (Vídeo/PDF) e interface do Aluno.
* **Sprint 3:** Checklists interativos de POPs diários e Quizzes de fixação com notas.
* **Sprint 4:** Painel do Gestor (Progresso dos alunos) e White-Label (Cores e Logo da clínica).
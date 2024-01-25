Segue o status completo da Análise e Desenvolvimento (AeD) da IDP API:

# Status da Análise e Desenvolvimento (AeD) da IDP API

Linha de status atual: A escrever discussão e decisão da etapa 3.1.

## 1. Análise de Requisitos

### 1.1. Avaliação dos Requisitos Funcionais (RFs)

#### 1.1.1. Processamento de Texto para Conversão (RF1-API e RF2-API):

- **RF1-API**: A API necessita de um endpoint que aceite textos em inglês padrão e os converta para o inglês EWD (English with Diacritics). Isso implica no desenvolvimento de um algoritmo capaz de analisar o texto em inglês e aplicar as regras específicas da Ortografia Didática PI (ODPI) para adicionar os acentos diacríticos necessários.

- **RF2-API**: Deve haver suporte para diferentes formatos de entrada, como texto puro (strings) e formatos estruturados (JSON, XML). Isso sugere a implementação de parsers flexíveis que possam processar diferentes tipos de entrada, reconhecendo e convertendo o conteúdo textual adequadamente.

#### 1.1.2. Preservação da Estrutura e Formatação do Texto Original (RF3-API):

- A API deve manter a estrutura e formatação originais do texto, o que é crucial para documentos com formatação complexa (como documentos XML ou formatados em Markdown). Portanto, o algoritmo de processamento de texto não deve alterar a formatação original, mas apenas adicionar os acentos diacríticos onde necessário. Isso pode ser alcançado através de uma abordagem que separa o conteúdo textual da formatação, processa o texto e, em seguida, reintegra-o mantendo a formatação original.

#### 1.1.3. Análise dos Requisitos Funcionais (RF4-API a RF6-API)

Nesta sub-etapa, o foco é na determinação de tecnologias e protocolos para a construção da interface da API, bem como na definição de parâmetros de customização. Os requisitos funcionais RF4-API a RF6-API serão detalhados a seguir:

- RF4-API: Interface RESTful e Documentação

  - **Objetivo**: Desenvolver uma interface de API RESTful que seja fácil de integrar em diferentes plataformas e linguagens de programação.
  - **Estratégias**:
    - Definir os principais endpoints da API, incluindo, mas não se limitando a, conversão de texto, consulta de regras de diacríticos e configurações de usuário.
    - Utilizar padrões de design de API RESTful para garantir escalabilidade e manutenção.
    - Desenvolver uma documentação abrangente e clara, fornecendo exemplos de uso, descrições de parâmetros e formatos de resposta.

- RF5-API: Ajustes e Customizações na Conversão

  - **Objetivo**: Permitir que os usuários ajustem e personalizem o processo de conversão através de parâmetros específicos na API.
  - **Estratégias**:
    - Implementar parâmetros na API que permitam a customização do nível de aplicação de diacríticos, escolha de variantes linguísticas, entre outros.
    - Garantir que a API possa lidar com diferentes tipos de input, como textos em formatos variados e listas de palavras.

- RF6-API: Endpoints para Configurações de Usuário

  - **Objetivo**: Oferecer endpoints específicos para configurações de usuário, como níveis de aplicação de diacríticos.
  - **Estratégias**:
    - Criar endpoints para que os usuários possam salvar e gerenciar suas configurações personalizadas.
    - Desenvolver um sistema de autenticação e autorização para garantir a segurança e privacidade das configurações do usuário.
    - Permitir que as configurações do usuário sejam aplicadas nas solicitações de conversão de texto.

### 1.2. Avaliação dos Requisitos Não Funcionais (RNFs)

#### 1.2.1. Desempenho e Escalabilidade

- **RNF1-API**: A exigência de um tempo de resposta abaixo de 5 segundos para textos de tamanho moderado demanda um foco na eficiência do algoritmo e otimização do código. A utilização de técnicas de programação eficientes, como algoritmos rápidos de processamento de texto e estruturas de dados otimizadas, é crucial. Além disso, pode-se considerar o uso de cache para resultados frequentemente solicitados.
- **RNF2-API**: Para garantir a alta disponibilidade e escalabilidade, é importante adotar uma arquitetura que suporte o aumento de carga, como microserviços ou arquiteturas baseadas em contêineres. Utilizar serviços de nuvem que ofereçam escalabilidade automática pode ser uma opção viável.

#### 1.2.2. Segurança e Privacidade

- **RNF3-API**: A implementação de autenticação e autorização robustas pode ser alcançada com o uso de padrões de mercado, como OAuth 2.0 para gerenciamento de acesso. Isso garante que apenas usuários autorizados possam acessar a API.

- **RNF4-API**: Para a criptografia de dados em trânsito e em repouso, o uso de TLS (Transport Layer Security) para comunicações seguras e algoritmos de criptografia fortes para o armazenamento de dados é essencial.

#### 1.2.3. Usabilidade e Acessibilidade

- **RNF5-API**: A documentação deve ser elaborada com clareza, abrangendo todos os aspectos da API, incluindo exemplos práticos de uso. Ferramentas como Swagger ou Redoc podem ser utilizadas para criar documentações interativas e fáceis de entender.

- **RNF6-API**: Um ambiente de testes (sandbox) facilita o desenvolvimento e teste de integrações por parte dos usuários da API. Isso pode incluir a disponibilização de uma versão da API com limitações controladas para desenvolvimento e teste.

#### 1.2.4. Compatibilidade e Internacionalização

- **RNF7-API**: Para assegurar a compatibilidade, é importante projetar a API com padrões abertos e considerar a utilização de formatos de dados amplamente suportados, como JSON ou XML.

- **RNF8-API**: O suporte a configurações regionais pode envolver a internacionalização e localização da API, permitindo a adaptação a diferentes idiomas e formatos regionais (como datas e números).

## 2. Projeto

### 2.1. Estruturação da API

#### 2.1.1. Arquitetura da API

- **Microserviços vs Monolítico**:

Discussão:

    Considerando a necessidade de escalabilidade e manutenção, a arquitetura de microserviços pode ser mais apropriada. Ela permite a distribuição de diferentes funcionalidades da API em serviços independentes, facilitando a escalabilidade e atualizações. No entanto, se o escopo do projeto for menor ou os recursos limitados, uma arquitetura monolítica pode ser mais prática inicialmente.

Decisão:

    A arquitetura de microserviços, apesar de suas vantagens em escalabilidade e flexibilidade, pode ser complexa e exigir mais recursos para gerenciamento e orquestração. Considerando suas limitações de recursos, uma abordagem monolítica pode ser mais adequada. Ela é mais simples de desenvolver e manter, especialmente para uma equipe pequena ou um único desenvolvedor.

- **Containers e Orquestração**:

Discussão:

    Utilizar containers, como Docker, pode simplificar o desenvolvimento, testes e implantação. Ferramentas de orquestração, como Kubernetes, podem ajudar na gestão dos microserviços, especialmente em ambientes de nuvem.

Decisão:

    Embora Docker e Kubernetes sejam poderosos para gerenciamento de microserviços, eles podem ser excessivos para um projeto monolítico e um único desenvolvedor. Você pode optar por usar apenas Docker para simplificar a implantação e o ambiente de teste, sem a necessidade imediata de Kubernetes.

#### 2.1.2. Escolha de Tecnologias

- **Linguagem de Programação e Frameworks**:

Discussão:

    A escolha da linguagem de programação deve ser baseada em critérios como desempenho, suporte da comunidade, e facilidade de integração com outras tecnologias. Linguagens como Python, Java, ou Go podem ser consideradas devido ao seu forte suporte para desenvolvimento web e APIs.

    Frameworks como Spring (Java), Django ou Flask (Python), ou Express (Node.js) podem ser utilizados para agilizar o desenvolvimento da API. A escolha depende da linguagem de programação e das necessidades específicas do projeto.

Decisão:

    Python e Flask são escolhas adequadas devido à sua simplicidade, flexibilidade e vasta comunidade. Eles são ideais para um desenvolvedor único e ajudam na rápida prototipagem e desenvolvimento.

- **Banco de Dados**:

Discussão:

    Escolher um banco de dados adequado é crucial. Dependendo dos requisitos, pode-se optar por um banco de dados relacional (como PostgreSQL ou MySQL) ou um não relacional (como MongoDB).

Decisão:

    PostgreSQL é robusto, mas pode ser mais do que necessário para um projeto inicial. Você poderia considerar SQLite para começar, que é mais leve e não requer um servidor de banco de dados separado.

#### 2.1.3. Estratégias de Desenvolvimento e Implantação

- **Desenvolvimento Baseado em Testes (TDD)**:

Discussão:

    Adotar uma abordagem de TDD poderia para garantir que a API funcione conforme esperado e facilitar a manutenção.

Decisão:

    Optar por TDD é uma boa prática, principalmente para manter a qualidade e reduzir bugs a longo prazo.

- **Integração e Entrega Contínua (CI/CD)**:

Discussão:

    Implementar pipelines de CI/CD para automatizar o teste e a implantação da API poderia melhorar a eficiência do processo de desenvolvimento.

Decisão:

    Configurar pipelines de CI/CD é benéfico, mas considere ferramentas mais simples e diretas que não exijam configuração complexa, como GitHub Actions.

- **Monitoramento e Logging**:

Discussão:

    Deve-se estabelecer um sistema robusto de monitoramento e logging para acompanhar o desempenho da API e identificar rapidamente quaisquer problemas.

Decisão:

    Embora ferramentas como Prometheus e ELK sejam abrangentes, elas podem ser substituídas por soluções mais simples como o Grafana ou mesmo logs internos do Flask, para começar.

- **Documentação e Versão da API**:

Discussão:

    Utilizar ferramentas como Swagger para documentação e garantir que a API seja versionada poderia facilitar futuras atualizações e manutenção.

Decisão:

    Usar Swagger para documentação é uma escolha sólida, pois ajuda a manter a clareza e facilita a futura expansão ou colaboração.

#### 2.1.4. Segurança

- **Autenticação e Autorização**:

Discussão:

    Implementar sistemas robustos de autenticação (como OAuth 2.0) e autorização para controlar o acesso à API.

- **Criptografia e Segurança dos Dados**:

Discussão:

    Garantir a segurança dos dados em trânsito e em repouso, utilizando protocolos como TLS e algoritmos de criptografia fortes.

- **Decisão**:

  Implementar OAuth 2.0 e TLS continua sendo importante para a segurança, mas pode ser simplificado para se adequar à escala do projeto.

#### Próximos Passos

Após a conclusão da etapa 2.1, a próxima fase será o design da interface da API, abordado na etapa 2.2. Aqui, a atenção será voltada para a criação de endpoints claros, definindo métodos de requisição e resposta, e elaborando uma documentação detalhada e acessível.

#### 2.2. Design de Interface

Criação de endpoints claros e documentação detalhada.

#### 2.2.1. Criação de Endpoints Claros

**Discussão:**

A definição clara dos endpoints é crucial para a eficácia e usabilidade da API. Deve-se considerar a criação de endpoints intuitivos e autoexplicativos, que reflitam diretamente as funcionalidades oferecidas pela API, como conversão de texto, consulta de regras e configurações de usuário. Além disso, é importante que os endpoints permitam a expansão e modificação futura sem interromper os serviços existentes.

**Decisão:**

Implementar endpoints com nomes descritivos, como `/convertText`, `/getRules`, e `/userSettings`. Cada endpoint deve aceitar e retornar dados em um formato padronizado (como JSON), e ser documentado com exemplos de requisições e respostas. Isso facilitará a compreensão e a integração por parte dos usuários da API.

#### 2.2.2. Documentação Detalhada

**Discussão:**

Uma documentação completa e acessível é fundamental para que os desenvolvedores possam integrar e utilizar a API eficientemente. A documentação deve incluir detalhes sobre os endpoints, parâmetros, formatos de dados, exemplos de código e informações sobre tratamento de erros. Ferramentas como Swagger podem ser usadas para criar uma documentação interativa e fácil de navegar.

**Decisão:**

Utilizar Swagger para criar uma documentação interativa e abrangente. A documentação deve ser atualizada constantemente para refletir mudanças na API e incluir exemplos de uso reais para auxiliar os desenvolvedores na integração.

#### 2.2.3. Métodos de Requisição e Resposta

**Discussão:**

Os métodos de requisição e resposta devem ser cuidadosamente escolhidos para cada endpoint. Por exemplo, o uso de GET para recuperação de informações e POST para ações que alteram o estado do servidor. Também é importante considerar a eficiência na transferência de dados e a segurança das informações transmitidas.

**Decisão:**

Adotar métodos de requisição HTTP padrão, como GET para consultas e POST para envio de dados para conversão. As respostas devem incluir códigos de status HTTP apropriados para indicar sucesso, erro ou outros estados relevantes. Os dados sensíveis devem ser protegidos usando protocolos de segurança, como HTTPS.

#### Próximos Passos

Após a conclusão do design da interface da API, a próxima fase envolverá a implementação dos componentes da API, conforme delineado na etapa 3. Isso incluirá o desenvolvimento dos algoritmos de conversão de texto, mecanismos de customização, e a implementação dos endpoints definidos.

### 3. Implementação

#### 3.1. Codificação

Desenvolvimento dos componentes da API, incluindo algoritmos de conversão de texto e mecanismos de customização.

Questionamento: Como e por que parte devemos começar o desenvolvimento?

**Discussão:**

1. **Priorização Baseada nos Requisitos Funcionais (RFs)**: Uma abordagem lógica é começar pelo desenvolvimento das funcionalidades mais críticas e centrais da API. Neste caso, o RF1-API e o RF2-API, que tratam do processamento de texto para conversão e suporte a diferentes formatos de entrada, são essenciais. Eles formam a base sobre a qual as outras funcionalidades serão construídas.

2. **Desenvolvimento Incremental e Modular**: Ao começar pelas funcionalidades centrais, é possível adotar um modelo de desenvolvimento incremental. Isso permite que a equipe concentre-se em pequenas partes do sistema de cada vez, facilitando o teste e a integração desses módulos antes de prosseguir para as próximas funcionalidades.

3. **Testes desde o Início**: Iniciar o desenvolvimento pelas funcionalidades principais permite que a equipe estabeleça uma estrutura de testes sólida desde o início. Isso é crucial para garantir a qualidade e a estabilidade da API.

4. **Resposta aos Desafios Técnicos**: Começar pelo processamento de texto e suporte a diferentes formatos de entrada permitirá enfrentar os desafios técnicos mais complexos no início do projeto. Isso pode incluir a criação de algoritmos de análise de texto e a implementação de parsers flexíveis.

**Decisão:**

- **Iniciar pelo Desenvolvimento do RF1-API e RF2-API**: Começar com o desenvolvimento do endpoint de conversão de texto, incluindo a implementação do algoritmo que aplica as regras da ODPI para adicionar acentos diacríticos. Isso será seguido pelo desenvolvimento de parsers para suportar diferentes formatos de entrada.

- **Adoção de TDD (Test-Driven Development)**: Utilizar TDD desde o início do desenvolvimento para garantir que cada componente funcione conforme esperado e para facilitar a manutenção.

- **Feedbacks e Iterações Rápidas**: Implementar um ciclo de feedback rápido com partes interessadas e usuários potenciais para iterar e melhorar os componentes desenvolvidos.

- **Documentação Simultânea**: Paralelamente ao desenvolvimento, iniciar a documentação das funcionalidades e exemplos de uso para facilitar a adoção da API por desenvolvedores.

- **Revisão Contínua e Ajustes**: Estar aberto para revisar e ajustar o plano de desenvolvimento com base no progresso e nos desafios encontrados.

---

#### 3.2. Integração

Conexão dos módulos desenvolvidos para formar uma API coesa.

#### 4.3. Testes

- **Testes Unitários e de Integração**: Verificação da funcionalidade de cada componente e do sistema como um todo.
- **Testes de Carga e Desempenho**: Avaliação do comportamento da API sob diferentes volumes de requisições.

#### 4.4. Segurança

- **Autenticação e Autorização**: Implementação de medidas de segurança para controlar o acesso à API.
- **Criptografia**: Garantia da segurança dos dados em trânsito e em repouso.

#### 4.5. Documentação e Suporte

- **Documentação da API**: Elaboração de materiais detalhados sobre o uso da API, incluindo guias e exemplos.
- **Ambiente de Sandbox**: Disponibilização de um ambiente de testes para desenvolvedores.

### 5. Implantação e Manutenção

#### 5.1. Implantação

- **Lançamento**: Disponibilização da API em um ambiente de produção.
- **Monitoramento**: Observação contínua do desempenho e segurança da API.

#### 5.2. Manutenção e Atualizações

- **Atualizações Regulares**: Incorporação de melhorias e novas funcionalidades.
- **Suporte Técnico**: Assistência contínua para desenvolvedores e usuários da API.

---

Complete com a discussão e decisão da etapa 3.1. Para cada tópico levantado, escreva sua respectiva decisão.

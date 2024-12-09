# Grupo:
Guilherme Teles da Costa Moura,
José Santarem Gomes,
Letícia Souza de Araújo,
Sarah Paulina Cruz de Arruda,
Victor da Silva Dantas,
Vinícius Santana Gato.

---

# Projeto de Sistema de Doação e Script Python

Este repositório contém três arquivos principais: um programa escrito em **Prolog** para gerenciar doações, um script **Python** para processamento de dados e o pdf contendo as respostas das demais questões da lista. Abaixo, você encontrará instruções claras e detalhadas para executar os sistemas em sua máquina.

---

## 📂 Estrutura do Repositório

- **sistema_doacao.pl**: Sistema de gerenciamento de doações escrito em SWI-Prolog.
- **questao_7.py**: Script Python para manipulação de dados.

---

## 🛠️ Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas antes de começar:

### Para o sistema Prolog:
- **[SWI-Prolog](https://www.swi-prolog.org/)**

### Para o script Python:
- **[Python 3.8+](https://www.python.org/)**
- Bibliotecas necessárias:
  - `pandas`
  - `numpy`

Você pode instalar as bibliotecas Python executando:

```bash
pip install pandas numpy
```

---

## 🚀 Como Executar o Sistema de Doação (Prolog)

1. Instale o SWI-Prolog.
2. Abra o terminal e navegue até o diretório onde o arquivo `sistema_doacao.pl` está localizado.
3. Inicie o interpretador SWI-Prolog:

   ```bash
   swipl
   ```

4. Carregue o arquivo Prolog:

   ```prolog
   [sistema_doacao].
   ```

5. Utilize as consultas disponíveis para gerenciar o sistema de doação. Exemplos:

   ```prolog
   % Para listar doações:
   listar_doacoes.

   % Para adicionar uma nova doação:
   adicionar_doacao('Nome do Doador', 'Item Doado').

   % Para remover uma doação específica:
   remover_doacao('Nome do Doador', 'Item Doado').
   ```

---

## 🐍 Como Executar o Script Python

1. Certifique-se de ter o Python instalado.
2. Navegue até o diretório onde o arquivo `questao_7.py` está localizado.
3. Execute o script:

   ```bash
   python questao_7.py
   ```

4. O script processará os dados e exibirá os resultados na saída padrão ou salvará os dados processados, dependendo da lógica do código.

---

## 🧐 Problemas Comuns e Soluções

### 1. **Erro ao carregar o arquivo Prolog**
   - Certifique-se de que está no diretório correto.
   - Verifique se o SWI-Prolog está instalado corretamente.

### 2. **Erro de módulo ausente no Python**
   - Execute `pip install pandas numpy` para instalar as dependências necessárias.

---

## 💡 Dicas Adicionais

- **Customizações:** Ambos os scripts são modulares, permitindo fácil personalização para atender às suas necessidades.
- **Aprendizado:** Consulte a [documentação oficial do Prolog](https://www.swi-prolog.org/) e a [documentação do Python](https://docs.python.org/3/) para expandir suas habilidades.


**Desenvolvido com 💻 e ❤️ pela equipe!**

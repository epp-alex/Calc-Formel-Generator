# Assistente de Fórmulas LibreOffice Calc

Uma ferramenta Python para criar, testar e gerenciar fórmulas do LibreOffice Calc rapidamente – com sistema de favoritos, sincronização em equipe, suporte a múltiplos idiomas e gerenciador de plugins.

## 🚀 Funcionalidades

- 📑 4 abas com mais de 60 funções

- 🌐 38 idiomas (incluindo Hindi com instalação automática de fonte)

- ⭐ Sistema de favoritos (local & sincronização em equipe via unidade de rede)

- 🛠 Painel de administrador para favoritos da equipe (protegido por senha)

- 📋 Fórmulas copiáveis diretamente com realce de sintaxe

- ✏️ Campo de saída editável com Desfazer/Refazer

- 📖 Ajuda integrada & referência de funções (por idioma)

- 💾 Salvamento automático (JSON, escrita atômica)

- 🌙 Modo escuro

- 🔌 Gerenciador de Plugins para criar seus próprios plugins de fórmulas

- 🔤 Suporte RTL (da direita para a esquerda) – detecção automática da direção de escrita

- 🗄️ Backup e restauração – salve todas as configurações e favoritos com nome e senha

- ⌨️ Atalho global `Ctrl+F12` para minimizar/restaurar
- 🔍 Validador JSON – verificação e correção automática de `languages.json` e `formula_explanations.json`

## 🖥️ Como Usar

**1. Preencha os campos**

- Intervalo de células (ex.: `A1:A10`)

- Célula 1 / Célula 2 (ex.: `A1`, `B1`)

- Parâmetro opcional (ex.: texto ou índice)

- Modo de referência absoluta selecionável: `A1`, `$A1`, `A$1`, `$A$1`

**2. Selecione uma função** Escolha uma aba e clique em uma função – a fórmula é gerada instantaneamente.

**3. Personalize a fórmula** A fórmula gerada pode ser editada diretamente no campo de saída.

**4. Copie** Com um clique para a área de transferência (incluindo cores de sintaxe).

**5. Use os favoritos**

- ⭐ Salvar → guardar a fórmula atual (Ctrl+S)

- 📂 Carregar → reutilizar uma fórmula

- ❌ Excluir → tecla Del ou botão

- 🕐 Histórico → fórmulas usadas recentemente

## 📊 Visão Geral das Abas

**Aba 1 – Funções Básicas** `+` `-` `\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Aba 2 – Funções Avançadas** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Aba 3 – Data & Texto** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Aba 4 – Pesquisa & Arredondamento** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Explicações de fórmulas da documentação do LibreOffice

O arquivo `formula_explanations.json` é preenchido diretamente a partir da **documentação oficial do LibreOffice Calc** (https://help.libreoffice.org).

### Fonte de dados e atualização

- Descrições, informações de sintaxe e exemplos são obtidos do site oficial de ajuda do LibreOffice
- Os idiomas suportados dependem das traduções disponíveis no site
- O arquivo contém para cada função: nome, sintaxe, descrição, exemplo e categoria
- Adições ou correções podem ser feitas manualmente (consulte Validador JSON)

### Estrutura de `formula_explanations.json`

```json
{
  "SUM": {
    "pt": {
      "syntax": "SUM(Número1; Número2; ...)",
      "description": "Soma todos os números em um intervalo de células.",
      "example": "=SUM(A1:A10)"
    },
    "en": {
      "syntax": "SUM(Number1; Number2; ...)",
      "description": "Adds all numbers in a cell range.",
      "example": "=SUM(A1:A10)"
    }
  }
}
```

| Campo | Obrigatório | Descrição |
|-------|------------|-----------|
| `syntax` | ✅ | Sintaxe da fórmula com parâmetros |
| `description` | ✅ | Descrição breve da função |
| `example` | ✅ | Exemplo de uso como fórmula pronta |
| `note` | ❌ | Nota opcional |

> 💡 **Nota:** Se não houver entrada para um idioma, o aplicativo retorna automaticamente à versão em inglês.

---

## 🔍 Validador JSON para arquivos de idioma

O **Validador JSON** integrado verifica e corrige `languages.json` e `formula_explanations.json` para consistência, completude e nomes de países corretos. Acessível em **Configurações → 🔍 Validador JSON**.

### O que é verificado?

#### `languages.json`

- ✅ Todos os 38 idiomas presentes (por código ISO 639-1)
- ✅ **Nomes de país e idioma corretos** (ex.: `"pt"` → `"Português"`)
- ✅ Sem códigos de idioma duplicados
- ✅ Campos obrigatórios presentes: `name`, `native_name`, `flag`, `rtl`
- ✅ Flag RTL configurado corretamente (Árabe, Hebraico, Persa, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Todas as funções das 4 abas registradas
- ✅ Campos obrigatórios presentes: `syntax`, `description`, `example`
- ✅ Sem campos vazios (`""` ou `null`)
- ✅ Códigos de idioma correspondem a `languages.json`

### Funções de correção

| Tipo de erro | Correção automática |
|-------------|---------------------|
| Nome de país errado | Substituído pelo nome correto conforme ISO |
| Entrada de idioma ausente | Preenchido com versão de reserva em inglês |
| Campo obrigatório vazio | Marcado como `"[MISSING]"` para revisão manual |
| Entrada duplicada | Duplicatas removidas, entrada mais completa mantida |
| Flag RTL incorreto | Corrigido automaticamente com base em códigos RTL conhecidos |

### Como usar

1. Abra **Configurações → 🔍 Validador JSON**
2. Selecione o arquivo: `languages.json` ou `formula_explanations.json` (ou ambos)
3. **🔎 Verificar** – mostra todos os problemas encontrados
4. **🛠 Corrigir automaticamente** – resolve todos os erros corrigíveis automaticamente
5. **💾 Salvar** – grava o arquivo corrigido atomicamente
6. **📋 Exportar relatório** (opcional) – salva um arquivo de texto com todos os resultados

> ⚠️ **Nota:** Antes de cada correção automática é criada uma cópia de segurança do arquivo original (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Sistema de Favoritos

- Salve e reutilize suas próprias fórmulas

- Separação entre favoritos pessoais e da equipe

- Favoritos da equipe são somente leitura (apenas o administrador pode editar)

- Entradas duplicadas são impedidas

- Ordenação livre dos favoritos pessoais

- Sincronização via unidade de rede (configurável opcionalmente)

### Sincronização em Equipe

Em **Configurações → 🌐 Caminho de Rede** é possível informar uma unidade de rede (ex.: `\\\\\\\\Servidor\\\\Compartilhado\\\\formulas`).

- Na inicialização: os favoritos da rede são salvos localmente (fallback offline)

- Ao salvar: as fórmulas pessoais são gravadas na rede, os favoritos da equipe permanecem intocados

## 🛠 Painel de Administrador

Acessível pelo botão 🛠. No primeiro clique, uma senha é definida (PBKDF2-SHA256, apenas o hash é armazenado).

- Adicionar, editar e excluir fórmulas da equipe

- Alterar senha

- Gravar alterações diretamente na unidade de rede

## 🔌 Gerenciador de Plugins

O Gerenciador de Plugins (`plugin\_manager.py`) é uma ferramenta independente para criar e gerenciar seus próprios plugins de fórmulas para o Calc2. Ele fica na mesma pasta que `Calc2.py` e é iniciado pelo botão 🔌 dentro do Calc2.py.

### Funções

- **Criar novo plugin** – Assistente passo a passo (nome, fórmulas, traduções, resumo)

- **Adicionar fórmulas** – Adicionar fórmulas a um plugin existente

- **Editar traduções** – Traduzir nomes de fórmulas para os 38 idiomas

- **Abrir pasta do plugin** – Diretamente no Explorador de Arquivos

- **Excluir plugin** – Com confirmação de segurança

### Estrutura do Plugin

Cada plugin fica como uma subpasta em `plugins/` e consiste em dois arquivos:

```
`plugins/`

`  meu\_plugin/`

`    plugin.json      ← Metadados (nome, versão, autor, descrição)`

`    formulas.json    ← Fórmulas com traduções`
```

**Exemplo `plugin.json`:**

```
`\{`

`  "id": "meu\_plugin",`

`  "enabled": true,`

`  "version": "1.0",`

`  "author": "Seu Nome",`

`  "icon": "💰",`

`  "name": \{ "en": "Finance Formulas", "pt": "Fórmulas Financeiras" \},`

`  "description": \{ "en": "Useful formulas for financial calculations." \}`

`\}`
```

**Exemplo `formulas.json`:**

```
`\[`

`  \{`

`    "formula": "=SUM(A1:A10)",`

`    "name": \{ "en": "Sum of range", "pt": "Soma do intervalo" \},`

`    "description": \{ "en": "Adds all values in A1:A10." \},`

`    "category": \{ "en": "Basic", "pt": "Básico" \}`

`  \}`

`\]`
```

### Aviso Importante (⚠️ Important Notice)

No Gerenciador de Plugins há o botão **⚠️ Important Notice**. Ao clicar, abre-se uma janela com todas as regras para a criação correta de plugins em inglês. As mesmas informações também estão em `IMPORTANT\_NOTICE.md`.

## 🌐 Suporte a Múltiplos Idiomas

38 idiomas disponíveis, alteráveis diretamente no aplicativo.  
Novos idiomas podem ser adicionados pelo botão 🌍 com o Assistente de Idiomas.

**Nota Hindi (हिंदी):** Na primeira troca para o Hindi, a fonte *Noto Sans Devanagari* é instalada uma vez em todo o sistema. O Windows pode solicitar permissões de administrador para isso.

## 🔤 Suporte RTL (da direita para a esquerda)

Idiomas com escrita da direita para a esquerda são detectados automaticamente e toda a interface é espelhada:

- **Árabe (عربي)** – detecção RTL automática
- **Hebraico (עברית)** – detecção RTL automática
- **Persa / Farsi (فارسی)** – detecção RTL automática
- **Urdu (اردو)** – detecção RTL automática

**O que muda no modo RTL:** Todo o layout da interface é espelhado, os campos de entrada usam alinhamento RTL, a fonte muda automaticamente para uma compatível com RTL (ex.: *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Nota:** As fórmulas LibreOffice geradas permanecem sempre em sintaxe LTR – apenas a interface muda de direção.


## 🗄️ Backup e restauração

### Criar backup

Em **Configurações → 🗄️ Criar backup**:

1. **Nome** – rótulo livre (ex.: `Backup_Maio_2025`)
2. **Senha** – o backup é criptografado com AES; sem ela, a restauração é impossível
3. **Local de salvamento** – local ou em uma unidade de rede
4. Clique em **💾 Criar backup** – é criado um arquivo `.calc2backup`

**Conteúdo:** Todos os favoritos, configurações, favoritos da equipe (opcional), plugins instalados.

### Restaurar backup

Em **Configurações → 📂 Restaurar backup**:

1. Selecione o arquivo (`.calc2backup`)
2. Digite a senha
3. Escolha o escopo: apenas favoritos / apenas configurações / tudo
4. Clique em **🔄 Restaurar**

> ⚠️ Os dados existentes são sobrescritos durante a restauração. Um backup automático dos dados atuais é oferecido antes da restauração.


## 💡 Dicas

- `$A$1` → referência absoluta (menu suspenso ao lado dos campos de célula)

- **Ctrl+S** → salvar fórmula nos favoritos

- **Ctrl+C** → copiar fórmula (fora dos campos de entrada)

- **Ctrl+Z / Ctrl+Y** → Desfazer / Refazer

- **Ctrl+F12** → minimizar / restaurar janela (funciona mesmo quando o Calc2 está minimizado)

- **Tecla Del** na lista de favoritos → excluir entrada

- As fórmulas podem ser ajustadas diretamente no campo de saída após a geração

## 📁 Estrutura do Projeto

```
`Calc2.py                        ← Programa principal`

`plugin\_manager.py               ← Gerenciador de Plugins`

`IMPORTANT\_NOTICE.md             ← Notas sobre criação de plugins`

`data/`

`  README\_pt.md / README\_en.md / ...      ← Ajuda por idioma`

`  REFERENZ\_pt.md / REFERENZ\_en.md / ...  ← Referência de funções por idioma`

`language/`

`  languages.json                ← Traduções da interface (38 idiomas)`

`  formula\_explanations.json`

`services/`

`  language\_tool.py              ← Assistente: adicionar novo idioma`

`  settings\_service.py`

`  auth\_service.py`

`  favorites\_service.py`

`  network\_sync.py`

`  install\_service.py`

`  json_validator.py             ← verificação e correção de languages.json / formula_explanations.json`

`plugins/                        ← Pasta de plugins (criada automaticamente)`

`  meu\_plugin/`

`    plugin.json`

`    formulas.json`

`fonts/`

`  NotoSansDevanagari-Regular.ttf  ← Fonte para Hindi
  NotoSansArabic-Regular.ttf      ← Fonte árabe (RTL)
  NotoSansHebrew-Regular.ttf      ← Fonte hebraica (RTL)`

`python/                         ← Python embutido`

`  python.exe`

`  ...`

`settings.json                   ← criado automaticamente`

`favoriten.json                  ← favoritos locais (criado automaticamente)`
```

## 🧠 Destaques Técnicos

- **Escrita Atômica de Arquivos** → evita arquivos corrompidos ao salvar

- **Arquitetura de Serviços** → lógica e interface estritamente separadas

- **Migração Automática** → formatos antigos de favoritos são reconhecidos e convertidos

- **Tratamento Robusto de Erros** → arquivos com falha não causam travamentos

- **Realce de Sintaxe** → fórmulas são exibidas em cores

- **Modo Escuro** → totalmente suportado

- **Sistema de Plugins** → o Calc2 é extensível com plugins de fórmulas próprios

- **Motor RTL** → detecção automática de idiomas RTL, espelhamento completo da interface com fontes adequadas

- **Backup e restauração** → backups criptografados AES com nome e senha, restauração seletiva

- **Validador JSON** → verificação e correção automática de `languages.json` e `formula_explanations.json` incl. nomes de países e campos obrigatórios

- **Fonte LibreOffice** → `formula_explanations.json` é preenchido a partir da documentação oficial do LibreOffice Calc (https://help.libreoffice.org)

- **Atalho Global** → `Ctrl+F12` funciona em todo o sistema via biblioteca `keyboard` (thread em segundo plano)

## Licença

Uso livre para fins pessoais e comerciais.


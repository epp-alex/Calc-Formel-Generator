# LibreOffice Calc Assistente de Fórmulas

Uma ferramenta Python para criar, testar e gerir rapidamente fórmulas do LibreOffice Calc – com sistema de favoritos, sincronização de equipa, suporte multilingue e gestor de plugins.

## 🚀 Funcionalidades

- 📑 4 separadores com mais de 60 funções

- 🌐 38 idiomas (incluindo hindi com instalação automática de fonte)

- ⭐ Sistema de favoritos (local e sincronização de equipa via unidade de rede)

- 🛠 Painel de administração para favoritos de equipa (protegido por palavra-passe)

- 📋 Fórmulas prontas a copiar com realce de sintaxe

- ✏️ Campo de saída editável com desfazer/refazer

- 📖 Ajuda integrada e referência de funções (por idioma)

- 💾 Gravação automática (JSON, escrita atómica)

- 🌙 Modo escuro

- 🔌 Gestor de plugins para criar plugins de fórmulas personalizados

- 🔤 Suporte RTL (da direita para a esquerda) – deteção automática da direção de escrita

- 🗄️ Cópia de segurança e restauro – guarde todas as definições e favoritos com nome e palavra-passe

- ⌨️ Atalho global `Ctrl+F12` para minimizar/restaurar a janela
- 🔍 Validador JSON – verificação e correção automática de `languages.json` e `formula_explanations.json`

## 🖥️ Utilização

**1. Introduzir dados**

- Intervalo de células (ex.: `A1:A10`)

- Célula 1 / Célula 2 (ex.: `A1`, `B1`)

- Parâmetro opcional (ex.: texto ou índice)

- Modo de referência absoluta selecionável: `A1`, `$A1`, `A$1`, `$A$1`

**2. Selecionar uma função** Escolha um separador e clique numa função – a fórmula é gerada imediatamente.

**3. Personalizar a fórmula** A fórmula gerada pode ser editada diretamente no campo de saída.

**4. Copiar** Transferir para a área de transferência com um clique (incluindo cores de sintaxe).

**5. Usar favoritos**

- ⭐ Guardar → guardar a fórmula atual (Ctrl+S)

- 📂 Carregar → reutilizar fórmula

- ❌ Eliminar → tecla Delete ou botão

- 🕐 Histórico → fórmulas usadas recentemente

## 📊 Visão geral dos separadores

**Separador 1 – Funções básicas** `+` `-` `\*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**Separador 2 – Funções avançadas** IF, AND, OR, NOT SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**Separador 3 – Data e texto** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**Separador 4 – Pesquisa e arredondamento** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 Explicações de fórmulas da documentação do LibreOffice

O ficheiro `formula_explanations.json` é preenchido diretamente a partir da **documentação oficial do LibreOffice Calc** (https://help.libreoffice.org).

### Fonte de dados e atualização

- Descrições, informações de sintaxe e exemplos são obtidos do sítio de ajuda oficial do LibreOffice
- Os idiomas suportados dependem das traduções disponíveis no sítio
- O ficheiro contém para cada função: nome, sintaxe, descrição, exemplo e categoria
- Adições ou correções podem ser feitas manualmente (consulte Validador JSON)

### Estrutura de `formula_explanations.json`

```json
{
  "SUM": {
    "pt": {
      "syntax": "SUM(Número1; Número2; ...)",
      "description": "Soma todos os números num intervalo de células.",
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
| `example` | ✅ | Exemplo de utilização como fórmula pronta |
| `note` | ❌ | Nota opcional |

> 💡 **Nota:** Se não existir entrada para um idioma, a aplicação regressa automaticamente à versão em inglês.

---

## 🔍 Validador JSON para ficheiros de idioma

O **Validador JSON** integrado verifica e corrige `languages.json` e `formula_explanations.json` para consistência, completude e nomes de países corretos. Acessível em **Definições → 🔍 Validador JSON**.

### O que é verificado?

#### `languages.json`

- ✅ Todos os 38 idiomas presentes (por código ISO 639-1)
- ✅ **Nomes de país e idioma corretos** (ex.: `"pt"` → `"Português"`)
- ✅ Sem códigos de idioma duplicados
- ✅ Campos obrigatórios presentes: `name`, `native_name`, `flag`, `rtl`
- ✅ Flag RTL configurado corretamente (Árabe, Hebraico, Persa, Urdu → `"rtl": true`)

#### `formula_explanations.json`

- ✅ Todas as funções dos 4 separadores registadas
- ✅ Campos obrigatórios presentes: `syntax`, `description`, `example`
- ✅ Sem campos vazios (`""` ou `null`)
- ✅ Códigos de idioma correspondem a `languages.json`

### Funções de correção

| Tipo de erro | Correção automática |
|-------------|---------------------|
| Nome de país errado | Substituído pelo nome correto conforme ISO |
| Entrada de idioma em falta | Preenchido com versão de reserva em inglês |
| Campo obrigatório vazio | Marcado como `"[MISSING]"` para revisão manual |
| Entrada duplicada | Duplicados removidos, entrada mais completa mantida |
| Flag RTL incorreto | Corrigido automaticamente com base em códigos RTL conhecidos |

### Como utilizar

1. Abra **Definições → 🔍 Validador JSON**
2. Selecione o ficheiro: `languages.json` ou `formula_explanations.json` (ou ambos)
3. **🔎 Verificar** – mostra todos os problemas encontrados
4. **🛠 Corrigir automaticamente** – resolve todos os erros corrigíveis automaticamente
5. **💾 Guardar** – grava o ficheiro corrigido atomicamente
6. **📋 Exportar relatório** (opcional) – guarda um ficheiro de texto com todos os resultados

> ⚠️ **Nota:** Antes de cada correção automática é criada uma cópia de segurança do ficheiro original (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ Sistema de favoritos

- Guardar e reutilizar fórmulas personalizadas

- Separação entre favoritos pessoais e de equipa

- Os favoritos de equipa são só de leitura (apenas o administrador pode editar)

- Entradas duplicadas são impedidas

- Ordenação livre dos favoritos pessoais

- Sincronização via unidade de rede (configurável opcionalmente)

### Sincronização de equipa

Em **Definições → 🌐 Caminho de rede** é possível indicar uma unidade de rede (ex.: `\\\\\\\\Servidor\\\\Partilha\\\\formulas`).

- No arranque: os favoritos de rede são guardados localmente (cópia de segurança offline)

- Ao guardar: as fórmulas pessoais são escritas na rede, as fórmulas de equipa ficam inalteradas

## 🛠 Painel de administração

Acessível pelo botão 🛠. No primeiro clique é definida uma palavra-passe (PBKDF2-SHA256, apenas o hash é guardado).

- Adicionar, editar e eliminar fórmulas de equipa

- Alterar palavra-passe

- Escrever alterações diretamente na unidade de rede

## 🔌 Gestor de plugins

O gestor de plugins (`plugin\_manager.py`) é uma ferramenta autónoma para criar e gerir plugins de fórmulas personalizados para o Calc2. Encontra-se na mesma pasta que `Calc2.py` e é iniciado pelo botão 🔌 no Calc2.py:

### Funções

- **Criar novo plugin** – assistente passo a passo (nome, fórmulas, traduções, resumo)

- **Adicionar fórmulas** – adicionar fórmulas a um plugin existente

- **Editar traduções** – traduzir nomes de fórmulas para todos os 38 idiomas

- **Abrir pasta de plugins** – diretamente no explorador de ficheiros

- **Eliminar plugin** – com confirmação de segurança

### Estrutura do plugin

Cada plugin encontra-se como subpasta em `plugins/` e é composto por dois ficheiros:

```
plugins/  
  meu\_plugin/  
    plugin.json      ← metadados (nome, versão, autor, descrição)  
    formulas.json    ← fórmulas com traduções
```

**Exemplo de `plugin.json`:**

```
\{  
  "id": "meu\_plugin",  
  "enabled": true,  
  "version": "1.0",  
  "author": "O seu nome",  
  "icon": "💰",  
  "name": \{ "en": "Finance Formulas", "pt": "Fórmulas Financeiras" \},  
  "description": \{ "en": "Useful formulas for financial calculations." \}  
\}
```

**Exemplo de `formulas.json`:**

```
\[  
  \{  
    "formula": "=SUM(A1:A10)",  
    "name": \{ "en": "Sum of range", "pt": "Soma do intervalo" \},  
    "description": \{ "en": "Adds all values in A1:A10." \},  
    "category": \{ "en": "Basic", "pt": "Básico" \}  
  \}  
\]
```

### Aviso importante (⚠️ Important Notice)

No gestor de plugins existe o botão **⚠️ Important Notice**. Um clique abre uma janela com todas as regras para a criação correta de plugins em inglês. As mesmas informações estão também disponíveis em `IMPORTANT\_NOTICE.md`.

## 🌐 Suporte multilingue

38 idiomas disponíveis, alteráveis diretamente na aplicação.  
Novos idiomas podem ser adicionados pelo botão 🌍 com o Assistente de Idiomas.

**Nota sobre hindi (हिंदी):** Na primeira mudança para hindi, a fonte *Noto Sans Devanagari* é instalada uma única vez a nível do sistema. O Windows solicitará permissões de administrador nesse momento.

## 🔤 Suporte RTL (da direita para a esquerda)

Os idiomas com escrita da direita para a esquerda são detetados automaticamente e toda a interface é espelhada:

- **Árabe (عربي)** – deteção RTL automática
- **Hebraico (עברית)** – deteção RTL automática
- **Persa / Farsi (فارسی)** – deteção RTL automática
- **Urdu (اردو)** – deteção RTL automática

**O que muda no modo RTL:** Todo o esquema da interface é espelhado, os campos de entrada utilizam alinhamento RTL, o tipo de letra muda automaticamente para um compatível com RTL (ex.: *Noto Sans Arabic*, *Noto Sans Hebrew*).

> 💡 **Nota:** As fórmulas LibreOffice geradas permanecem sempre em sintaxe LTR – apenas a interface muda de direção.


## 🗄️ Cópia de segurança e restauro

### Criar cópia de segurança

Em **Definições → 🗄️ Criar cópia de segurança**:

1. **Nome** – etiqueta livre (ex.: `Copia_Maio_2025`)
2. **Palavra-passe** – a cópia é cifrada com AES; sem ela, o restauro é impossível
3. **Local de gravação** – local ou numa unidade de rede
4. Clique em **💾 Criar cópia de segurança** – é criado um ficheiro `.calc2backup`

**Conteúdo:** Todos os favoritos, definições, favoritos de equipa (opcional), plugins instalados.

### Restaurar cópia de segurança

Em **Definições → 📂 Restaurar cópia de segurança**:

1. Selecione o ficheiro (`.calc2backup`)
2. Introduza a palavra-passe
3. Escolha o âmbito: apenas favoritos / apenas definições / tudo
4. Clique em **🔄 Restaurar**

> ⚠️ Os dados existentes são substituídos durante o restauro. É oferecida uma cópia automática dos dados atuais antes do restauro.


## 💡 Dicas

- `$A$1` → referência absoluta (lista suspensa junto aos campos de célula)

- **Ctrl+S** → guardar fórmula nos favoritos

- **Ctrl+C** → copiar fórmula (fora dos campos de entrada)

- **Ctrl+Z / Ctrl+Y** → desfazer / refazer

- **Ctrl+F12** → minimizar / restaurar a janela (funciona mesmo quando o Calc2 está minimizado)

- **Tecla Delete** na lista de favoritos → eliminar entrada

- As fórmulas podem ser ajustadas diretamente no campo de saída após a geração

## 📁 Estrutura do projeto

```
Calc2.py                        ← programa principal  
plugin\_manager.py               ← gestor de plugins  
IMPORTANT\_NOTICE.md             ← notas sobre a criação de plugins  
data/  
  README\_de.md / README\_en.md / ...      ← ajuda por idioma  
  REFERENZ\_de.md / REFERENZ\_en.md / ...  ← referência de funções por idioma  
language/  
  languages.json                ← traduções da interface (38 idiomas)  
  formula\_explanations.json  
services/  
  language\_tool.py              ← assistente: adicionar novo idioma  
  settings\_service.py  
  auth\_service.py  
  favorites\_service.py  
  network\_sync.py  
  install\_service.py  
  json\_validator.py             ← verificação e correção de languages.json / formula_explanations.json
  json\_validator.py             ← verificação e correção de languages.json / formula_explanations.json
plugins/                        ← pasta de plugins (criada automaticamente)  
  meu\_plugin/  
    plugin.json  
    formulas.json  
fonts/  
  NotoSansDevanagari-Regular.ttf  ← fonte hindi
  NotoSansArabic-Regular.ttf      ← fonte árabe (RTL)
  NotoSansHebrew-Regular.ttf      ← fonte hebraica (RTL)  
python/                         ← Python incorporado  
  python.exe  
  ...  
settings.json                   ← criado automaticamente  
favoritos.json                  ← favoritos locais (criado automaticamente)
```

## 🧠 Destaques técnicos

- **Escrita atómica de ficheiros** → evita ficheiros corrompidos durante a gravação

- **Arquitetura de serviços** → lógica e interface separadas de forma rigorosa

- **Migração automática** → formatos antigos de favoritos são detetados e convertidos

- **Tratamento robusto de erros** → ficheiros corrompidos não causam falhas

- **Realce de sintaxe** → as fórmulas são apresentadas a cores

- **Modo escuro** → totalmente suportado

- **Sistema de plugins** → o Calc2 pode ser expandido com plugins de fórmulas personalizados

- **Motor RTL** → deteção automática de idiomas RTL, espelhamento completo da interface com fontes adequadas

- **Cópia de segurança e restauro** → cópias AES cifradas com nome e palavra-passe, restauro seletivo

- **Validador JSON** → verificação e correção automática de `languages.json` e `formula_explanations.json` incl. nomes de países e campos obrigatórios

- **Fonte LibreOffice** → `formula_explanations.json` é preenchido a partir da documentação oficial do LibreOffice Calc (https://help.libreoffice.org)

- **Validador JSON** → verificação e correção automática de `languages.json` e `formula_explanations.json` incl. nomes de países e campos obrigatórios

- **Fonte LibreOffice** → `formula_explanations.json` é preenchido a partir da documentação oficial do LibreOffice Calc (https://help.libreoffice.org)

- **Atalho global** → `Ctrl+F12` funciona a nível do sistema através da biblioteca `keyboard` (fio de execução em segundo plano)

## Licença

Livre para uso pessoal e comercial.


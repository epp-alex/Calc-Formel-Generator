# LibreOffice Calc 公式助手

一款用于快速创建、测试和管理 LibreOffice Calc 公式的 Python 工具——具备收藏夹系统、团队同步、多语言支持和插件管理器。

## 🚀 功能特性

- 📑 4 个选项卡，涵盖 60 余种函数

- 🌐 38 种语言（含印地语，支持自动安装字体）

- ⭐ 收藏夹系统（本地存储及通过网络驱动器进行团队同步）

- 🛠 团队收藏夹管理员面板（密码保护）

- 📋 可直接复制的公式，带语法高亮显示

- ✏️ 可编辑的输出区域，支持撤销/重做

- 📖 内置帮助文档及函数参考（按语言分类）

- 💾 自动保存（JSON 格式，原子写入）

- 🌙 深色模式

- 🔌 插件管理器，可创建自定义公式插件

- 🔤 RTL 支持（从右到左）– 自动检测书写方向

- 🗄️ 备份与恢复 – 使用名称和密码保存所有设置和收藏夹

- ⌨️ 全局快捷键 `Ctrl+F12`，用于最小化/还原窗口
- 🔍 JSON 验证器 – 自动检查并修正 `languages.json` 和 `formula_explanations.json`

## 🖥️ 使用方法

**1. 输入数据**

- 单元格范围（例如 `A1:A10`）

- 单元格 1 / 单元格 2（例如 `A1`、`B1`）

- 可选参数（例如文本或索引）

- 可选绝对引用模式：`A1`、`$A1`、`A$1`、`$A$1`

**2. 选择函数** 选择一个选项卡并点击某个函数——公式将立即生成。

**3. 调整公式** 生成的公式可直接在输出区域中编辑。

**4. 复制** 一键复制到剪贴板（包含语法颜色）。

**5. 使用收藏夹**

- ⭐ 保存 → 保存当前公式（Ctrl+S）

- 📂 加载 → 重新使用公式

- ❌ 删除 → Delete 键或按钮

- 🕐 历史记录 → 最近使用的公式

## 📊 选项卡概览

**选项卡 1 – 基础函数** `+` `-` `*` `/` `^` SUM、AVERAGE、MIN、MAX、MEDIAN、COUNT、COUNTA、SUMPRODUCT

**选项卡 2 – 高级函数** IF、AND、OR、NOT SUMIF、COUNTIF、AVERAGEIF、SUMIFS、STDEV、VAR、COUNTBLANK、LARGE

**选项卡 3 – 日期与文本** TODAY、NOW、YEAR、MONTH、DAY、DATE、DATEDIF、WEEKDAY CONCATENATE、LEN、LEFT、RIGHT、MID、UPPER、LOWER、TRIM

**选项卡 4 – 查找与舍入** VLOOKUP、HLOOKUP、INDEX、MATCH、INDEX+MATCH ROUND、ROUNDUP、ROUNDDOWN、INT、TRUNC、ABS、MOD、SQRT、RAND


## 📖 来自 LibreOffice 文档的公式说明

`formula_explanations.json` 文件直接从 **LibreOffice Calc 官方文档**（https://help.libreoffice.org）填充。

### 数据来源与更新

- 说明、语法信息和示例来自 LibreOffice 官方帮助网站
- 支持的语言取决于网站上可用的翻译
- 文件为每个函数包含：名称、语法、说明、示例和类别
- 可手动添加或修正条目（请参阅 JSON 验证器）

### `formula_explanations.json` 结构

```json
{
  "SUM": {
    "zh": {
      "syntax": "SUM(数字1; 数字2; ...)",
      "description": "对单元格范围内的所有数字求和。",
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

| 字段 | 必填 | 说明 |
|------|------|------|
| `syntax` | ✅ | 带参数的公式语法 |
| `description` | ✅ | 函数简短说明 |
| `example` | ✅ | 作为完整公式的使用示例 |
| `note` | ❌ | 可选备注 |

> 💡 **说明：** 如果某语言没有对应条目，应用将自动回退到英文版本。

---

## 🔍 语言文件 JSON 验证器

内置 **JSON 验证器**检查并修正 `languages.json` 和 `formula_explanations.json` 的一致性、完整性以及国家名称的正确性。可通过**设置 → 🔍 JSON 验证器**访问。

### 检查内容

#### `languages.json`

- ✅ 全部 38 种语言均存在（按 ISO 639-1 语言代码）
- ✅ 正确的**国家和语言名称**（例如 `"zh"` → `"中文"`）
- ✅ 无重复语言代码
- ✅ 必填字段存在：`name`、`native_name`、`flag`、`rtl`
- ✅ RTL 标志正确设置（阿拉伯语、希伯来语、波斯语、乌尔都语 → `"rtl": true`）

#### `formula_explanations.json`

- ✅ 4 个选项卡中的所有函数均已记录
- ✅ 必填字段存在：`syntax`、`description`、`example`
- ✅ 无空字段（`""` 或 `null`）
- ✅ 语言代码与 `languages.json` 一致

### 修正功能

| 错误类型 | 自动修正 |
|---------|---------|
| 错误的国家名称 | 按 ISO 标准替换为正确名称 |
| 缺失的语言条目 | 用英文备用版本填充 |
| 空的必填字段 | 标记为 `"[MISSING]"` 以供手动审查 |
| 重复条目 | 删除重复项，保留更完整的条目 |
| 错误的 RTL 标志 | 根据已知 RTL 代码自动修正 |

### 使用方法

1. 打开**设置 → 🔍 JSON 验证器**
2. 选择文件：`languages.json` 或 `formula_explanations.json`（或两者均选）
3. **🔎 检查** – 显示所有发现的问题
4. **🛠 自动修正** – 修正所有可自动修复的错误
5. **💾 保存** – 以原子方式写回修正后的文件
6. **📋 导出报告**（可选）– 保存包含所有结果的文本文件

> ⚠️ **说明：** 每次自动修正前，都会创建原始文件的备份副本（`languages.json.bak` / `formula_explanations.json.bak`）。

## ⭐ 收藏夹系统

- 保存并重复使用自定义公式

- 区分个人收藏夹与团队收藏夹

- 团队收藏夹为只读（仅管理员可编辑）

- 防止重复条目

- 个人收藏夹可自由排序

- 通过网络驱动器同步（可选配置）

### 团队同步

在 **设置 → 🌐 网络路径** 中可填写网络驱动器路径（例如 `\\\\服务器\\共享\\公式`）。

- 启动时：网络收藏夹保存至本地（离线备份）

- 保存时：个人公式写入网络，团队公式保持不变

## 🛠 管理员面板

通过 🛠 按钮访问。首次点击时设置密码（PBKDF2-SHA256，仅存储哈希值）。

- 添加、编辑和删除团队公式

- 修改密码

- 将更改直接写入网络驱动器

## 🔌 插件管理器

插件管理器（`plugin_manager.py`）是一个独立工具，用于为 Calc2 创建和管理自定义公式插件。它与 `Calc2.py` 位于同一文件夹，通过 Calc2.py 中的 🔌 按钮启动：

### 功能

- **新建插件** — 分步向导（名称、公式、翻译、摘要）

- **添加公式** — 向现有插件添加公式

- **编辑翻译** — 将公式名称翻译为全部 38 种语言

- **打开插件文件夹** — 直接在文件资源管理器中打开

- **删除插件** — 含安全确认提示

### 插件结构

每个插件作为子文件夹存放于 `plugins/` 目录下，由两个文件组成：

```
plugins/
  我的插件/
    plugin.json      ← 元数据（名称、版本、作者、描述）
    formulas.json    ← 含翻译的公式
```

**`plugin.json` 示例：**

```
{
  "id": "我的插件",
  "enabled": true,
  "version": "1.0",
  "author": "您的姓名",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "zh": "财务公式" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**`formulas.json` 示例：**

```
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "zh": "区域求和" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "zh": "基础" }
  }
]
```

### 重要提示（⚠️ Important Notice）

插件管理器中有一个 **⚠️ Important Notice** 按钮。点击后将打开一个窗口，以英文列出正确创建插件的所有规则。相同内容也可在 `IMPORTANT_NOTICE.md` 中找到。

## 🌐 多语言支持

提供 38 种语言，可直接在应用内切换。  
可通过 🌍 按钮使用语言向导添加新语言。

**关于印地语（हिंदी）的说明：** 首次切换到印地语时，系统将一次性安装 *Noto Sans Devanagari* 字体。Windows 届时会请求管理员权限。

## 🔤 RTL 支持（从右到左）

从右到左书写的语言会被自动检测，整个界面随之镜像显示：

- **阿拉伯语 (عربي)** – 自动 RTL 检测
- **希伯来语 (עברית)** – 自动 RTL 检测
- **波斯语 / 法尔西语 (فارسی)** – 自动 RTL 检测
- **乌尔都语 (اردو)** – 自动 RTL 检测

**RTL 模式下的变化：** 整个界面布局镜像翻转，输入框使用 RTL 对齐，字体自动切换为 RTL 兼容字体（如 *Noto Sans Arabic*、*Noto Sans Hebrew*）。

> 💡 **说明：** 生成的 LibreOffice 公式始终保持 LTR 语法——只有用户界面会改变方向。


## 🗄️ 备份与恢复

### 创建备份

通过 **设置 → 🗄️ 创建备份**：

1. **名称** – 自定义标签（例如 `备份_2025年5月`）
2. **密码** – 备份使用 AES 加密；没有密码则无法恢复
3. **保存位置** – 本地或网络驱动器
4. 点击 **💾 创建备份** – 生成 `.calc2backup` 文件

**内容：** 所有收藏夹、设置、团队收藏夹（可选）、已安装插件。

### 恢复备份

通过 **设置 → 📂 恢复备份**：

1. 选择备份文件（`.calc2backup`）
2. 输入密码
3. 选择恢复范围：仅收藏夹 / 仅设置 / 全部
4. 点击 **🔄 恢复**

> ⚠️ 恢复时现有数据将被覆盖。恢复前会提示自动备份当前数据。


## 💡 使用技巧

- `$A$1` → 绝对引用（单元格字段旁的下拉菜单）

- **Ctrl+S** → 将公式保存到收藏夹

- **Ctrl+C** → 复制公式（在输入字段外）

- **Ctrl+Z / Ctrl+Y** → 撤销 / 重做

- **Ctrl+F12** → 最小化 / 还原窗口（即使 Calc2 已最小化也有效）

- 收藏夹列表中的 **Delete 键** → 删除条目

- 生成公式后可直接在输出区域中进行调整

## 📁 项目结构

```
Calc2.py                        ← 主程序
plugin_manager.py               ← 插件管理器
IMPORTANT_NOTICE.md             ← 插件创建说明
data/
  README_de.md / README_en.md / ...      ← 各语言帮助文档
  REFERENZ_de.md / REFERENZ_en.md / ...  ← 各语言函数参考
language/
  languages.json                ← 界面翻译（38 种语言）
  formula_explanations.json
services/
  language_tool.py              ← 向导：添加新语言
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← 备份与恢复
  json_validator.py             ← languages.json / formula_explanations.json 检查与修正
plugins/                        ← 插件文件夹（自动创建）
  我的插件/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← 印地语字体
  NotoSansArabic-Regular.ttf      ← 阿拉伯语字体 (RTL)
  NotoSansHebrew-Regular.ttf      ← 希伯来语字体 (RTL)
python/                         ← 内嵌 Python
  python.exe
  ...
settings.json                   ← 自动创建
收藏夹.json                     ← 本地收藏夹（自动创建）
```

## 🧠 技术亮点

- **原子写入** → 保存时防止文件损坏

- **服务化架构** → 业务逻辑与用户界面严格分离

- **自动迁移** → 识别并转换旧版收藏夹格式

- **健壮的错误处理** → 损坏的文件不会导致程序崩溃

- **语法高亮** → 公式以彩色显示

- **深色模式** → 完整支持

- **插件系统** → Calc2 可通过自定义公式插件进行扩展

- **RTL 引擎** → 自动检测 RTL 语言，完整镜像界面并使用适配字体

- **备份与恢复** → 使用名称和密码的 AES 加密备份，选择性恢复

- **JSON 验证器** → 自动检查并修正 `languages.json` 和 `formula_explanations.json`，包括国家名称和必填字段

- **LibreOffice 来源** → `formula_explanations.json` 从 LibreOffice Calc 官方文档填充（https://help.libreoffice.org）

- **全局快捷键** → `Ctrl+F12` 通过 `keyboard` 库在系统级别生效（后台线程）

## 许可证

可免费用于个人及商业用途。

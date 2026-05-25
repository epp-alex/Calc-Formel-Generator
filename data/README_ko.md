# LibreOffice Calc 수식 도우미

Python으로 만든 LibreOffice Calc 수식 생성·테스트·관리 도구 – 즐겨찾기 시스템, 팀 동기화, 다국어 지원, 플러그인 매니저 포함.

## 🚀 주요 기능

- 📑 4개 탭, 60개 이상의 함수
- 🌐 38개 언어 지원 (힌디어 자동 폰트 설치 포함)
- ⭐ 즐겨찾기 시스템 (로컬 & 네트워크 드라이브를 통한 팀 동기화)
- 🛠 팀 즐겨찾기용 관리자 패널 (비밀번호 보호)
- 📋 구문 강조(Syntax Highlighting)와 함께 바로 복사 가능한 수식
- ✏️ 실행 취소/다시 실행 지원 편집 가능한 출력 필드
- 📖 통합 도움말 & 함수 참조 (언어별 제공)
- 💾 자동 저장 (JSON, 원자적 쓰기)
- 🌙 다크 모드
- 🔌 자체 수식 플러그인 제작용 플러그인 매니저
- 🔤 RTL 지원 (오른쪽에서 왼쪽) – 쓰기 방향 자동 감지
- 🗄️ 백업 & 복원 – 이름과 비밀번호로 모든 설정과 즐겨찾기 저장
- ⌨️ 최소화/복원을 위한 전역 단축키 `Ctrl+F12`
- 🔍 JSON 유효성 검사기 – `languages.json` 및 `formula_explanations.json` 자동 검사 및 수정

## 🖥️ 사용 방법

**1. 입력값 입력**
- 셀 범위 (예: `A1:A10`)
- 셀 1 / 셀 2 (예: `A1`, `B1`)
- 선택적 매개변수 (예: 텍스트 또는 인덱스)
- 절대 참조 모드 선택 가능: `A1`, `$A1`, `A$1`, `$A$1`

**2. 함수 선택** 탭을 선택하고 함수를 클릭하면 수식이 즉시 생성됩니다.

**3. 수식 수정** 생성된 수식은 출력 필드에서 직접 편집할 수 있습니다.

**4. 복사** 버튼 한 번으로 클립보드에 복사합니다 (구문 강조 포함).

**5. 즐겨찾기 활용**
- ⭐ 저장 → 현재 수식 저장 (Ctrl+S)
- 📂 불러오기 → 수식 재사용
- ❌ 삭제 → Delete 키 또는 버튼
- 🕐 기록 → 최근 사용한 수식

## 📊 탭 구성

**탭 1 – 기본 함수** `+` `-` `*` `/` `^` SUM, AVERAGE, MIN, MAX, MEDIAN, COUNT, COUNTA, SUMPRODUCT

**탭 2 – 고급 함수** IF, AND, OR, NOT, SUMIF, COUNTIF, AVERAGEIF, SUMIFS, STDEV, VAR, COUNTBLANK, LARGE

**탭 3 – 날짜 & 텍스트** TODAY, NOW, YEAR, MONTH, DAY, DATE, DATEDIF, WEEKDAY, CONCATENATE, LEN, LEFT, RIGHT, MID, UPPER, LOWER, TRIM

**탭 4 – 조회 & 반올림** VLOOKUP, HLOOKUP, INDEX, MATCH, INDEX+MATCH, ROUND, ROUNDUP, ROUNDDOWN, INT, TRUNC, ABS, MOD, SQRT, RAND


## 📖 LibreOffice 문서의 수식 설명

`formula_explanations.json` 파일은 **LibreOffice Calc 공식 문서**(https://help.libreoffice.org)에서 직접 가져옵니다.

### 데이터 소스 및 업데이트

- 설명, 구문 정보 및 예시는 LibreOffice 공식 도움말 사이트에서 가져옵니다
- 지원 언어는 사이트에서 사용 가능한 번역에 따라 다릅니다
- 파일에는 각 함수별로 이름, 구문, 설명, 예시, 카테고리가 포함됩니다
- 추가 또는 수정은 수동으로 가능합니다 (JSON 유효성 검사기 참조)

### `formula_explanations.json` 구조

```json
{
  "SUM": {
    "ko": {
      "syntax": "SUM(숫자1; 숫자2; ...)",
      "description": "셀 범위의 모든 숫자를 더합니다.",
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

| 필드 | 필수 | 설명 |
|------|------|------|
| `syntax` | ✅ | 매개변수가 포함된 수식 구문 |
| `description` | ✅ | 함수에 대한 간단한 설명 |
| `example` | ✅ | 완성된 수식으로서의 사용 예시 |
| `note` | ❌ | 선택적 메모 |

> 💡 **참고:** 언어 항목이 없으면 앱이 자동으로 영어 버전으로 대체됩니다.

---

## 🔍 언어 파일용 JSON 유효성 검사기

통합된 **JSON 유효성 검사기**는 `languages.json` 및 `formula_explanations.json`의 일관성, 완전성 및 올바른 국가명을 검사하고 수정합니다. **설정 → 🔍 JSON 유효성 검사기**에서 접근할 수 있습니다.

### 검사 항목

#### `languages.json`

- ✅ 38개 언어 모두 존재 (ISO 639-1 언어 코드 기준)
- ✅ **올바른 국가 및 언어 이름** (예: `"ko"` → `"한국어"`)
- ✅ 중복 언어 코드 없음
- ✅ 필수 필드 존재: `name`, `native_name`, `flag`, `rtl`
- ✅ RTL 플래그 올바르게 설정 (아랍어, 히브리어, 페르시아어, 우르두어 → `"rtl": true`)

#### `formula_explanations.json`

- ✅ 4개 탭의 모든 함수 등록됨
- ✅ 필수 필드 존재: `syntax`, `description`, `example`
- ✅ 빈 필드 없음 (`""` 또는 `null`)
- ✅ 언어 코드가 `languages.json`과 일치

### 수정 기능

| 오류 유형 | 자동 수정 |
|---------|---------|
| 잘못된 국가명 | ISO 표준에 따른 올바른 이름으로 교체 |
| 언어 항목 누락 | 영어 대체 항목으로 채움 |
| 빈 필수 필드 | 수동 검토를 위해 `"[MISSING]"`으로 표시 |
| 중복 항목 | 중복 제거, 더 완전한 항목 유지 |
| 잘못된 RTL 플래그 | 알려진 RTL 코드 기반으로 자동 수정 |

### 사용 방법

1. **설정 → 🔍 JSON 유효성 검사기** 열기
2. 파일 선택: `languages.json` 또는 `formula_explanations.json` (또는 둘 다)
3. **🔎 검사** – 발견된 모든 문제 표시
4. **🛠 자동 수정** – 자동으로 수정 가능한 모든 오류 수정
5. **💾 저장** – 수정된 파일을 원자적으로 저장
6. **📋 보고서 내보내기** (선택사항) – 모든 결과가 포함된 텍스트 파일 저장

> ⚠️ **참고:** 모든 자동 수정 전에 원본 파일의 백업 복사본이 생성됩니다 (`languages.json.bak` / `formula_explanations.json.bak`).

## ⭐ 즐겨찾기 시스템

- 자신만의 수식 저장 및 재사용
- 개인 즐겨찾기와 팀 즐겨찾기 분리
- 팀 즐겨찾기는 읽기 전용 (관리자만 편집 가능)
- 중복 항목 방지
- 개인 즐겨찾기 자유로운 순서 정렬
- 네트워크 드라이브를 통한 동기화 (선택적으로 설정 가능)

### 팀 동기화

**설정 → 🌐 네트워크 경로**에서 네트워크 드라이브를 입력할 수 있습니다 (예: `\\\\Server\\Share\\formeln`).

- 시작 시: 네트워크 즐겨찾기를 로컬에 저장 (오프라인 폴백)
- 저장 시: 개인 수식은 네트워크에 기록, 팀 수식은 그대로 유지

## 🛠 관리자 패널

🛠 버튼으로 접근. 처음 클릭 시 비밀번호를 설정합니다 (PBKDF2-SHA256, 해시만 저장).

- 팀 수식 추가, 편집, 삭제
- 비밀번호 변경
- 변경 사항을 네트워크 드라이브에 직접 저장

## 🔌 플러그인 매니저

플러그인 매니저(`plugin_manager.py`)는 Calc2용 자체 수식 플러그인을 만들고 관리하는 독립 도구입니다. `Calc2.py`와 같은 폴더에 위치하며 🔌 버튼으로 실행됩니다.

### 기능

- **새 플러그인 만들기** – 단계별 마법사 (이름, 수식, 번역, 요약)
- **수식 추가** – 기존 플러그인에 수식 추가
- **번역 편집** – 수식 이름을 38개 언어로 번역
- **플러그인 폴더 열기** – 파일 탐색기에서 직접 열기
- **플러그인 삭제** – 확인 메시지 포함

### 플러그인 구조

각 플러그인은 `plugins/` 하위 폴더로 존재하며 두 개의 파일로 구성됩니다:

```
plugins/
  my_plugin/
    plugin.json      ← 메타데이터 (이름, 버전, 작성자, 설명)
    formulas.json    ← 번역이 포함된 수식
```

**`plugin.json` 예시:**

```json
{
  "id": "my_plugin",
  "enabled": true,
  "version": "1.0",
  "author": "이름",
  "icon": "💰",
  "name": { "en": "Finance Formulas", "ko": "재무 수식" },
  "description": { "en": "Useful formulas for financial calculations." }
}
```

**`formulas.json` 예시:**

```json
[
  {
    "formula": "=SUM(A1:A10)",
    "name": { "en": "Sum of range", "ko": "범위 합계" },
    "description": { "en": "Adds all values in A1:A10." },
    "category": { "en": "Basic", "ko": "기본" }
  }
]
```

### 중요 안내 (⚠️ Important Notice)

플러그인 매니저에는 **⚠️ Important Notice** 버튼이 있습니다. 클릭하면 올바른 플러그인 제작 규칙이 영어로 표시됩니다. 동일한 내용이 `IMPORTANT_NOTICE.md`에도 있습니다.

## 🌐 다국어 지원

38개 언어를 앱 내에서 바로 전환할 수 있습니다.
🌍 버튼의 언어 마법사를 통해 새 언어를 추가할 수 있습니다.

**힌디어(हिंदी) 참고:** 처음 힌디어로 전환 시 *Noto Sans Devanagari* 폰트가 시스템 전체에 한 번 설치됩니다. Windows에서 관리자 권한을 요청합니다.

## 🔤 RTL 지원 (오른쪽에서 왼쪽)

오른쪽에서 왼쪽으로 쓰는 언어는 자동으로 감지되며 전체 인터페이스가 미러링됩니다:

- **아랍어 (عربي)** – 자동 RTL 감지
- **히브리어 (עברית)** – 자동 RTL 감지
- **페르시아어 / 파르시 (فارسی)** – 자동 RTL 감지
- **우르두어 (اردو)** – 자동 RTL 감지

**RTL 모드에서 변하는 것:** 전체 UI 레이아웃이 미러링되고, 입력 필드가 RTL 정렬을 사용하며, 폰트가 자동으로 RTL 호환 폰트(예: *Noto Sans Arabic*, *Noto Sans Hebrew*)로 전환됩니다.

> 💡 **참고:** 생성된 LibreOffice 수식은 항상 LTR 구문을 유지합니다 – 사용자 인터페이스만 방향이 바뀝니다.


## 🗄️ 백업 & 복원

### 백업 만들기

**설정 → 🗄️ 백업 만들기**를 통해:

1. **이름** – 자유로운 레이블 (예: `Backup_2025년5월`)
2. **비밀번호** – 백업은 AES로 암호화됩니다; 비밀번호 없이는 복원 불가
3. **저장 위치** – 로컬 또는 네트워크 드라이브
4. **💾 백업 만들기** 클릭 – `.calc2backup` 파일 생성

**내용:** 모든 즐겨찾기, 설정, 팀 즐겨찾기 (선택), 설치된 플러그인.

### 백업 복원

**설정 → 📂 백업 복원**을 통해:

1. 백업 파일 선택 (`.calc2backup`)
2. 비밀번호 입력
3. 복원 범위 선택: 즐겨찾기만 / 설정만 / 전부
4. **🔄 복원** 클릭

> ⚠️ 복원 시 기존 데이터가 덮어씌워집니다. 복원 전에 현재 데이터의 자동 백업이 제안됩니다.


## 💡 팁

- `$A$1` → 절대 참조 (셀 필드 옆 드롭다운)
- **Ctrl+S** → 수식을 즐겨찾기에 저장
- **Ctrl+C** → 수식 복사 (입력 필드 외부에서)
- **Ctrl+Z / Ctrl+Y** → 실행 취소 / 다시 실행
- **Ctrl+F12** → 창 최소화 / 복원 (Calc2가 최소화된 상태에서도 작동)
- 즐겨찾기 목록에서 **Delete 키** → 항목 삭제
- 생성 후 출력 필드에서 수식을 직접 수정 가능

## 📁 프로젝트 구조

```
Calc2.py                        ← 메인 프로그램
plugin_manager.py               ← 플러그인 매니저
IMPORTANT_NOTICE.md             ← 플러그인 제작 안내
data/
  README_de.md / README_en.md / ...      ← 언어별 도움말
  REFERENZ_de.md / REFERENZ_en.md / ...  ← 언어별 함수 참조
language/
  languages.json                ← UI 번역 (38개 언어)
  formula_explanations.json
services/
  language_tool.py              ← 마법사: 새 언어 추가
  settings_service.py
  auth_service.py
  favorites_service.py
  network_sync.py
  install_service.py
  backup_service.py             ← 백업 & 복원
  json_validator.py             ← languages.json / formula_explanations.json 검사 및 수정
plugins/                        ← 플러그인 폴더 (자동 생성)
  my_plugin/
    plugin.json
    formulas.json
fonts/
  NotoSansDevanagari-Regular.ttf  ← 힌디어 폰트
  NotoSansArabic-Regular.ttf      ← 아랍어 폰트 (RTL)
  NotoSansHebrew-Regular.ttf      ← 히브리어 폰트 (RTL)
python/                         ← 내장 Python
  python.exe
  ...
settings.json                   ← 자동 생성
favoriten.json                  ← 로컬 즐겨찾기 (자동 생성)
```

## 🧠 기술적 특징

- **원자적 파일 쓰기** → 저장 중 파일 손상 방지
- **서비스 아키텍처** → 로직과 UI 완전 분리
- **자동 마이그레이션** → 구버전 즐겨찾기 형식 자동 인식 및 변환
- **강력한 오류 처리** → 잘못된 파일이 있어도 프로그램 충돌 없음
- **구문 강조** → 수식을 색상으로 표시
- **다크 모드** → 완전 지원
- **플러그인 시스템** → 자체 수식 플러그인으로 Calc2 확장 가능
- **RTL 엔진** → RTL 언어 자동 감지, 적합한 폰트와 함께 완전한 UI 미러링
- **백업 & 복원** → 이름과 비밀번호가 있는 AES 암호화 백업, 선택적 복원
- **JSON 유효성 검사기** → `languages.json` 및 `formula_explanations.json` 자동 검사 및 수정 (국가명 및 필수 필드 포함)

- **LibreOffice 소스** → `formula_explanations.json`은 LibreOffice Calc 공식 문서에서 가져옴 (https://help.libreoffice.org)

- **전역 단축키** → `Ctrl+F12`는 `keyboard` 라이브러리(백그라운드 스레드)를 통해 시스템 전체에서 작동

## 라이선스

개인 및 상업적 목적으로 자유롭게 사용 가능합니다.

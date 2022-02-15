# 🦾 Automation HMS

🤖 長崎大学 健康管理システムの自動化


## 🏯 使い方 / Usage

1. GitHubでPrivate Repositoryを新しく作成
2. 下記のコードを`.github/workflows/automation-hms.yml`に記述
  - `ID:`の右に自分の学籍番号を記述
  - `PASSWORD`の右に自分のパスワードを記述
3. `.github/workflows/automation-hms.yml`を新しく作ったRepositoryにpush

```yaml:automation-hms.yml
name: 'Automation of NU Health Manage System'

on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 21 * * *'

jobs:
  ubuntu-test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - uses: k5-mot/auto-hms-action@main
        with:
          id:       'bb12345678'
          password: 'passwd'
```

## 🔖 References / 参考文献

- [長崎大学 健康管理システム](https://hms.hc.nagasaki-u.ac.jp/)


## 🍋 License / ライセンス

Copyright (c) 2021-2022 k5-mot All Rights Reserved.

"k5-mot/auto-hms" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).


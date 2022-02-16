# 🤖 Automation of NU Health Management System

[長崎大学 健康管理システム](https://hms.hc.nagasaki-u.ac.jp/)の自動化


## 🏯 Usage / 使い方

1. GitHub で本リポジトリを `Fork` する
1. `Fork` したリポジトリの `Settings` をクリック
1. `Secrets > Actions` をクリック
1. `SCHOOL_ID` と `SCHOOL_PASSWD` を設定する
    1. `New repository secret` をクリック
    1. `Name` に `SCHOOL_ID` を入力
    1. `Value` に自分の学籍番号(例: bb12345678) を入力
    1. `Add secret` をクリック
    1. 再度、 `New repository secret` をクリック
    1. `Name` に `SCHOOL_PASSWD` を入力
    1. `Value` に自分のパスワード を入力
    1. `Add secret` をクリック
1. 基本設定、終了
1. 下記は、Discord通知設定
1. `DISCORD_WEBHOOK` を設定する
    1. `New repository secret` をクリック
    1. `Name` に `DISCORD_WEBHOOK` を入力
    1. `Value` に Discord の Webhook URL を入力
    1. `Add secret` をクリック
1. Discord通知設定、終了

- 毎日0:00 UTC (9:00 JST) にシステムに自動入力するように設定していますが、 **GitHub Actions の負荷の影響により、指定時間から大きく遅延することがあります。**


## 🔖 References / 参考文献

- [長崎大学 健康管理システム](https://hms.hc.nagasaki-u.ac.jp/)


## 🖊️ Note / 備考

- 不具合報告は、[Issues](https://github.com/k5-mot/auto-hms-action/issues)にお願いします。


## 🍋 License / ライセンス

Copyright (c) 2021-2022 k5-mot All Rights Reserved.

"k5-mot/auto-hms-action" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).


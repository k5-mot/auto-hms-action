# ð¤ Automation of NU Health Management System

[é·å´å¤§å­¦ å¥åº·ç®¡çã·ã¹ãã ](https://hms.hc.nagasaki-u.ac.jp/)ã®èªåå

ä¸åº¦ã»ããã¢ããããããã°ãæ¯æ7:00~8:00ã«GitHub Actionãèªåå¥åãã­ã°ã©ã ãå®æå®è¡ãã¦ããã¾ãã
Discordã®Webhook URLãè¨­å®ããã°ãèªåå¥åå¾ãDiscordã«éç¥ããã¾ãã


## ð¯ Setup / ã»ããã¢ãã

1. GitHub ã§æ¬ãªãã¸ããªã `Fork` ãã
1. `Fork` ãããªãã¸ããªã® `Settings` ãã¯ãªãã¯
1. `Secrets > Actions` ãã¯ãªãã¯
1. `SCHOOL_ID` ã¨ `SCHOOL_PASSWD` ãè¨­å®ãã
    1. `New repository secret` ãã¯ãªãã¯
    1. `Name` ã« `SCHOOL_ID` ãå¥å
    1. `Value` ã«èªåã®å­¦ç±çªå·(ä¾: bb12345678) ãå¥å
    1. `Add secret` ãã¯ãªãã¯
    1. ååº¦ã `New repository secret` ãã¯ãªãã¯
    1. `Name` ã« `SCHOOL_PASSWD` ãå¥å
    1. `Value` ã«èªåã®ãã¹ã¯ã¼ã ãå¥å
    1. `Add secret` ãã¯ãªãã¯
1. åºæ¬è¨­å®ãçµäº
1. ä¸è¨ã¯ãDiscordéç¥è¨­å®
1. `DISCORD_WEBHOOK` ãè¨­å®ãã
    1. `New repository secret` ãã¯ãªãã¯
    1. `Name` ã« `DISCORD_WEBHOOK` ãå¥å
    1. `Value` ã« Discord ã® Webhook URL ãå¥å
    1. `Add secret` ãã¯ãªãã¯
1. Discordéç¥è¨­å®ãçµäº


## ð Test / ãã¹ã

1. `Actions` ãã¯ãªãã¯
1. `Automation of NU Health Management System` ãã¯ãªãã¯
1. `Run workflow` ãã¯ãªãã¯
1. èµ·åããworkflowã« âï¸ ãã¼ã¯ãä»ãããããã¹ã1ã¯æå
1. æå¾ã«ãå¥åº·ç®¡çã·ã¹ãã ã®ä¸è¦§ã«å¥åããã¦ããã°ããã¹ã2ã¯æå


## ðï¸ Note / åè

- æ¯æ¥22:00 UTC (7:00 JST) ã«ã·ã¹ãã ã«èªåå¥åããããã«è¨­å®ãã¦ãã¾ãã
- ãããã GitHub Actions ã®è² è·æ¬¡ç¬¬ã§ã **æå®æéããå¤§ããéå»¶ãããã¨ãããã¾ãã**
- ä¸å·åå ±åã¯ã[Issues](https://github.com/k5-mot/auto-hms-action/issues)ã«ãé¡ããã¾ãã


## ð References / åèæç®

- [é·å´å¤§å­¦ å¥åº·ç®¡çã·ã¹ãã ](https://hms.hc.nagasaki-u.ac.jp/)


## ð License / ã©ã¤ã»ã³ã¹

Copyright (c) 2021-2022 k5-mot All Rights Reserved.

"k5-mot/auto-hms-action" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).


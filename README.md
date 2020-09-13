# ansible-role-lsyncd [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-lsyncd.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-lsyncd)

CentOS 7 に lsyncd (rsync) を導入する ansible role です。

## 設定項目

以下の設定項目を設定して利用すること。

| 項目名                      | デフォルト値             | 説明                       |
| --------------------------- | ------------------------ | -------------------------- |
| lsyncd_master_hostname      | none                     | マスタとなるインベントリ名 |
| lsyncd_master_identity_file | /root/.ssh/id_rsa_lsyncd | ssh key ファイル           |
| lsyncd_slave_hosts          | []                       | スレーブホスト             |
| lsyncd_slave_username       | lsyncd                   | スレープホストのユーザ名   |
| lsyncd_local_sync_targets   | []                       | ローカルホストでの同期設定 |
| lsyncd_remote_sync_targets  | []                       | リモートホストとの同期設定 |

同期設定例

```
lsyncd_local_sync_targets:
  - source: /root/src/
    target: /root/dst/
```

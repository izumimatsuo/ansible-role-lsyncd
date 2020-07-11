# ansible-role-lsyncd [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-lsyncd.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-lsyncd)

CentOS 7 に lsyncd (rsync) を導入する ansible role です。

## 設定項目

以下の設定項目を設定して利用すること。

| 項目名             | デフォルト値| 説明               |
| ------------------ | ----------- | ------------------ |
| lsyncd_source_dir  | "/root/"    | 同期元ディレクトリ |
| lsyncd_target_dir  | "/root/"    | 同期先ディレクトリ |
| lsyncd_ssh_host    | "localhost" | 同期先sshホスト    |

# CeraDNS+

![CeraDNS](./Assets/CeraDNS.png)

为校园网提供优质的DNS解析服务，SNI列表转接及HTTP缓存的配置及工具分享

## 特性

### 基础（仅DNS）

智能查询：基于域名规则分流，分别查询境内外上游服务器，确保境外域名无污染

流量分流：将部分资源解析到教育网 CDN ，获取更快访问速度

去广告及隐私收集：订阅去广告及反隐私搜集规则，屏蔽相关域名解析

### 进阶（DNS+）

列表转接：使部分网站在无IPv6环境下获得访问权限(SNI)

HTTP缓存：对部分静态资源进行缓存，加快校园网内访问(HTTP Cache)

## 原理

**DNS**: AdGuardHome + Pcap_DNSProxy

**SNI**: [Gost](https://github.com/ginuerzh/gost) + 加密代理

**Cache**: Nginx +加密代理

## 如何使用

在每个文件夹中，都会有相应的README来详细解析

（努力编写中）

### 目录结构

- Conf:  相应功能的配置文件或配置示例
- Assets: 规则或列表等资源文件
- Tools: 一些有用的可用于生成配置的工具

## 公共DNS

以下公共DNS基于本项目搭建，无特别说明外服务仅限校内使用

欢迎提交PR或Issue来增添新的服务器

### 中山大学

#### 主要信息

| IP地址        | 位置             |
| ------------- | ---------------- |
| 172.16.84.110 | 中山大学珠海校区 |
| 172.16.84.111 | 中山大学珠海校区 |
| 172.16.84.112 | 中山大学珠海校区 |

#### 细节

DNS+服务器部署在N270 x86平台上，通过百兆以太网与校园网相连

目前已稳定运行超过60天，每24小时查询量在30万次

虽然部署在学生宿舍，但是我们会尽量确保 DNS 服务器的正常运行

## 许可

本仓库中配置文件(Conf)及元文件(Assets)内容适用[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)许可

程式源代码(Tools)适用[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)许可

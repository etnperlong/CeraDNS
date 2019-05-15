# CeraDNS+ Tools 实用脚本

## Gen_Pcap_Host.py

用于生成适用于Pcap_DNSProxy的解析规则

可参考本项目提供的 [SNI 加速域名列表](https://github.com/etnperlong/CeraDNS/blob/master/Assets/SNI_Accelerate_List.txt)

**usage: Gen_Pcap_Host.py [-h] [-s SNI] [-o OUTPUT] input**

| 参数        | 备注                         | 默认值             |
| ----------- | ---------------------------- | ------------------ |
| [-s SNI]    | SNI 加速服务器IP（可多个IP） | 0.0.0.0\|127.0.0.1 |
| [-o OUTPUT] | 输出文件                     | SNIHosts.txt       |
| input       | SNI 加速域名元列表           | **必须**           |

## Gen_SNIProxy_Table.py

*注：目前不使用SNI Proxy，因此此脚本已**废弃***

用于生成SNI Proxy转发规则

**usage: python3 Gen_SNIProxy_Table.py [-h] [-o OUTPUT] sni input**

| 参数        | 备注                              | 默认值       |
| ----------- | --------------------------------- | ------------ |
| [-o OUTPUT] | 输出文件                          | SNIHosts.txt |
| sni         | SNI Proxy 配置文件(sniproxy.conf) | **必须**     |
| input       | SNI 加速域名元列表                | **必须**     |

## ADHost_Merger.py

*注：目前使用ADGuard Home作为DNS请求前端，因此此脚本已**废弃***

用于抓取去广告Hosts项目，去重并合并

**usage: python3 ADHost_Merger.py [-h] [-i INPUT] [-o OUTPUT] [-r IP]**

| 参数        | 备注                          | 默认值                   |
| ----------- | ----------------------------- | ------------------------ |
| [-i INPUT]  | 去广告Hosts来源列表(JSON格式) | **内置Ad-War源**         |
| [-o OUTPUT] | 合并后输出的Hosts文件         | adblock_hosts_merged.txt |
| [-r IP]     | 重定向到的IP地址              | 127.0.0.1                |

## Update_Routing.sh

此脚本来源于Pcap_DNSProxy项目 | [来源](https://github.com/chengr28/Pcap_DNSProxy/blob/master/Source/Auxiliary/Scripts/Update_Routing.sh)

从APNIC更新并生成最新中国大陆境内路由表

**usage: bash Update_Routing.sh **

## Update_WhiteList.sh

此脚本来源于Pcap_DNSProxy项目 | [来源](https://github.com/chengr28/Pcap_DNSProxy/blob/master/Source/Auxiliary/Scripts/Update_WhiteList.sh)

从[dnsmasq-china-list](https://github.com/felixonmars/dnsmasq-china-list)项目更新并生成最新中国大陆域名白名单

**usage: bash Update_Routing.sh **
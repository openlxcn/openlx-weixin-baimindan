# OpenLX 微信公众号发布免登录白名单 Skill

> v0.1.1 · 测试版 · GitHub Pre-release

![OpenLX](assets/readme-hero.png)

## 换电脑、换网络，不再反复登录公众号后台修改 IP 白名单。

由公众号管理员完成首次扫码授权，把已经准备好的请求交给长期在线的 OpenLX 网关。技能只负责授权与发布交接，不写作、不排版、不生成素材，不连接客户的其他业务系统。

**[官网与安装](https://wx.openlx.cn/skills/openlx-weixin-baimindan) · [扫码授权](https://wx.openlx.cn/account?authorize=1) · [版本历史](https://wx.openlx.cn/skills/openlx-weixin-baimindan/update#version-history) · [English](README.en.md)**

## 能做什么

| 内容 | 当前能力 |
|---|---|
| 微信公众号图文 | 创建草稿、明确提交发布、结果查询 |
| 小绿书图片消息 | 有序图片与正文交接、草稿、明确提交发布 |
| 微信原文转载 | 按指定原文创建转载草稿或明确提交 |
| 已有草稿 | 明确提交发布并查询结果 |
| 视频、声音、播客音频 | 上传微信素材并返回素材 ID；当前不等同于公开发布 |

首次授权、公众号接口权限和微信规则仍然适用。播客使用用户已准备的音频或指定微信原文，不自动订阅、抓取或转播未指定内容。

## 复制给智能体安装

适用于 WorkBuddy、豆包办公、千问办公、百度搭子、ZCode、Trae Work、Qoder、Codex、Claude Code、Cursor。七个新增宿主由团队实测、Owner 确认；各宿主通过自己的技能导入方式读取同一份技能。

```text
请帮我安装「OpenLX 微信公众号发布免登录白名单 Skill」。
官网：https://wx.openlx.cn/skills/openlx-weixin-baimindan
GitHub：https://github.com/openlxcn/openlx-weixin-baimindan
请读取官网 Manifest（https://wx.openlx.cn/api/skills/openlx-weixin-baimindan/manifest），下载最新测试版并核验 SHA256。如果 GitHub 无法访问或要求登录，不必登录 GitHub，直接使用 Manifest 中的 official_mirror_url 从官网下载。按当前智能体支持的方式安装，已有版本先备份。安装后检查能否加载，并说明如何扫码授权公众号。本次只安装，不提交或发布内容。
```

[安装指南](skills/openlx-weixin-baimindan/references/INSTALL.md) · [更新与回退](skills/openlx-weixin-baimindan/references/UPDATE.md) · [兼容记录](compatibility-matrix.json)
首方命令宿主参数支持 codex、claude、cursor；其他宿主使用自身的技能导入方式。每7天首次使用时非阻断检查，确认后才更新，保护本地修改。

## 授权后使用

明确目标公众号 → 交接已准备内容或素材 → 获取真实结果。草稿创建后核对同一 media_id；公开提交后查询同一 publish_id。超时不盲重试。

[请求字段与操作](skills/openlx-weixin-baimindan/references/HANDOFF_CONTRACT.md) · [授权](skills/openlx-weixin-baimindan/references/AUTHORIZATION.md) · [数据边界](skills/openlx-weixin-baimindan/references/SECURITY_AND_PRIVACY.md) · [常见问题](skills/openlx-weixin-baimindan/references/FAQ.md)

[MIT License](LICENSE) · [Trademark](TRADEMARKS.md) · [Support](SUPPORT.md)

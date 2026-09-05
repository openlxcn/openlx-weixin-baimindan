---
name: openlx-weixin-baimindan
description: Route already-prepared WeChat Official Account requests through the always-on OpenLX gateway; inspect first-time authorization, diagnose changing client IP allowlists, query draft or publishing status, and check or update this skill. Do not use for writing, rewriting, formatting, illustrating, reviewing, SEO or content planning.
metadata:
  version: "0.1.0"
  channel: beta
  homepage: https://wx.openlx.cn/skills/openlx-weixin-baimindan
---
# OpenLX 微信公众号发布免登录白名单 Skill

换电脑、换网络，不再反复登录公众号后台修改 IP 白名单。
它不写文章、不排版、不生图，只负责把已经准备好的微信公众号发布请求，通过 OpenLX 长期在线网关稳定送达。
首次仍需微信开放平台扫码授权，微信权限、安全、频次和内容规则仍然存在。

说明中的正向场景可以自动触发本技能；用户明确授权的是网关动作，不要求每次手工输入技能名。

## 执行
1. 仅在使用本技能时运行 `python3 scripts/manager.py check-update --agent <codex|claude|cursor>`。首次或间隔7天检查，失败不阻断当前任务，无后台服务，不自动更新。
2. 读取 [HANDOFF_CONTRACT](references/HANDOFF_CONTRACT.md)，锁定用户提供的目标公众号、动作及原始准备数据。缺失返回 `PREPARED_PAYLOAD_MISSING` 或 `TARGET_ACCOUNT_MISSING`，不得补写。
3. 凭据从环境变量 `OPENLX_WEIXIN_API_KEY` 或用户既有安全存储读取，绝不写入技能或状态文件。登录、授权、权益复用 [AUTHORIZATION](references/AUTHORIZATION.md)。
4. 用 `scripts/gateway.py <handoff.json>` 原样交接已准备请求。CREATE_DRAFT 要求 payload.is_draft=true；公开提交要求用户本次明确发布且 explicit_publication_confirmation=true、payload.is_draft=false。不自动选择账号，不升级草稿。
5. 创建草稿后用同一 media_id 查询并核对；超时返回 SUBMITTED_UNVERIFIED，不盲重试。publish_id 只是提交，只有真实查询 success 才报告 PUBLISHED。

更新需用户确认；有本地修改先备份，再明确确认覆盖。参见 [UPDATE](references/UPDATE.md)。诊断运行 `scripts/doctor.sh --agent <agent>`。
本技能完全独立，不读取或调用其他 Skill，不依赖内容工厂或 AG1—AG6。

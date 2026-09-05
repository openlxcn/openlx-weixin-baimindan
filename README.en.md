# OpenLX WeChat Official Account IP Allowlist Skill

Public beta v0.1.0, GitHub Pre-release; not stable.

Changing computers or networks should not mean repeatedly signing into the WeChat account console to maintain the API IP allowlist. After the required first-time QR authorization, the always-on OpenLX gateway executes prepared requests.

This standalone skill does not write, rewrite, format or illustrate content, and has no other Skill dependency. It accepts an explicitly selected account and prepared payload, routes a draft or explicitly confirmed publishing request, and reports the real gateway result. WeChat permissions, security and content rules still apply.

[Install and product](https://wx.openlx.cn/skills/openlx-weixin-baimindan) · [Chinese guide](README.md) · [Compatibility](compatibility-matrix.json)

First-party Shell and PowerShell installers require Python 3.9+. Choose codex, claude or cursor explicitly. The default source is the official mirror; use --source github --version 0.1.0 for GitHub. Packages are checked against SHA256. Local changes are backed up and require a separate confirmation before replacement.

Version checks run on first use after seven days, never block the gateway task and never update automatically. Rollback restores the previous local backup. Personal OpenLX access credentials are kept outside the skill and update state; never supply a WeChat AppSecret.

See the Chinese reference set for the exact existing API fields and error codes. Only VERIFIED matrix rows mean real installation, loading, invocation and update have all passed. An accepted publishing job is not a published article; an uncertain request must not be blindly retried.

[License](LICENSE) · [Trademarks](TRADEMARKS.md) · [Security](SECURITY.md) · [Support](SUPPORT.md)

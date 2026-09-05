# OpenLX WeChat Official Account IP Allowlist Skill

v0.1.1 beta · GitHub Pre-release.

Changing computers or networks should not require repeatedly signing into the WeChat console to maintain the API IP allowlist. After first-time QR authorization, the always-on OpenLX gateway executes prepared requests for the specified account.

Supports article and image-post drafts, explicitly requested publication, authorized WeChat reprints, existing-draft submission, and video/audio material upload. Podcast audio uses the audio material path. Material upload is not public publication; no automatic podcast subscription or rebroadcast is performed.

The skill does not write, format or generate content, upload workspace history, or connect to the customer's other business systems. Only the required operation payload and credentials go to the gateway; the gateway returns the WeChat result. Platform permissions and rules still apply.

[Install](https://wx.openlx.cn/skills/openlx-weixin-baimindan#install) · [QR authorization](https://wx.openlx.cn/account?authorize=1) · [Chinese guide](README.md)

If GitHub is unavailable or asks for login, use the official Manifest's official_mirror_url and verify SHA256. No GitHub login is required. Native directory installers support Codex, Claude Code and Cursor; other hosts use their own skill import mechanism. Team-tested hosts also include WorkBuddy, Doubao Office, Qianwen Office, Baidu Dazi, ZCode, Trae Work and Qoder.

Nonblocking version checks occur on first use after seven days. Updates need confirmation and protect local edits. No background daemon or installation telemetry. Store personal access credentials outside the skill; never send WeChat AppSecret. Query the same draft or publishing ID, and never blindly retry an uncertain write.

[License](LICENSE) · [Data boundaries](skills/openlx-weixin-baimindan/references/SECURITY_AND_PRIVACY.md) · [Support](SUPPORT.md)

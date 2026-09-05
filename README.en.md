<p align="center"><a href="https://wx.openlx.cn/skills/openlx-weixin-baimindan"><img src="assets/product-hero-v2.png" alt="Switch computers and networks without repeatedly maintaining the WeChat IP allowlist. Initial QR authorization is required." width="100%"></a></p>

# OpenLX WeChat Official Account Publishing Skill

**Stop repeatedly signing in to maintain the calling-IP allowlist when your computer or network changes.**

`openlx-weixin-baimindan` connects your agent's prepared requests to the always-on OpenLX gateway. An account administrator authorizes the account first; the gateway handles subsequent WeChat API calls. Initial authorization, renewal, account permissions and WeChat rules still apply.

**v0.1.1 beta · GitHub Pre-release**

[Website](https://wx.openlx.cn/skills/openlx-weixin-baimindan) · [中文](README.md) · [Releases](https://github.com/openlxcn/openlx-weixin-baimindan/releases) · [Request contract](skills/openlx-weixin-baimindan/references/HANDOFF_CONTRACT.md)

## Why it exists

A prepared article should not stall because you switched Wi-Fi or moved to another computer. Direct calls from changing client networks can require repeated IP allowlist maintenance. OpenLX routes prepared operations through a long-running gateway, so changes to the client's network do not require corresponding account-backend allowlist edits.

The gateway stays online independently of your computer. Operations already accepted by the server can continue; unsent local tasks do not run automatically.

## Capabilities

| Prepared input | Current operation | Actual result |
|---|---|---|
| Articles and covers | Upload images, create drafts, explicitly submit publication | Draft `media_id`, submission `publish_id`, queried status |
| Image posts / newspic | Preserve image order and prepared text | Draft or publication task identifiers |
| Authorized WeChat reprints | Use the original article specified by the user | Corresponding draft or publication task |
| Existing drafts | Explicitly submit and query the same task | Publication task and status |
| Video, voice, podcast audio | Upload prepared WeChat materials | Material ID; **not public publication** |
| Authorization / status checks | Check access; read the original object | Actual permission or operation result |

Podcast input means prepared audio or a specified WeChat original. The skill does not subscribe to feeds, generate content or claim an upload is a published post.

## Ask your agent to install

Copy this into your existing agent:

```text
Install “OpenLX 微信公众号发布免登录白名单 Skill” (openlx-weixin-baimindan).
Website: https://wx.openlx.cn/skills/openlx-weixin-baimindan
Repository: https://github.com/openlxcn/openlx-weixin-baimindan
Read https://wx.openlx.cn/api/skills/openlx-weixin-baimindan/manifest and download the latest beta. Verify SHA256 before installation.
If GitHub is inaccessible or asks for sign-in, use the manifest's official_mirror_url instead; do not require GitHub login.
Use this agent's supported skill installation method. Detect and back up existing local changes without overwriting customizations. Verify the skill loads, then explain QR authorization. Install only; do not submit or publish content.
```

| Hosts | Installation | Evidence |
|---|---|---|
| Codex, Claude Code, Cursor | First-party installer: `codex`, `claude`, `cursor` | Actual install and load checks |
| WorkBuddy, Doubao Office (豆包办公), Qianwen Office (千问办公), Baidu Dazi (百度搭子), ZCode, Trae Work, Qoder | Host's native skill import | Team-tested and Owner-confirmed |
| Other hosts supporting `SKILL.md` | Import the skill folder | Not individually verified |

See the [compatibility record](compatibility-matrix.json). No invented installer flags are provided for unverified hosts.

## Install from the website

Requirements: Python 3.9+, plus curl on macOS/Linux or PowerShell on Windows. Replace `codex` with `claude` or `cursor` as needed.

macOS / Linux:

```sh
curl --proto '=https' --tlsv1.2 -fsSL https://wx.openlx.cn/downloads/openlx-weixin-baimindan/v0.1.1/install.sh -o /tmp/openlx-install.sh
sh /tmp/openlx-install.sh --agent codex --version 0.1.1
```

Windows PowerShell:

```powershell
$OpenLXInstaller = Join-Path $env:TEMP 'openlx-install.ps1'
Invoke-WebRequest 'https://wx.openlx.cn/downloads/openlx-weixin-baimindan/v0.1.1/install.ps1' -OutFile $OpenLXInstaller
& $OpenLXInstaller --agent codex --version 0.1.1
```

## Install from GitHub

```sh
git clone https://github.com/openlxcn/openlx-weixin-baimindan.git
cd openlx-weixin-baimindan
sh skills/openlx-weixin-baimindan/scripts/install.sh --agent codex --source github --version 0.1.1
```

On Windows, after cloning:

```powershell
& ./skills/openlx-weixin-baimindan/scripts/install.ps1 --agent codex --source github --version 0.1.1
```

The bootstrap retrieves and verifies a pinned manager from the official website; `--source github` downloads the skill archive from GitHub Releases. If GitHub is unavailable, use the website commands above.

Manual downloads: [GitHub ZIP](https://github.com/openlxcn/openlx-weixin-baimindan/releases/download/v0.1.1/openlx-weixin-baimindan-v0.1.1.zip) · [Official mirror](https://wx.openlx.cn/downloads/openlx-weixin-baimindan/v0.1.1/openlx-weixin-baimindan-v0.1.1.zip) · [SHA256SUMS](https://wx.openlx.cn/downloads/openlx-weixin-baimindan/v0.1.1/SHA256SUMS).

After verifying and extracting the archive, import `skills/openlx-weixin-baimindan` into your host. Restart the agent session and verify that it can load `SKILL.md`.

## First draft

1. Open [account authorization](https://wx.openlx.cn/account?authorize=1), sign in and have the account administrator scan the QR code.
2. Follow the [authorization guide](skills/openlx-weixin-baimindan/references/AUTHORIZATION.md). Keep the personal access credential in an environment variable or existing secure storage, never in an article or repository.
3. Give the agent the target account, prepared content and an explicit operation.

```text
Use OpenLX to create a draft for the AppID I specify, using my prepared HTML and cover.
Do not rewrite the content or publish it publicly. Return the media_id and read back that same draft for review.
```

For public submission, explicitly identify the account and draft and authorize that operation. Query the returned `publish_id`. Accepted submission is not confirmed publication. Preserve the original identifier if the result is uncertain; do not blindly retry writes.

Developers can run `python3 scripts/gateway.py handoff.json` inside the installed skill directory. See the [request contract](skills/openlx-weixin-baimindan/references/HANDOFF_CONTRACT.md).

## Independent by design

Your agent prepares content and chooses the target. The skill passes the requested operation to the gateway and reports the actual result. It does not write, format or generate content, upload your workspace or attach chat history. Account access is checked separately for each customer.

This public package contains no internal OpenLX workflow. Your own local extensions can remain separate and are not redistributed to other users. See [data boundaries](skills/openlx-weixin-baimindan/references/SECURITY_AND_PRIVACY.md).

## Updates and troubleshooting

The first use after seven days performs a nonblocking version check. An update requires user confirmation; local changes are detected and backed up before replacement. Installation or updates never authorize publication.

From the installed directory:

```sh
sh scripts/doctor.sh --agent codex
sh scripts/check-update.sh --agent codex
```

Windows has equivalent `.ps1` scripts. See [update / rollback](skills/openlx-weixin-baimindan/references/UPDATE.md) and [troubleshooting](skills/openlx-weixin-baimindan/references/TROUBLESHOOTING.md).

## History and support

- **v0.1.1 beta:** Focused account authorization and publishing handoff, with accurate material-versus-publication results.
- **v0.1.0 beta:** Initial installers, version checks, rollback, official mirror and compatibility baseline.

[Changelog](CHANGELOG.md) · [Version history](https://wx.openlx.cn/skills/openlx-weixin-baimindan/update#version-history) · [Issues](https://github.com/openlxcn/openlx-weixin-baimindan/issues)

If this saves you repeated allowlist maintenance, consider starring or sharing the repository. Report issues with the version, host, OS and redacted error; omit credentials and customer content.

[MIT License](LICENSE) · [Trademarks](TRADEMARKS.md) · [Support](SUPPORT.md) · [Security](SECURITY.md)

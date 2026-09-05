# OpenLX 微信公众号免白名单发布

本仓库包含 Claude Code / Cowork 和 Cursor 的插件描述文件。插件使用 `skills/openlx-weixin-baimindan`，技能正文与执行脚本均与 GitHub v0.1.1 一致。插件版本为 0.1.1 测试版；平台收录状态以各平台实际审核结果为准。

![OpenLX LOGO](assets/openlx-logo.png)

## Claude Code 本地验证

克隆本公开仓库后，在仓库根目录运行：

```sh
claude plugin validate .
claude --plugin-dir .
```

在新会话中调用 `/openlx-weixin-baimindan:openlx-weixin-baimindan`，或描述明确的公众号接口操作。官方目录审核通过后，也可在插件目录搜索 OpenLX 并安装。

## Cursor

插件由 `.cursor-plugin/plugin.json` 声明，自动发现 `skills/` 下的技能。官方 Marketplace 审核通过后，从市场安装；审核前可按 [README](README.md) 的首方安装器方式安装同版技能。

## 配置与使用

需要 Python 3.9+。先访问 [OpenLX 授权入口](https://wx.openlx.cn/account?authorize=1)，由目标公众号管理员完成首次扫码授权，再按 [授权说明](skills/openlx-weixin-baimindan/references/AUTHORIZATION.md) 设置 `OPENLX_WEIXIN_API_KEY`。插件不附带凭据。技能包采用 MIT 许可，OpenLX 名称与 LOGO 的使用边界见 [TRADEMARKS.md](TRADEMARKS.md)。网关服务的可用权限及费用以用户账户实际显示为准。

安装本身不会发布公众号内容。使用时提供目标公众号、准备好的内容和明确动作；创建草稿后读取同一对象，公开发布须另有本次明确授权。网络变化不再要求用户反复维护调用 IP 白名单，首次扫码授权、授权续期及微信账号权限仍然适用。

## 版本与分发

GitHub Release v0.1.1 的原 ZIP 与校验值保持有效；插件描述文件属于同版技能的分发适配。后续修改技能功能时，应先更新 GitHub 的版本与发布，再同步各平台。

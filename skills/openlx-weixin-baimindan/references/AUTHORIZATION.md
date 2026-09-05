# AUTHORIZATION

登录与凭据：https://wx.openlx.cn/account 。扫码授权：https://wx.openlx.cn/account?authorize=1 。免费体验与优惠券复用用户中心，购买复用现有支付页。
使用用户的个人访问 Key，HTTP 头 x-api-key。客户端不需要公众号 AppSecret。不要把凭据放入命令参数、技能目录、Git 或日志。
CHECK_AUTHORIZATION 调用现有 draft-count 进行只读鉴权/权益/草稿权限探测；它不是完整授权列表，也不能证明其他微信权限可用。首次扫码属于用户微信端交互，不能伪造完成。

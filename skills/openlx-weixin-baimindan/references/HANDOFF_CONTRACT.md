# HANDOFF_CONTRACT

schema: OPENLX_WEIXIN_BAIMINDAN_HANDOFF_V0_1
必需：target_account、requested_action、prepared_payload_or_reference（完整原始 JSON）、user_intent。
动作：CREATE_DRAFT、SUBMIT_EXPLICIT_PUBLISH、QUERY_STATUS、CHECK_AUTHORIZATION。公开提交还需 explicit_publication_confirmation=true。
payload.appid 必须等于 target_account，不自动补选。CREATE_DRAFT 的 payload.is_draft 必须为 true。
现有真实 API：POST /v2/proxy/publish、/v2/proxy/draft-get、/v2/proxy/publish-status、/v2/proxy/draft-count，均使用 x-api-key。
article 字段：appid、type=article、title、content（已准备 HTML）、cover_media_id、is_draft；可带 author、digest、content_source_url。
newspic 字段：appid、type=newspic、title、content、images（有序 media_id 对象）、is_draft。
查询草稿：appid + media_id；查询发布：appid + publish_id。原样返回网关响应。
可携带 idempotency_key、source_agent 作为上游记录，但现有网关没有被验证的去重保障。超时不盲重试。先查询并由用户处理不确定结果。
技能不上传未准备的素材，不转换 HTML，不替换图片。网关内部处理遵循现有 API 合同。

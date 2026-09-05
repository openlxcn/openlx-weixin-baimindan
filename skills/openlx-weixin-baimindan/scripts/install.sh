#!/bin/sh
set -eu
command -v python3 >/dev/null || { echo 'PYTHON_3_REQUIRED'; exit 1; }
TASK_TMP=$(mktemp -d)
trap 'rm -rf "$TASK_TMP"' EXIT HUP INT TERM
curl --proto '=https' --tlsv1.2 -fsSL 'https://wx.openlx.cn/downloads/openlx-weixin-baimindan/v0.1.0/manager.py' -o "$TASK_TMP/manager.py"
python3 -c 'import hashlib,sys; assert hashlib.sha256(open(sys.argv[1],"rb").read()).hexdigest()=="8e8fb38eee70e959ae0ed129411db5d06cb542b1080b64649c7d3f7a5ed38204", "BOOTSTRAP_HASH_MISMATCH"' "$TASK_TMP/manager.py"
python3 "$TASK_TMP/manager.py" install "$@"

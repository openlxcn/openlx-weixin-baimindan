#!/bin/sh
set -eu
command -v python3 >/dev/null || { echo 'PYTHON_3_REQUIRED'; exit 1; }
TASK_TMP=$(mktemp -d)
trap 'rm -rf "$TASK_TMP"' EXIT HUP INT TERM
curl --proto '=https' --tlsv1.2 -fsSL 'https://wx.openlx.cn/downloads/openlx-weixin-baimindan/v0.1.0/manager.py' -o "$TASK_TMP/manager.py"
python3 -c 'import hashlib,sys; assert hashlib.sha256(open(sys.argv[1],"rb").read()).hexdigest()=="f84fea3f199ef0ea5c391fed95271b494a440f8a311a22bd98fe7a45cedfc237", "BOOTSTRAP_HASH_MISMATCH"' "$TASK_TMP/manager.py"
python3 "$TASK_TMP/manager.py" install "$@"

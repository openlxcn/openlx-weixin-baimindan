import os,zipfile,hashlib,json,tempfile
from pathlib import Path
r=Path(__file__).resolve().parent.parent;out=Path(os.environ.get('RUNNER_TEMP',tempfile.gettempdir()))/'baimindan-installer-test';out.mkdir(exist_ok=True);z=out/'fixture.zip';sid='openlx-weixin-baimindan'
with zipfile.ZipFile(z,'w') as f:
 for p in (r/'skills'/sid).rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts:f.write(p,sid+'/'+p.relative_to(r).as_posix())
b=z.read_bytes();m=json.loads((r/'release-manifest.json').read_text(encoding='utf-8'));m['versions'][m['latest']['beta']]['files']=[{'size':len(b),'sha256':hashlib.sha256(b).hexdigest()}];(out/'manifest.json').write_text(json.dumps(m));print(out)

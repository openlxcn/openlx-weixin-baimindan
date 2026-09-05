#!/usr/bin/env python3
import hashlib,json,os,subprocess,sys,zipfile
from pathlib import Path
from datetime import datetime,timezone
R=Path(__file__).resolve().parent.parent
ID='openlx-weixin-baimindan'
def main():
 subprocess.run(['node','--test'],cwd=R,check=True)
 allow=json.loads((R/'public-package-allowlist.json').read_text())
 v=(R/'VERSION').read_text().strip()
 if v!='0.1.0': raise ValueError('First release limited to 0.1.0')
 commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip()
 epoch=int(subprocess.check_output(['git','show','-s','--format=%ct','HEAD'],cwd=R,text=True).strip())
 out=R/'dist'; out.mkdir(exist_ok=True)
 target=out/(ID+'-v'+v+'.zip')
 if target.exists(): raise ValueError('IMMUTABLE_RELEASE_ALREADY_BUILT')
 with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for name in sorted(allow):
   if name=='release-manifest.json': continue
   f=R/name
   if f.is_symlink() or not f.is_file(): raise ValueError('INVALID_ALLOWLIST_FILE')
   b=f.read_bytes()
   if f.suffix not in ('.png',): b=b.replace(b'\r\n',b'\n')
   info=zipfile.ZipInfo(ID+'/'+name,(2026,1,1,0,0,0)); info.create_system=3; info.external_attr=(0o100755 if f.suffix in ('.sh','.py') else 0o100644)<<16; info.compress_type=zipfile.ZIP_DEFLATED
   z.writestr(info,b)
 b=target.read_bytes(); sha=hashlib.sha256(b).hexdigest(); m=json.loads((R/'release-manifest.json').read_text()); e=m['versions'][v]; e.update(source_commit=commit,built_at=datetime.fromtimestamp(epoch,timezone.utc).isoformat(),released_at=datetime.fromtimestamp(epoch,timezone.utc).isoformat()); e['files']=[{'name':target.name,'sha256':sha,'size':len(b),'github_url':'https://github.com/openlxcn/'+ID+'/releases/download/v'+v+'/'+target.name,'official_mirror_url':'https://wx.openlx.cn/downloads/'+ID+'/v'+v+'/'+target.name}]
 (out/'release-manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n'); (out/'SHA256SUMS').write_text(sha+'  '+target.name+'\n'); (out/('CHANGELOG-v'+v+'.md')).write_bytes((R/'CHANGELOG.md').read_bytes()); print(json.dumps(e))
if __name__=='__main__': main()

import importlib.util,unittest,tempfile,zipfile,io,json,hashlib,argparse,contextlib
from pathlib import Path
from unittest.mock import patch
R=Path(__file__).resolve().parent.parent
spec=importlib.util.spec_from_file_location('manager',R/'skills/openlx-weixin-baimindan/scripts/manager.py'); m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Lifecycle(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.home=Path(self.tmp.name);self.p=patch.object(Path,'home',return_value=self.home);self.p.start();self.old=m.ROOT;m.ROOT=self.home/'state';self.a=argparse.Namespace(command='install',agent='codex',source='official',version=None,yes=False,confirm_local_changes=False,force=False,manifest_file=None,package_file=None);self.fixture('0.1.0')
 def tearDown(self): self.p.stop();m.ROOT=self.old;self.tmp.cleanup()
 def fixture(self,v,bad=False):
  b=io.BytesIO()
  with zipfile.ZipFile(b,'w') as z:
   prefix=m.ID+'/skills/'+m.ID+'/'
   z.writestr(prefix+'VERSION',v);z.writestr(prefix+'SKILL.md','name: '+m.ID+'\n'+v)
   if bad:z.writestr('../escape','x')
  data=b.getvalue();p=self.home/('pkg'+v+'.zip');p.write_bytes(data);mf=self.home/('m'+v+'.json');mf.write_text(json.dumps({'skill_id':m.ID,'latest':{'beta':v},'versions':{v:{'pre_release':True,'files':[{'size':len(data),'sha256':hashlib.sha256(data).hexdigest()}]}}}));self.a.package_file=str(p);self.a.manifest_file=str(mf)
 def run_action(self,c): self.a.command=c;m.run(self.a)
 def test_install_update_refuse_and_rollback(self):
  self.run_action('install');dest=m.location('codex');self.assertEqual((dest/'VERSION').read_text(),'0.1.0');self.fixture('0.1.1');self.run_action('update');self.assertEqual((dest/'VERSION').read_text(),'0.1.0');self.a.yes=True;self.run_action('update');self.assertEqual((dest/'VERSION').read_text(),'0.1.1');self.run_action('rollback');self.assertEqual((dest/'VERSION').read_text(),'0.1.0')
 def test_local_edits_are_backed_up_before_confirmation(self):
  self.run_action('install');dest=m.location('codex');(dest/'custom.md').write_text('local');self.fixture('0.1.1');self.a.yes=True;self.run_action('update');self.assertTrue((dest/'custom.md').exists());self.assertTrue(list((m.ROOT/'codex/backups').glob('*/skill/custom.md')));self.a.confirm_local_changes=True;self.run_action('update');self.assertFalse((dest/'custom.md').exists());self.run_action('rollback');self.assertEqual((dest/'custom.md').read_text(),'local');self.fixture('0.1.2');self.a.confirm_local_changes=False;self.run_action('update');self.assertTrue((dest/'custom.md').exists())
 def test_hash_and_zip_traversal(self):
  p=Path(self.a.package_file);p.write_bytes(p.read_bytes()+b'bad')
  with self.assertRaisesRegex(ValueError,'HASH'):self.run_action('install')
  self.fixture('0.1.0',True)
  with self.assertRaisesRegex(ValueError,'UNSAFE'):self.run_action('install')
  self.assertFalse(m.location('codex').exists())
 def test_seven_day_checks(self):
  self.run_action('install')
  with patch.object(m,'manifest',wraps=m.manifest) as fetch:
   self.run_action('check-update');self.run_action('check-update');self.assertEqual(fetch.call_count,1)
   sp=m.ROOT/'codex/state.json';s=m.read(sp);s['last_checked_at']-=8*86400;m.write(sp,s);self.run_action('check-update');self.assertEqual(fetch.call_count,2)
 def test_failed_check_is_nonblocking_and_throttled(self):
  self.run_action('install')
  with patch.object(m,'manifest',side_effect=TimeoutError('timeout')),patch('sys.argv',['manager.py','check-update','--agent','codex']): self.assertEqual(m.main(),0)
  with patch.object(m,'manifest') as fetch:self.run_action('check-update');fetch.assert_not_called()
 def test_multiple_hosts_requires_choice(self):
  (self.home/'.codex').mkdir();(self.home/'.claude').mkdir();self.a.agent='auto'
  with self.assertRaisesRegex(ValueError,'AGENT_SELECTION_REQUIRED'):self.run_action('install')
 def test_invalid_target_does_not_call_network(self):
  spec=importlib.util.spec_from_file_location('gateway',R/'skills/openlx-weixin-baimindan/scripts/gateway.py');g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
  with patch.object(g.urllib.request,'urlopen') as request:
   with self.assertRaisesRegex(ValueError,'TARGET_ACCOUNT_MISMATCH'):g.request({'target_account':'test-a','requested_action':'CREATE_DRAFT','prepared_payload_or_reference':{'appid':'test-b'},'user_intent':'create draft'})
   with self.assertRaisesRegex(ValueError,'EXPLICIT_PUBLICATION'):g.request({'target_account':'test-a','requested_action':'SUBMIT_EXPLICIT_PUBLISH','prepared_payload_or_reference':{'appid':'test-a','is_draft':False},'user_intent':'publish'})
   request.assert_not_called()
if __name__=='__main__':unittest.main()

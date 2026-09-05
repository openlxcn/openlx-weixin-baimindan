import {test} from 'node:test';import {execFileSync} from 'node:child_process';test('version sync',()=>execFileSync('node',['scripts/verify-version-sync.mjs']));

import {execFileSync} from 'node:child_process';execFileSync('node',['--test','tests/package-boundary.test.mjs','tests/secret-scan.test.mjs'],{stdio:'inherit'});

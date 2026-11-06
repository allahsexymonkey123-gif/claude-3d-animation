// Explicitly invoked helper. No token is requested or stored by this repository.
import {spawnSync} from 'node:child_process';
import fs from 'node:fs';
function run(command,args,opts={}) {
  const r=spawnSync(command,args,{stdio:'inherit',...opts});
  if(r.error||r.status!==0)throw Error(r.error?.message??`${command} exited ${r.status}`);
}
const dry=process.argv.includes('--dry-run');
const name=process.argv.find((v,i)=>i>1&&!v.startsWith('--'))??'zen-3d-explainer-shorts';
if(!/^[A-Za-z0-9_.-]+$/.test(name))throw Error('Pass a repository name, without owner or URL.');
if(!fs.existsSync('SKILL.md')||!fs.existsSync('references/manifest.json'))throw Error('Run from the repository root.');
const commands=[['gh',['auth','status']],['git',['init','-b','main']],['git',['add','.']],
  ['git',['commit','-m','Add reference-driven 3D explainer style and complete 30fps study']],
  ['gh',['repo','create',name,'--public','--source','.','--remote','origin','--push',
    '--description','30 fps low-poly 3D cutaway explainer style for Claude; detailed references, measurements and runnable templates']]];
if(dry){for(const [cmd,args] of commands)console.log(JSON.stringify([cmd,...args]));process.exit(0);}
if(fs.existsSync('.git'))throw Error('This folder already has Git history. Publish it manually; the helper will not replace history or remotes.');
if(spawnSync('gh',['--version'],{stdio:'ignore'}).status!==0)throw Error('Install GitHub CLI from https://cli.github.com, run gh auth login, then retry.');
run('gh',['auth','status']);
const profile=spawnSync('gh',['api','user'],{encoding:'utf8'});
if(profile.status!==0)throw Error('Could not read the authenticated GitHub account.');
const user=JSON.parse(profile.stdout);
if(!Number.isSafeInteger(user.id)||!user.login)throw Error('GitHub did not return a valid profile.');
// Use GitHub's verified account ID/login for a commit-only public noreply identity.
const author=['-c',`user.name=${user.name||user.login}`,'-c',`user.email=${user.id}+${user.login}@users.noreply.github.com`];
run('git',['init','-b','main']);run('git',['add','.']);
run('git',[...author,'commit','-m','Add reference-driven 3D explainer style and complete 30fps study']);
run('gh',commands[4][1]);
run('gh',['repo','view','--json','url','--jq','.url']);

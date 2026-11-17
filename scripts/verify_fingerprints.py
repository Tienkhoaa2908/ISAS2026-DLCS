#!/usr/bin/env python3
from pathlib import Path
import hashlib, argparse, subprocess, sys
from private_paths import outside_repo, private_root

def sha(p):
    h=hashlib.sha256();
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--data-root',type=Path,required=True); ap.add_argument('--out',type=Path,help='Rebuilt fingerprints CSV outside the repository worktree.'); a=ap.parse_args()
    try:
        r=outside_repo(a.data_root,'--data-root'); out=outside_repo(a.out or private_root()/'rebuilt_train_fingerprints.csv','--out')
    except ValueError as error:
        ap.error(str(error))
    out.parent.mkdir(parents=True,exist_ok=True)
    cmd=[sys.executable,str(r/'build_fingerprints.py'),'-i',str(r/'processed_ble_events.csv'),'-l',str(r/'fingerprint_location_intervals.csv'),'-o',str(out),'--window','10','--step','2','--features','mean,present,std,max,count','--past-context','8','--past-feats','count,std']
    subprocess.run(cmd,check=True)
    expected=r/'train_fingerprints.csv'; print('rebuilt ',sha(out)); print('expected',sha(expected)); print('match',sha(out)==sha(expected))
if __name__=='__main__': main()

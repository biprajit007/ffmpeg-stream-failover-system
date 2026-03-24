#!/usr/bin/env python3
import argparse, json

def main():
    p=argparse.ArgumentParser(description='ffmpeg-stream-failover-system')
    p.add_argument('--dry-run', action='store_true')
    p.add_argument('args', nargs='*')
    a=p.parse_args()
    print(json.dumps({'project': 'ffmpeg-stream-failover-system', 'args': a.args, 'dry_run': a.dry_run}, indent=2))

if __name__ == '__main__':
    main()

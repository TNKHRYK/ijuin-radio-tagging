#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
深夜の馬鹿力の年度フォルダ名からスペースを一括削除
例: "深夜の馬鹿力 2025年" → "深夜の馬鹿力2025年"
"""

import os
import re
from pathlib import Path

def rename_year_folders(base_path, start_year=1995, end_year=2025, dry_run=True):
    """
    指定された範囲の年度フォルダ名からスペースを削除
    
    Args:
        base_path: 本放送フォルダのパス
        start_year: 開始年
        end_year: 終了年
        dry_run: True の場合、実際の変更を行わない
    """
    base_path = Path(base_path)
    
    if not base_path.exists():
        print(f"エラー: パスが存在しません: {base_path}")
        return
    
    print(f"処理対象ディレクトリ: {base_path}")
    print(f"対象年度: {start_year}年 〜 {end_year}年")
    print(f"モード: {'ドライラン（確認のみ）' if dry_run else '実行モード'}")
    print("=" * 60)
    
    success_count = 0
    skip_count = 0
    error_count = 0
    
    # 年度ごとに処理
    for year in range(start_year, end_year + 1):
        old_name = f"深夜の馬鹿力 {year}年"
        new_name = f"深夜の馬鹿力{year}年"
        
        old_path = base_path / old_name
        new_path = base_path / new_name
        
        # 既に変更済みの場合
        if not old_path.exists() and new_path.exists():
            print(f"✓ 既に変更済み: {new_name}")
            skip_count += 1
            continue
        
        # フォルダが存在しない場合
        if not old_path.exists():
            print(f"- スキップ: {old_name} (フォルダが存在しません)")
            skip_count += 1
            continue
        
        # 変更処理
        if dry_run:
            print(f"○ 変更予定: {old_name} → {new_name}")
            success_count += 1
        else:
            try:
                # 既に新しい名前のフォルダが存在する場合の確認
                if new_path.exists():
                    print(f"⚠ 警告: {new_name} は既に存在します")
                    response = input("  上書きしますか？ (y/N): ")
                    if response.lower() != 'y':
                        print(f"  → スキップしました")
                        skip_count += 1
                        continue
                
                # リネーム実行
                old_path.rename(new_path)
                print(f"✓ 変更完了: {old_name} → {new_name}")
                success_count += 1
                
            except Exception as e:
                print(f"✗ エラー: {old_name} の変更に失敗: {e}")
                error_count += 1
    
    # 結果のサマリー
    print("=" * 60)
    print(f"処理結果:")
    print(f"  成功: {success_count} 件")
    print(f"  スキップ: {skip_count} 件")
    print(f"  エラー: {error_count} 件")
    print(f"  合計: {success_count + skip_count + error_count} / {end_year - start_year + 1} 件")

def list_year_folders(base_path):
    """現在の年度フォルダ一覧を表示"""
    base_path = Path(base_path)
    
    if not base_path.exists():
        print(f"エラー: パスが存在しません: {base_path}")
        return
    
    print(f"現在のフォルダ一覧: {base_path}")
    print("=" * 60)
    
    # 深夜の馬鹿力で始まるフォルダを検索
    folders = []
    for item in sorted(base_path.iterdir()):
        if item.is_dir() and item.name.startswith("深夜の馬鹿力"):
            folders.append(item.name)
    
    if folders:
        for folder in folders:
            # スペースの有無を表示
            if " " in folder:
                print(f"[ ] {folder} (スペースあり)")
            else:
                print(f"[✓] {folder}")
    else:
        print("深夜の馬鹿力フォルダが見つかりません")
    
    print(f"\n合計: {len(folders)} フォルダ")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='深夜の馬鹿力の年度フォルダ名からスペースを削除'
    )
    parser.add_argument('base_path', 
                       help='本放送フォルダのパス')
    parser.add_argument('--start-year', type=int, default=1995,
                       help='開始年 (デフォルト: 1995)')
    parser.add_argument('--end-year', type=int, default=2025,
                       help='終了年 (デフォルト: 2025)')
    parser.add_argument('--list', '-l', action='store_true',
                       help='現在のフォルダ一覧を表示')
    parser.add_argument('--execute', '-e', action='store_true',
                       help='実際に名前を変更（デフォルトはドライラン）')
    
    args = parser.parse_args()
    
    if args.list:
        # フォルダ一覧を表示
        list_year_folders(args.base_path)
    else:
        # リネーム処理
        rename_year_folders(
            args.base_path,
            start_year=args.start_year,
            end_year=args.end_year,
            dry_run=not args.execute
        )

if __name__ == "__main__":
    main()
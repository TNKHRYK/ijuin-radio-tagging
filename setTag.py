#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
from typing import Optional
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError
import time


class MP3TagProcessor:
    """MP3ファイルのタグ処理とファイル名変更を行うクラス"""
    
    def __init__(self):
        self.artist = '伊集院 光'
        self.genre = 'Radio'
        self.album_prefix = '深夜の馬鹿力 '
    
    def show_id3_tags(self, file_path: str) -> None:
        """ID3タグを表示する"""
        try:
            tags = EasyID3(file_path)
            print(tags.pprint())
        except ID3NoHeaderError:
            print(f"エラー: {file_path} はID3タグがありません")
        except Exception as e:
            print(f"エラー: タグの読み込みに失敗しました - {e}")
    
    def set_id3_tag(self, file_path: str) -> bool:
        """ID3タグを設定する"""
        try:
            tags = EasyID3(file_path)
            current_year = time.strftime('%Y')
            
            tags['author'] = self.artist
            tags['artist'] = self.artist
            tags['album'] = f'{self.album_prefix}{current_year}年'
            tags['genre'] = self.genre
            tags['title'] = os.path.splitext(os.path.basename(file_path))[0]
            
            tags.save()
            return True
        except ID3NoHeaderError:
            print(f"エラー: {file_path} はID3タグがありません")
            return False
        except Exception as e:
            print(f"エラー: タグの設定に失敗しました - {e}")
            return False
    
    def rename_file(self, file_path: str) -> Optional[str]:
        """ファイル名を変更する"""
        try:
            new_name = file_path.replace('伊集院光 深夜の馬鹿力 ', 'JUNK伊集院光・深夜の馬鹿力')
            
            if new_name != file_path:
                os.rename(file_path, new_name)
                return new_name
            return file_path
        except OSError as e:
            print(f"エラー: ファイル名の変更に失敗しました - {e}")
            return None
    
    def process_file(self, file_path: str) -> bool:
        """MP3ファイルを処理する（タグ設定とファイル名変更）"""
        if not os.path.exists(file_path):
            print("対象ファイルが見つかりません")
            return False
        
        if not self.set_id3_tag(file_path):
            return False
        
        new_file_path = self.rename_file(file_path)
        if new_file_path is None:
            return False
        
        self.show_id3_tags(new_file_path)
        return True


def main():
    """メイン関数"""
    if len(sys.argv) != 2:
        print("使用法: python setTag.py <MP3ファイル>")
        sys.exit(1)
    
    target_file = sys.argv[1]
    processor = MP3TagProcessor()
    
    if not processor.process_file(target_file):
        sys.exit(1)


if __name__ == '__main__':
    main()

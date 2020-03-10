https://www.mobilesuica.com/index.aspx で得られるsuicaの交通費の履歴を、freeeで読み込めるようなxlsxの形式に変換するためのスクリプトです。

# Installation

```bash
pip install -r requirements.txt
```

# 使い方

1. suicaの履歴が記入されたtsvの用意
   suicaの履歴のtsvは以下のようなフォーマットで与える。

   > 2020/1/4	入	御茶ノ水	出	新宿　　	"¥5,454"	-168
   >
   > 2020/1/4	入	地　池袋	出	地御茶水	"¥5,622"	-199

   また、

   > 1/4	入	御茶ノ水	出	新宿　　	"¥5,454"	-168
   >
   > 1/4	入	地　池袋	出	地御茶水	"¥5,622"	-199

   のように年を指定しなければ、自動的に実行している年として解釈される。
   https://www.mobilesuica.com/index.aspx から辿れる履歴画面の表をコピーしてエクセルに貼り付ければ、自然とこのような形式で保存される。

   

2. suicaの履歴が記入されたtsvから交通費の情報を抽出し、freeeで読み込めるxlsxに変換
   例えば次のようにして実行する。

	```bash
	python3 convert_freee_format.py -i suica.tsv  -o converted.xlsx
	```

	ここで-iに用意したtsv、-oに変換後のファイルパスを指定する。

   
   
3. xlsxのアップロード

   xlsxファイルをfreeeの以下のページにドラッグアンドドロップして読み込ませる。
   https://secure.freee.co.jp/spreadsheets/import
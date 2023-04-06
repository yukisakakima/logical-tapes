# crud.py
from model import db, UserInfo

# モデルからテーブルを作成する(インポートされているモデルすべてが対象)
db.create_all()

# モデルで定義したデータクラスのインスタンスを作成する。
man1 = UserInfo("Hirota", "Taro", "askdfj.@", "kasjdfipq")
man2 = UserInfo("Tanaka", "Masato", "askd5j.@", "sjdfipqdf")
man3 = UserInfo("Mitani", "Ken", "askdf7.@", "fipqsdfsdf")

print(man1, man2, man3)
# 作成したテーブルにを追加する(add:追加　add_all：リスト形式の一括追加)
db.session.add_all([man1, man2])
db.session.add(man3)

# テーブルへの変更をcommitで確定する。
db.session.commit()
print(man1, man2, man3)
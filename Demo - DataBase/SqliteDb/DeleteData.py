#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

# 连接数据库，不存在则自动创建
conn = sqlite3.connect("test.db")

# 创建一个新
cursor = conn.cursor()

# 添加一条记录
cursor.execute("Delete from TXT_USER")

# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭连接
conn.close()

print(cursor.rowcount)

print("删除完成！")

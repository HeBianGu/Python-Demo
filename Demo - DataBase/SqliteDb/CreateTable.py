#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

# 连接数据库，不存在则自动创建
conn = sqlite3.connect("test.db")

# 创建一个新表
cursor=conn.cursor();

cursor.execute("""CREATE TABLE  TXT_USER
(

            ID varchar(50),

            NAME varchar(50),

            AGE varchar(50),

            GENDER varchar(50),

            CreateDate varchar(50),

            UpdateDate varchar(50),

            IsUpdate varchar(50)
);""")

# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭连接
conn.close()


print("创建成功！")

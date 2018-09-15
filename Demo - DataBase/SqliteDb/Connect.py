#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

# 连接数据库，不存在则自动创建
conn = sqlite3.connect("test.db")

# 提交事务
conn.commit()
# 关闭连接
conn.close()

#!/usr/bin python
# coding: utf8
import psycopg2


conn = psycopg2.connect("dbname='scp'\
						 user='postgres'\
						 host='localhost'\
						 password=''")
c = conn.cursor()

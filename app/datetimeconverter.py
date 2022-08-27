from dateutil import parser

dt = "2022-06-21 00:47:33.161589"

n_dt = parser.parse(dt)

print(type(n_dt))
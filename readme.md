数据库作业，处理10gtxt文件，将10g导入到Mysql中，并实现查询和导出，简单可视化

思路：对10gtxt数据进行分割后导入mysql

create table DB_gps(
car_id varchar(6) not null comment '车辆标识',
event int(2) not null comment '触发事件',
status int(2) not null comment '运营状态',
gps_date date not null comment 'GPS时间',
gps_lon float(8,4) not null comment 'GPS经度',
gps_lat float(8,4) not null comment 'GPS维度',
gps_speed int(4) not null comment 'GPS速度',
gps_dir int(4) not null comment 'GPS方位',
gps_status int (2) not null comment 'GPS状态'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;



数据量为：1亿8千万条数据


spl_size.py  按照文件流读取的大小进行文件的切割。效率更快
spl_rows.py  按照预设置的行数进行文件切割。
use_sql.py   读取切割好后的文件目录，添加Load data+'filename' 到txt中，然后使用bat 批处理导入到mysql中。

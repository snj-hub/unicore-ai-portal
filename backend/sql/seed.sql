USE unicore_ai;

INSERT INTO students (id,name,mobile,email,dept,year,section,roll_no) VALUES
(1,'Aarthi K','9876500011','23051710500111071@vcsm.ac.in','Computer Science',2,'A','CS2101'),
(2,'Bala R','9876500022','23051710500111072@vcsm.ac.in','BBA',1,'B','BBA1102'),
(3,'Charan V','9876500033','23051710500111073@vcsm.ac.in','Physics',3,'A','PHY3103')
ON DUPLICATE KEY UPDATE name=VALUES(name);

INSERT INTO fees (student_id,total_amount,paid_amount,last_payment_date) VALUES
(1,21000,21000,'2026-01-03'),
(2,21000,15000,'2026-01-05'),
(3,21000,0,NULL)
ON DUPLICATE KEY UPDATE paid_amount=VALUES(paid_amount);

INSERT INTO attendance (student_id,date,subject,present_bool) VALUES
(1,'2026-01-10','Math',1),(1,'2026-01-11','Physics',1),(2,'2026-01-10','Math',1),(2,'2026-01-11','Physics',0),(3,'2026-01-10','Math',0);

INSERT INTO timetable (day_order,day_name,period_no,start_time,end_time,subject,faculty) VALUES
(3,'Monday',1,'10:00:00','10:50:00','Mathematics','Dr. Kumar'),
(3,'Monday',5,'14:40:00','15:45:00','AI Lab','Ms. Devi'),
(4,'Tuesday',1,'09:00:00','09:50:00','Data Structures','Mr. Arun');

INSERT INTO day_orders (date,day_order) VALUES (CURDATE(),3) ON DUPLICATE KEY UPDATE day_order=VALUES(day_order);

INSERT INTO exams (title,date,time,syllabus_link) VALUES
('Data Structures','2026-03-02','10:00:00','https://vcsm.ac.in/syllabus/ds'),
('Maths II','2026-03-06','13:30:00','https://vcsm.ac.in/syllabus/m2');

INSERT INTO events (title,date,category,description,is_past) VALUES
('Innovation Summit','2026-03-05','Academic','Inter-department innovation showcase',0),
('Cultural Fest','2025-11-20','Cultural','Annual arts and cultural fest',1);

INSERT INTO placement_news (title,date,content,tags) VALUES
('TechWave Campus Drive','2026-02-10','TechWave hiring final year students','drive,software'),
('Placement Record Update','2026-01-28','78% placements achieved this season','stats,highlights');

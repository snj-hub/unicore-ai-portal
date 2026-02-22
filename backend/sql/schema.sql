CREATE DATABASE IF NOT EXISTS unicore_ai;
USE unicore_ai;

CREATE TABLE IF NOT EXISTS students (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  mobile VARCHAR(10) UNIQUE NOT NULL,
  email VARCHAR(150) UNIQUE NOT NULL,
  dept VARCHAR(100),
  year INT,
  section VARCHAR(10),
  roll_no VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS otp_logins (
  mobile VARCHAR(10) PRIMARY KEY,
  otp_hash VARCHAR(255) NOT NULL,
  expires_at DATETIME NOT NULL,
  attempts INT DEFAULT 0,
  last_sent_at DATETIME
);

CREATE TABLE IF NOT EXISTS fees (
  student_id INT PRIMARY KEY,
  total_amount DECIMAL(10,2),
  paid_amount DECIMAL(10,2),
  last_payment_date DATE,
  FOREIGN KEY (student_id) REFERENCES students(id)
);

CREATE TABLE IF NOT EXISTS attendance (
  id INT PRIMARY KEY AUTO_INCREMENT,
  student_id INT,
  date DATE,
  subject VARCHAR(100),
  present_bool BOOLEAN,
  FOREIGN KEY (student_id) REFERENCES students(id)
);

CREATE TABLE IF NOT EXISTS timetable (
  id INT PRIMARY KEY AUTO_INCREMENT,
  day_order INT,
  day_name VARCHAR(20),
  period_no INT,
  start_time TIME,
  end_time TIME,
  subject VARCHAR(100),
  faculty VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS day_orders (
  id INT PRIMARY KEY AUTO_INCREMENT,
  date DATE UNIQUE,
  day_order INT
);

CREATE TABLE IF NOT EXISTS exams (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(200),
  date DATE,
  time TIME,
  syllabus_link VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS events (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(200),
  date DATE,
  category VARCHAR(100),
  description TEXT,
  is_past BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS placement_news (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(200),
  date DATE,
  content TEXT,
  tags VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS admin_users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  email VARCHAR(150),
  password_hash VARCHAR(255)
);

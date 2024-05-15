-- create user.
CREATE USER 'holberton_user@localhost' IDENTIFIED WITH mysql_native_password BY 'projectcorrection280hbtn';
-- Grant privileges to user
GRANT ALL PRIVILEGES ON *.* TO 'holberton_user@localhost' IDENTIFIED WITH mysql_native_password BY 'projectcorrection280hbtn'; 

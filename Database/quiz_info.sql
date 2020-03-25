\c quiz;

create table if not exists quiz
(question_id SERIAL primary key,
category varchar(22), 
question varchar(120),
options_1 varchar(400),
options_2 varchar(400),
option_3 varchar(400),
option_4 varchar(400),
answer varchar(400)
);

Insert into quiz (category, question, options_1, options_2, option_3, option_4, answer) values('python','Python latest version?','python 1.7','python 1.6','python 2.6','python 3.7', 'python 3.7');
Link admin : http://127.0.0.1:8000/admin/
Link user : http://127.0.0.1:8000/fels

Database : projectLearn.json
Tài khoản test :
-	Admin : 123 pass 123
-	User : trang pass 123

######################################
- User
+ Course
	+ xem danh sách course
	+ xem chi tiết course
	+ xem danh sách các Lesson thuộc Course
	+ xem trạng thái của User của Lesson ( learning or join )
+ Lesson
	+ xem danh sách các Lesson ( Những Lesson ở trạng thái Enable )
	+ Xem chi tiết Lesson
		- Xem chi tiết thông tin của Lesson
		- Xem danh sach các từ trong Lesson
		- Xem danh sách các User join vào Lesson
		- Thực hiện Exam của Lesson
+ Exam
	+ Thực hiện làm bài thi với những từ nằm trong Lesson
	+ Chọn các lựa chọn đúng cho từ
	+ Submit để gửi bài thi. 
	+ Chấm điểm bài thi ( số câu đúng ) và hiển thị cho User ( số câu đúng, câu nào đúng, câu nào sai )
+ Word
	+ Xem danh sach cac từ 
	+ Lọc từ theo ngôn ngữ
	+ Tìm kiếm từ theo từ khoa
	+ Xem chi tiết về từ
		- Xem từ đang thuộc những Lesson nào ?
	+ Xem lại những từ đã học thuộc ( những từ trả lời đúng trong các Exam )
+ Profile
	+ Đăng nhập, đăng ký, đăng xuất
	+ Thay đổi thông tin ca nhân
	+ Thay đổi mật khẩu
#############################################################################################
#############################################################################################
- Admin
+ Course
	+ Xem danh sách các Course
	+ Tạo Course mới
	+ Xem chi tiết Course
		- Tạo Lesson mới thuộc Course hiện tại
		- Xem danh sach các Lesson thuộc Course
		- Xem được trạng thái của các Lesson thuộc Course
		- Được phép Edit Lesson ( nội dung và tên Lesson )
		- Được Delete những Lesson ở trạng thái Disabled 
+ Lesson 
	+ Xem chi tiết các Lesson 
	+ Xemm danh sach các từ khóa, User trong Lesson
	+ Edit Lesson 
		- Chỉnh sửa thông tin Lesson
		- Thay đổi trạng thái từ Disabled -> Enable 
	+ Thêm từ vào Lesson
		- Chỉ thêm dc từ vào Lesson có trạng thái là Disabled
		- Chỉ thêm những từ đã đầy đủ thông tin
		- Hiển thi danh sách từ ko thuộc Lesson
		- Remover từ khỏi Lesson 
	+ Remover thành viên khỏi Lesson ( chuyển trạng thái trong database True -> False )
+ Word 
	+ Xem danh sach  các từ, lọc từ theo ngôn ngữ, tìm kiếm từ
	+ Chinh sủa từ 
	+ Xóa từ ( chỉ xóa dc từ khi từ chưa thuộc 1 Lesson nào )
	+ Thêm các đáp án khác cho từ ( Tói đa 3 )
	


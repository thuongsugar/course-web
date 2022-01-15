# **Trang web học và thi online**
*Ngôn ngữ Python*

## Thông tin
Trang web cho phép người dùng tìm kiếm và đăng ký các khóa học có trên  web ở mỗi khóa học sẽ có các bài học theo video đính kèm, học xong người dùng có thể kiểm tra kiến thức đã học qua các bài kiểm tra có sẵn trên web và có thể xem lại số điểm qua các lần kiểm tra của mình.


## Cài đặt
*yêu cài máy của bạn đã cài đặt python3*
```
pip install Django Pillow mysqlclient django-ckeditor
```
Mở mysql và tạo một cơ sở dữ liệu có tên là ***course_web*** nếu không muốn có thể thay đổi tên khác và bạn sẽ vào file **setting** tìm 
``` 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'course_web',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost'


    }
}
 ```
hãy xóa tên cở sở dữ liệu cũ **course_web** và thay nó thành tên của bạn. 

Bây giờ hãy mở dự án lên đứng ở thư mục gốc vào cửa sổ **Terminal** thực hiện 
``` 
python .\manage.py migrate
```
Tạo một tài khoản quản trị viên cho trang web
```
python .\manage.py createsuperuser
```
hãy nhập **username email password** để hoàn tất

Và chạy trang web
``` 
python .\manage.py runserver
```
mặc định trang web chạy ở địa chỉ [http://localhost:8000/](http://localhost:8000/)

Truy cập [http://localhost:8000/admin](http://localhost:8000/admin) và đăng nhập bằng tài khoản vừa tạo để thêm dữ liệu cho trang web.

Bảng **Catygorys:** thông tin các danh mục khóa học

Bảng **Courses:** thông tin các khóa học tương ứng với mỗi danh mục trên

Bảng **Lessons:** thông tin các bài học tương ứng với mỗi khóa học

* Trường **Link** lấy từ link *Youtube*

Bảng **Quizs:** thông tin của bài kiểm tra

Bảng **Questions:** nội dung câu hỏi tương ứng với bài kiểm tra

* Có thể thêm luôn đáp án ở trong bảng này, đáp án nào đúng hãy đánh dấu bên cột **correct**

Bảng **Answers:** nội dung câu trả lời cho câu hỏi tương ứng

Bảng **Results:** kết quả sau khi người dùng làm bài kiểm tra

* Có tính số lần người dùng vi phạm 

Bảng **Users:** tất cả thông tin người dùng trang web

* Mật khẩu đã được mã hóa, không vi phạm quên riêng tư


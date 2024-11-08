from nicegui import ui
from login_backend import User , UserDatabase
from datetime import datetime, timedelta
user_db = UserDatabase()


# Các hàm tiện ích (utility functions)
def create_centered_container():
    # Tạo container căn giữa màn hình
    return ui.element('div').style('position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 100%; max-width: 400px;')

def redirect(url: str):
    # Chuyển hướng trang
    ui.run_javascript(f'window.location.href = "{url}"')

def get_date_limits():
    # Lấy giới hạn ngày cho input date
    today = datetime.now()
    max_date = today.strftime('%Y-%m-%d')  # Ngày hiện tại
    min_date = (today - timedelta(days=365 * 100)).strftime('%Y-%m-%d')  # 100 năm trước
    return min_date, max_date


@ui.page('/')
def register_page():
    ui.query('body').style('margin: 0; padding: 0; background: linear-gradient(135deg, #f0f4ff, #e5e7ff);')
    # Lấy giới hạn ngày
    min_date, max_date = get_date_limits()
    
    # Tạo giao diện đăng ký
    with create_centered_container():

        with ui.card().classes('w-full p-8 rounded-lg shadow-lg'):
            # Tiêu đề
            ui.label('Sign up').classes('text-3xl front-bold text-center mb-6')
            
            with ui.column().classes('w-full gap-4') as form_container:
                # Form đăng ký
                username_input = ui.input('Login name*').props('rounded').props('outlined required').classes('w-full')
                fullname_input = ui.input('User name*').props('rounded').props('outlined required').classes('w-full')
                email_input = ui.input('Email*').props('rounded').props('outlined required type=email').classes('w-full')
                birthdate_input = ui.input('Date of birth*').props('rounded').props(f'outlined required type=date min="{min_date}" max="{max_date}"').classes('w-full')
                password_input = ui.input('Password*').props('rounded').props('outlined required type=password').classes('w-full')
                confirm_password_input = ui.input('Confirm password*').props('rounded').props('outlined required type=password').classes('w-full')
                
                # Thông báo
                ui.label('* Please enter correctly and remember the information to retrieve your password when necessary').classes('text-red-500 text-sm mb-2')

                # Nút đăng ký
                register_button = ui.button('SIGN UP').props('rounded').classes('w-full bg-indigo hover:bg-indigo text-white font-semibold py-2 rounded-lg shadow-md')
                
                # Xử lý đăng ký
                async def validate_and_register():
                    # Kiểm tra ngày sinh
                    if not birthdate_input.value:
                        ui.notify('Please enter your date of birth!', color='negative')
                        return
                    
                    # Kiểm tra định dạng ngày
                    input_date = datetime.strptime(birthdate_input.value, '%Y-%m-%d')
                    min_date_obj = datetime.strptime(min_date, '%Y-%m-%d')
                    max_date_obj = datetime.strptime(max_date, '%Y-%m-%d')

                    # Validate ngày sinh
                    if input_date < min_date_obj or input_date > max_date_obj:
                        birthdate_input.value = min_date
                        ui.notify('Invalid date of birth', color='negative')
                        return
                    
                    # Kiểm tra mật khẩu
                    if password_input.value != confirm_password_input.value:
                        ui.notify('Password does not match!', color='negative')
                        return
                    
                    # Kiểm tra email
                    if not '@' in email_input.value:
                        ui.notify('Invalid email!', color='negative')
                        return
                    
                    # Tạo user mới
                    new_user = User(
                        username=username_input.value,
                        fullname=fullname_input.value,
                        email=email_input.value,
                        birthdate=birthdate_input.value,
                        password=password_input.value
                    )
                    
                    # Thêm user vào database
                    success, message = user_db.add_user(new_user)
                    if success:
                        print(f"User registered: {new_user.__dict__}")

                    ui.notify(message, color='positive' if success else 'negative')
                    if success:
                        register_button.visible = False
                        ui.link('Back to log in', '/').classes('w-full text-center text-blue-500 hover:text-blue-700 cursor-pointer no-underline')

                register_button.on_click(validate_and_register)
ui.run()

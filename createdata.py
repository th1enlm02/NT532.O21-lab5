import cv2
import os

def create_dataset(name, save_path='Dataset/raw', num_images=200):
    # Kiểm tra và tạo thư mục lưu trữ nếu chưa tồn tại
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Tạo thư mục cho người dùng nếu chưa tồn tại
    person_path = os.path.join(save_path, name)
    if not os.path.exists(person_path):
        os.makedirs(person_path)

    # Mở camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Không thể mở camera")
        return

    count = 0
    while count < num_images:
        ret, frame = cap.read()
        if not ret:
            print("Không thể nhận frame từ camera")
            break

        # Hiển thị frame
        cv2.imshow('Capture', frame)

        # Lưu frame vào thư mục với tên người dùng
        img_name = os.path.join(person_path, f"{name}_{count+1}.jpg")
        cv2.imwrite(img_name, frame)
        print(f"Đã lưu {img_name}")

        count += 1

        # Thoát khi nhấn phím 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Giải phóng camera và đóng các cửa sổ
    cap.release()
    cv2.destroyAllWindows()

# Gọi hàm để tạo dataset cho một người dùng với tên 'user1'
create_dataset(name='tranchucthien', num_images=500)

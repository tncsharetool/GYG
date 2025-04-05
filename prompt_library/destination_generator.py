# prompt_library/destination_generator.py

def generate_destination(prompt: str) -> dict:
    # Giả lập logic sinh nội dung bằng prompt (mock)
    if "Đà Lạt" in prompt:
        return {"location": "Đà Lạt", "days": 3, "highlight": "Thung lũng Tình Yêu"}
    elif "Nha Trang" in prompt:
        return {"location": "Nha Trang", "days": 3, "highlight": "Vinpearl Land"}
    else:
        return {"location": "Việt Nam", "days": 2, "highlight": "Ẩm thực đường phố"}

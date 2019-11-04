import pandas as pd
xl = pd.ExcelFile('./datas/neural_data.xlsx')
# get the first sheet as an object
df = pd.read_excel(xl, 0, header=None)


print(df.__len__())

print(df.iloc[1, 1])
df.iloc[1, 1] = 1

print(df.iloc[1, 1])
#s = "Sự thực là khá tò mò khi thấy bạn bè check in khi quán mới Vị trí view hồ khá đẹp nhưng k gian quá lúc mình tới đang là mùa rất nóng nhưng trên tầng điều hoà quạt thì có duy nhất thực sự k thể thở Phòng cũng khá cảm giác mọi thứ bàn ghế bừa bộn k đc vệ sinh order đồ thì cái gì cũng Trà thì quá bt nếu k muốn nói là thất k đặc Nghe nói là hãng trà sữa việt nên cũng muốn trải nghiệm ủng hộ nhưng thực tình sau lần này thì k thể ủng hộ đc nữa"
#Chuẩn hóa về chữ thường
#s = s.lower()
#print(s)
#Thay thế các url trong dữ liệu bởi link_spam

#Tách từ

#Loại bỏ dấu câu và các ký tự đặc biệt


#Xử lý các trường hợp người dùng láy âm tiết


#Chuẩn hóa các từ viết tắc cơ bản ( vd : k, ko k0 -> không, bt -> bình thường )


#Loại bỏ số và các từ có 1 ký tự
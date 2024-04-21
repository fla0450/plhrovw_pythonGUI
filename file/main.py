import tkinter as tk
from PIL import ImageTk, Image
import requests
import json
import io


def get_Coordinates():
    client_id = "91kkuktuv8"
    client_secret = "fXUvN9IUvkZXuWI1TeKv1YKS8I3TKi9nApdn4Pog"
    query = "경남 양산시 중앙로 133"
    endpoint ="https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    headers = {
        "X-NCP-APIGW-API-KEY-ID" : client_id,
        "X-NCP-APIGW-API-KEY": client_secret
    }
    Accept = "application/json"
    url = f"{endpoint}?query={query}&Accept={Accept}"
    res = requests.get(url,headers=headers)
    new_json = json.loads(res.text)
    x = new_json['addresses'][0]['x']
    y = new_json['addresses'][0]['y']
    address =[x,y]
    return address
def send_api():
    # NCP 콘솔에서 복사한 클라이언트ID와 클라이언트Secret 값
    client_id = "rim865ejp1"
    client_secret = "raprPBPoRJjyzw8cdCKIQFOdHXeBAYipQ08fIXFF"

    # 좌표 (경도, 위도)
    endpoint = "https://naveropenapi.apigw.ntruss.com/map-static/v2/raster"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,
    }
    address = get_Coordinates()
    # 중심 좌표
    lon, lat = address[0], address[1]
    _center = f"{lon},{lat}"
    # 줌 레벨 - 0 ~ 20
    _level = 16
    # 가로 세로 크기 (픽셀)
    _w, _h = 700, 600
    # 지도 유형 - basic, traffic, satellite, satellite_base, terrain
    _maptype = "satellite"
    # 반환 이미지 형식 - jpg, jpeg, png8, png
    _format = "png"
    # 고해상도 디스펠레이 지원을 위한 옵션 - 1, 2
    _scale = 1
    # 마커
    _markers = f"""type:d|size:mid|pos:{lon} {lat}|color:red"""
    # 라벨 언어 설정 - ko, en, ja, zh
    _lang = "ko"
    # 대중교통 정보 노출 - Boolean
    _public_transit = False
    # 서비스에서 사용할 데이터 버전 파라미터 전달 CDN 캐시 무효화
    _dataversion = "201.3"

    # URL
    url = f"{endpoint}?center={_center}&level={_level}&w={_w}&h={_h}&maptype={_maptype}&format={_format}&scale={_scale}&markers={_markers}&lang={_lang}&public_transit={_public_transit}&dataversion={_dataversion}"
    res = requests.get(url, headers=headers)

    image_data = io.BytesIO(res.content)
    image  = Image.open(image_data)
    return image
def mainPage():
    button_label.place(x=400, y=415)
    start_button.place(x=270, y=380)
    min_label3.place(x=388, y=310)
    min_label2.place(x=170, y=310)
    min_label1.place(x=170, y=270)
    title_label.place(x=160, y=166)
def StartButtonClick():
    title_label.place(x=5000,y=5000)
    min_label1.place(x=5000,y=5000)
    min_label2.place(x=5000,y=5000)
    min_label3.place(x=5000,y=5000)
    button_label.place(x=5000,y=5000)
    start_button.place(x=5000,y=5000)
    map_label.place(x=0,y=0)
    window.config(bg="#FFFFFF")
    business_button1.place(x=700,y=100)
if __name__ == "__main__":
    #window은 프레임
    window = tk.Tk()
    window.title("MARKETINYOU")
    window.geometry("1024x600")#화면 화질설정
    window.config(bg="#B22B15")#blackground 설정
    window.resizable(False,False)
    #라벨 설정
    title_label = tk.Label(window,text="MARKETINYOU")
    title_label.config(font=("Black Han Sans",70),fg="#FFFFFF",bg="#B22B15")

    #작은 글자
    min_label1 = tk.Label(window,text="전통의 맛과 멋이 살아 숨쉬는 곳,")
    min_label1.config(font=("Gowun Dodum",23),fg="#FFFFFF",bg="#B22B15")

    min_label2 = tk.Label(window,text="MARKETINYOU")
    min_label2.config(font=("Gowun Dodum",23),fg="#FFC786",bg="#B22B15")


    min_label3 = tk.Label(window,text="로 재밌는 시장 여행을 떠나보세요!")
    min_label3.config(font=("Gowun Dodum",23),fg="#FFFFFF",bg="#B22B15")


    img = ImageTk.PhotoImage(Image.open("../imges/button.png"))
    start_button = tk.Button(window,image=img,bg="#B22B15",command=StartButtonClick)
    start_button.config(highlightthickness=0,bd=0)
    start_button.config(activebackground="#B22B15")

    #버튼
    button_label = tk.Label(window,text='시작하기')
    button_label.config(font=("Gowun Dodum",25),bg="#EDDCC2")
    mainPage()
    send_api()
    map_img = send_api()
    photo_image = ImageTk.PhotoImage(map_img)
    map_label = tk.Label(window,image=photo_image)
    #지도 버튼
    business_button1 = tk.Button(window,image=img)
    business_button1.config(highlightthickness=0,bd=0)
    business_button1.config(activebackground="#FFFFFF")
    business_button1.place(x=5000,y=5000)
    #실행
    window.mainloop()

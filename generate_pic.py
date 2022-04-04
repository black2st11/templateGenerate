from PIL import Image, ImageFont, ImageDraw
import os
import textwrap

# 한글 14 포인트 기준 한 글자당 width 11, 특수 기호 / 는 5, 글자당 공백 1, .글자는 2, 띄어쓰기 4
def calc_textsize(text):
    result = 0
    #문자마다 크기가 다름
    for i in text:
        # 특문 처리
        if  ord(i)<= 47:
            result += 2
        # 숫자 처리
        elif 48 <= ord(i) and ord(i) <= 57:
            result += 5
        else : 
            # 한글은 평균 11
            result += 11
        # 글자가 쓰이고 난 후 있는 공백
        result += 2
    else :
        # 마지막 공백 삭제
        result -= 2
    return result



fonts_folder = './static'
selectFont = ImageFont.truetype(os.path.join(fonts_folder, 'NotoSansKR-Medium.otf'), 14)

background = Image.new(mode="RGB", size=(1200, 400), color='black')
background_draw = ImageDraw.Draw(background)
var_title = "Python Image Generate"
var_title_width_length = 7
var_pad = 10

var_title_wrap = textwrap.wrap(var_title, width=var_title_width_length)

var_len_line = len(var_title_wrap)

var_x = 1200/2
var_y = 400/2

var_textsize_h = background_draw.textsize(var_title_wrap[0], font=selectFont)[1]

var_y_point = var_y - (((var_textsize_h * var_len_line) + (var_pad * (var_len_line - 1))) / 2) + (var_textsize_h / 2)
for var_line in var_title_wrap:
 
    # 이미지에 텍스트 출력
    w, h = background_draw.textsize(var_line)

    result = background_draw.text(((1200-w)/2, var_y_point)
                , var_line
                , 'white'
                , font=selectFont
                , stroke_width=0
                , stroke_fill='white')
    print(result)
    # 글자 height 추가
    var_y_point = var_y_point + var_textsize_h + var_pad

background.save('./static/test1.png')


target = Image.open('./static/table.png')

draw = ImageDraw.Draw(target)
text = ['검/흰/노', '폴리에스테르', '약간 두꺼움', '잘 늘.어.남', '55', '약간 비침']
column = 200
for i in range(len(text)):
    draw.text((column * i + ((200 - (calc_textsize(text[i]))) // 2), 90), text[i], '#292929', selectFont, align='center')
target.save('./static/test.png')